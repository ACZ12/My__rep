import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.1.8",9999))
print("Connected")
print(s.recv(1024))
s.close()