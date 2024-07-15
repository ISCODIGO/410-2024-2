import socket


def handle_client(client_socket):
    while True:
        received_data = client_socket.recv(1024).decode()
        if not received_data:
            print("Conexión cerrada por el cliente.")
            break
        print(f"CLIENTE: {received_data}")

        message = input("Escriba un mensaje para enviar al cliente: ")
        if message.lower() == "exit":
            print("Terminando la conexión.")
            client_socket.close()
            break
        client_socket.send(message.encode())

    client_socket.close()


def start_server(host="localhost", port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Servidor esperando conexiones...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Conexión desde {client_address} ha sido establecida.")
        handle_client(client_socket)


start_server()
