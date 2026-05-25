from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from app.websocket_manager import (
    connect,
    disconnect
)

from app.database import (
    get_metrics_data,
    get_top_ips
)


app = FastAPI(
    title="IP Network Stream Monitor",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():

    return {
        "status": "running",
        "message": "WebSocket monitoring server active"
    }


@app.get("/metrics")
def metrics_endpoint():

    return get_metrics_data()

@app.get("/top-ips")
def top_ips_endpoint():

    return get_top_ips()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await connect(websocket)

    try:

        while True:

            await websocket.receive_text()

    except WebSocketDisconnect:

        disconnect(websocket)