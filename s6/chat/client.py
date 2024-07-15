import socket


def receive_messages(client_socket):
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            print("Conexión cerrada por el servidor.")
            break
        print(f"SERVIDOR: {data}")


def send_messages(client_socket):
    while True:
        message = input("Escriba un mensaje para enviar al servidor: ")
        if message.lower() == "exit":
            print("Terminando la conexión.")
            client_socket.close()
            break
        client_socket.send(message.encode())


def start_client(host="localhost", port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        receive_messages(client_socket)
        send_messages(client_socket)


start_client()
