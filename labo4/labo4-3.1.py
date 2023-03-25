import socket

serverAddress = ('0.0.0.0', 3000)

with socket.socket() as s:
    s.bind(serverAddress)
    s.listen()
    client, address = s.accept()
    with client:
        message = client.recv(2048).decode()
    print(message)