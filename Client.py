#Client

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