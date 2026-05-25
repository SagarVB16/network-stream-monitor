from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from app.websocket_manager import (
    connect,
    disconnect
)

app = FastAPI(
    title="IP Network Stream Monitor",
    version="1.0.0"
)


@app.get("/")
def home():

    return {
        "status": "running",
        "message": "WebSocket monitoring server active"
    }


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await connect(websocket)

    try:

        while True:

            await websocket.receive_text()

    except WebSocketDisconnect:

        disconnect(websocket)