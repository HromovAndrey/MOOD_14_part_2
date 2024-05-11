#Client
import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    print("Підключено до сервера.")

    while True:
        message = input("Введіть повідомлення: ")
        client_socket.send(message.encode())

        response = client_socket.recv(1024).decode()
        print("Сервер:", response)

        if message.lower() == 'exit':
            break

    client_socket.close()

if __name__ == "__main__":
    start_client()
