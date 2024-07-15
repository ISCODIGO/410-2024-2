import socket

DOMAIN = "data.pr4e.org"
PORT = 80
URL = "http://data.pr4e.org"

misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
misock.connect((DOMAIN, PORT))
cmd = f"GET {URL} HTTP/1.0\r\n\r\n".encode()
misock.send(cmd)

while True:
    datos = misock.recv(512)
    if len(datos) < 1:
        break
    print(datos.decode(), end="")

misock.close()
