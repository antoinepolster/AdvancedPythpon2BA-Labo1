import socket

s = socket.socket()
serverAddress = ('0.0.0.0', 3000)
s.bind(serverAddress)

s.listen()

client, address = s.accept()
message = client.recv(2048).decode()
