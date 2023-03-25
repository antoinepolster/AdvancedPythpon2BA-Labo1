import socket 

s = socket.socket()

address = ('www.perdu.com', 80)
s.connect(address)

request = 'GET / HTTP/1.1\r\nHost: www.perdu.com\r\n\r\n'.encode()

s.send(request)

response = s.recv(2048).decode()

print(response)

s.close()