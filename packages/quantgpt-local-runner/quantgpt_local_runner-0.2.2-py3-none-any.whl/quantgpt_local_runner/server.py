from fastapi import FastAPI, WebSocket
from io import StringIO
import contextlib
import json
import logging
import traceback
from datetime import datetime
from termcolor import colored

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI(title="QuantGPT Local Runner")

# Global namespace for code execution
GLOBALS = {
    '__name__': '__main__',
    'print': print,
}

# Import commonly used scientific packages into the execution namespace if available
try:
    import numpy as np  # type: ignore
    import pandas as pd  # type: ignore
    import vectorbtpro as vbt  # type: ignore

    GLOBALS.update({
        'np': np,
        'pd': pd,
        'vbt': vbt,
    })
    logging.getLogger(__name__).info(colored("Successfully imported scientific packages (numpy, pandas, vectorbtpro)", "green"))
except Exception as e:  # Broad on purpose: all are optional
    logging.getLogger(__name__).warning(colored(f"Optional packages not fully available: {e}", "yellow"))

@app.get("/")
async def root():
    return {"message": "Hello from QuantGPT Local Runner"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    try:
        logger.debug(colored(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Client attempting to connect...", "cyan"))
        await websocket.accept()
        logger.info(colored(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Client connected successfully", "green"))

        while True:
            try:
                logger.debug(colored(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Waiting for message...", "cyan"))
                data = await websocket.receive_text()
                logger.debug(colored(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Received raw data: {data}", "cyan"))

                try:
                    parsed_data = json.loads(data)
                    logger.debug(colored(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Parsed data: {parsed_data}", "cyan"))
                    code = parsed_data["code"]
                    logger.debug(colored(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Code to execute: {code}", "cyan"))

                    stdout = StringIO()
                    with contextlib.redirect_stdout(stdout):
                        try:
                            logger.debug(colored(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Compiling code...", "cyan"))
                            compiled_code = compile(code, '<string>', 'exec')

                            logger.debug(colored(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Executing code...", "cyan"))
                            exec(compiled_code, GLOBALS)

                            output = stdout.getvalue()
                            logger.debug(colored(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Code execution successful. Output: {output}", "green"))

                            await websocket.send_json({
                                "status": "completed",
                                "content": output or "Code executed successfully",
                                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                            })
                            logger.debug(colored(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Response sent to client", "green"))
                        except Exception as e:
                            error_msg = f"Error: {str(e)}\n{traceback.format_exc()}"
                            logger.error(colored(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Code execution error: {error_msg}", "red"))
                            await websocket.send_json({
                                "status": "failed",
                                "content": error_msg,
                                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                            })
                except json.JSONDecodeError as e:
                    logger.error(colored(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] JSON decode error: {e}", "red"))
                    await websocket.send_json({
                        "status": "failed",
                        "content": f"Invalid JSON: {str(e)}",
                        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    })
                    continue
                except KeyError as e:
                    logger.error(colored(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Missing 'code' key in data: {e}", "red"))
                    await websocket.send_json({
                        "status": "failed",
                        "content": "Missing 'code' in request",
                        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    })
                    continue

            except Exception as e:
                # Likely connection closed or fatal read error; avoid sending on a closed socket
                logger.error(colored(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error handling message: {str(e)}\n{traceback.format_exc()}", "red"))
                break

    except Exception as e:
        logger.error(colored(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] WebSocket connection error: {str(e)}\n{traceback.format_exc()}", "red"))