##Server
import socket
server = socket.socket(socket.AF_INET,#user_IP4
                        socket.SOCK_STREAM)# use_TCP

server.bind(("127.0.0.1",8080))
server.listen(1)

while True:
    print("Waiting..")
    client, address = server.accept()
    print(f"Conection from{address}")

    while True:
        data = client.recv(1024).decode()
        print(data)

        if data == "exit":
            break

        response = input("Enter somethong:")

        client.send(response.encode())
    client.close()



    data = client.recv(1024).decode()
    print(data)


import socket
import threading
def handle_client(client_socket, address):
    print(f"Connection from {address} has been established")

    while True:
        data = client_socket.recv(1024)
        if not data:
           break
        client_socket.sendall(data)

    client_socket.close()

serer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8080))
server_socket.listen(5)
print("Echo server is listening...")


import socket

client = socket.socket(socket.AF_INET,#user_IP4
                        socket.SOCK_STREAM)# use_TCP

client.connect(("127.0.0.1",8080))

while True:
    data = input("Enter something:")

    client.send(data.encode())
    if data == "exit":
        break

    response = client.recv(1024).decode()
    print(response)

client.close()