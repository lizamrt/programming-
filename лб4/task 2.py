import socket

HOST = '127.0.0.1'
PORT = 65432

def handle_client(conn, addr):
    print(f"Підключено клієнта: {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Отримано від {addr}: {data.decode('utf-8')}")
            conn.sendall(data)
    print(f"Клієнт {addr} від'єднався.")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Сервер запущено на {HOST}:{PORT}, очікування клієнтів...")

    while True:
        conn, addr = server_socket.accept()
        handle_client(conn, addr)
