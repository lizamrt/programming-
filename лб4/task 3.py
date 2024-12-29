import socket

HOST = '127.0.0.1'
PORT = 65432

def send_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_data = file.read()
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))
            print(f"Підключено до сервера {HOST}:{PORT}")
            
            client_socket.sendall(file_data.encode('utf-8'))
            print(f"Файл '{file_path}' успішно відправлено.")
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено. Перевірте шлях до файлу.")
    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == '__main__':
    file_path = input("Введіть шлях до текстового файлу: ")
    send_file(file_path)
