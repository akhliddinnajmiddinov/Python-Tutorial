# client.py
import websocket
import threading

# Function to send messages
def send_message(ws):
    while True:
        message = input("You: ")
        ws.send(message)

# Function to receive messages
def on_message(ws, message):
    print(f"Server: {message}")

# Function to handle errors
def on_error(ws, error):
    print(f"Error: {error}")

# Function to handle connection close
def on_close(ws, close_status_code, close_msg):
    print("### Disconnected ###")

# Main client function
def on_open(ws):
    threading.Thread(target=send_message, args=(ws,)).start()

if __name__ == "__main__":
    ws = websocket.WebSocketApp("ws://localhost:12345",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
