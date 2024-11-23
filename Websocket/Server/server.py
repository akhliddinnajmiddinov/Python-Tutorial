import asyncio
import websockets

# List to hold all connected clients
clients = set()

# Function to handle incoming messages from clients
async def handle_client(websocket, path):
    clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Client says: {message}")
            # Broadcast the message to all clients
            await asyncio.gather(*(client.send(f"Client: {message}") for client in clients))
    except websockets.ConnectionClosed:
        print(f"Client disconnected")
    finally:
        clients.remove(websocket)

# Function for the server to periodically send messages
async def send_server_message():
    while True:
        await asyncio.sleep(10)  # Server sends a message every 10 seconds
        message = "Server says: Hello to all clients!"
        print(message)
        if clients:  # If there are connected clients
            await asyncio.gather(*(client.send(message) for client in clients))

# Main function to run both server and server messages
async def main():
    # Start WebSocket server
    async with websockets.serve(handle_client, "localhost", 12345):
        print("Server running on ws://localhost:12345")
        
        # Run server message broadcaster alongside handling clients
        await asyncio.gather(
            send_server_message(),  # Periodic server messages
            asyncio.Future()        # Keep the server running indefinitely
        )

asyncio.run(main())
