from fastapi import FastAPI, WebSocket
import asyncio
import sys
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

app = FastAPI()

# Global namespace for code execution
GLOBALS = {
    '__name__': '__main__',
    'print': print  # Ensure print is available
}

# Import commonly used packages
try:
    import numpy as np
    import pandas as pd
    import vectorbtpro as vbt
    GLOBALS.update({
        'np': np,
        'pd': pd,
        'vbt': vbt
    })
    logger.info(colored("Successfully imported scientific packages", "green"))
except ImportError as e:
    logger.warning(colored(f"Could not import some packages: {e}", "yellow"))

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
                                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            })
                            logger.debug(colored(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Response sent to client", "green"))
                        except Exception as e:
                            error_msg = f"Error: {str(e)}\n{traceback.format_exc()}"
                            logger.error(colored(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Code execution error: {error_msg}", "red"))
                            await websocket.send_json({
                                "status": "failed",
                                "content": error_msg,
                                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            })
                except json.JSONDecodeError as e:
                    logger.error(colored(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] JSON decode error: {e}", "red"))
                    await websocket.send_json({
                        "status": "failed",
                        "content": f"Invalid JSON: {str(e)}",
                        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    })
                    continue
                except KeyError as e:
                    logger.error(colored(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Missing 'code' key in data: {e}", "red"))
                    await websocket.send_json({
                        "status": "failed",
                        "content": "Missing 'code' in request",
                        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    })
                    continue
                    
            except Exception as e:
                logger.error(colored(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error handling message: {str(e)}\n{traceback.format_exc()}", "red"))
                # Don't try to send on a closed socket!
                break
                
    except Exception as e:
        logger.error(colored(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] WebSocket connection error: {str(e)}\n{traceback.format_exc()}", "red"))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000, 
        log_level="debug",
        ws_ping_interval=None,
        ws_ping_timeout=None,
    ) 