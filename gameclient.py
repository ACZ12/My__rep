import socket
import threading

# Client configuration
HOST = '127.0.0.1'
PORT = 5555

# Get user nickname
nickname = input("Choose a nickname: ")

# Connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            # Handle potential errors, e.g., if the connection is lost
            print("An error occurred!")
            break

def write():
    while True:
        try:
            message = input()
            client.send(f'{nickname}: {message}'.encode('utf-8'))
        except:
            # Handle potential errors, e.g., if the connection is lost
            print("An error occurred!")
            break

# Create and start two threads: one for receiving messages, and one for writing messages
receive_thread = threading.Thread(target=receive)
write_thread = threading.Thread(target=write)

receive_thread.start()
write_thread.start()

try:
    # Wait for both threads to finish
    receive_thread.join()
    write_thread.join()
except KeyboardInterrupt:
    # Handle Ctrl+C gracefully
    print("Closing the chat application.")
finally:
    # Close the client socket
    client.close()