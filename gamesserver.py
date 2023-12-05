import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 5555

# List to store client sockets
clients = []

# Server socket setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

def broadcast(message, sender_socket):
    for client_socket in clients:
        if client_socket != sender_socket:
            try:
                client_socket.send(message)
            except:
                # Handle potential errors, e.g., if the connection is lost
                remove_client(client_socket)

def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

def handle_client(client_socket, addr):
    print(f"Accepted connection from {addr}")
    client_socket.send("Welcome to the chat!".encode('utf-8'))

    try:
        while True:
            message = client_socket.recv(1024)
            if not message:
                break
            message = message.decode('utf-8')
            print(f"Received from {addr}: {message}")
            broadcast(message.encode('utf-8'), client_socket)
    except:
        # Handle potential errors, e.g., if the connection is lost
        pass

# Accept incoming connections
print(f"Server listening on {HOST}:{PORT}")
while True:
    client_socket, addr = server.accept()
    clients.append(client_socket)

    # Create a new thread for each client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_thread.start()
