active_connections = []


async def connect(websocket):

    await websocket.accept()

    active_connections.append(websocket)

    print("New dashboard client connected")


def disconnect(websocket):

    active_connections.remove(websocket)

    print("Dashboard client disconnected")


async def broadcast_message(message):

    disconnected_clients = []

    for connection in active_connections:

        try:

            await connection.send_text(message)

        except:

            disconnected_clients.append(connection)

    for client in disconnected_clients:

        disconnect(client)