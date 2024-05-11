# Завдання
# Є словник з друзями, де ключ – людина, а значення –
# список друзів. Користувач вводить імена двох людей,
# які є друзями, повторює це певну кількість разів,
# після чого дані зберігаються у файл.
# Завантажте дані назад та виведіть на екран.
import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Сервер запущено. Очікування з'єднання...")

    while True:
        connection, address = server_socket.accept()
        print("З'єднання від:", address)

        while True:
            message = connection.recv(1024).decode()
            if not message:
                print("Клієнт відключився")
                break
            print("Клієнт:", message)

            response = input("Введіть відповідь сервера: ")
            connection.send(response.encode())

        connection.close()

if __name__ == "__main__":
    start_server()
