import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Сервер запущено на {HOST}:{PORT}, очікування з'єднань...")

    while True:
        conn, addr = server_socket.accept()
        with conn:
            print(f"Підключено клієнта: {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Отримано від клієнта: {data.decode('utf-8')}")
                conn.sendall(data)
