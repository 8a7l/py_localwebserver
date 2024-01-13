from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import os

# Шлях до папки з вашим сайтом
site_folder = '/path/to/your/site'

# Встановлення IP-адреси та порту
host = '127.0.0.1'
port = 8000

# Зміна поточного каталогу на папку сайту
os.chdir(site_folder)

class MyHandler(SimpleHTTPRequestHandler):
    pass

if __name__ == '__main__':
    # Створення сервера з класом обробника SimpleHTTPRequestHandler
    server_address = (host, port)
    httpd = TCPServer(server_address, MyHandler)

    print(f"Сервер запущений на http://{host}:{port}/")

    # Запуск сервера
    httpd.serve_forever()
