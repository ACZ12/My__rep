import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("192.168.1.8",9999))
print("Waiting for connection")
s.listen(1)
while 1:
    conn,addr=s.accept()
    print("Connected to",addr)
    conn.send("hello")
    conn.close()