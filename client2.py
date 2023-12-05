import socket
import threading

nickname = input("Choose a nickname: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 9999))


def receive():
    while True:
        try:
            # Receive messages from the server
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            # Handle potential errors, for example, if the connection is lost
            print("An error occurred!")
            client.close()
            break


def write():
    while True:
        try:
            # Send messages to the server
            message = f'{nickname}: {input("")}'
            client.send(message.encode('utf-8'))
        except:
            # Handle potential errors, for example, if the connection is lost
            print("An error occurred!")
            client.close()
            break


# Create and start two threads: one for receiving messages, and one for writing messages
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
