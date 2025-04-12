# это до установки django работало
# Импорт встроенной библиотеки для работы веб-сервера
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

# Для начала определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8000  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    """

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        try:
            with open("catalog/templates/catalog/contacts.html", "r", encoding="UTF-8") as file:
                my_content = file.read()

            self.send_response(200)  # Отправка кода ответа
            # Отправка типа данных, который будет передаваться
            self.send_header("Content-type", "text/Html")
            self.end_headers()  # Завершение формирования заголовков ответа

            # Отправляем содержимое HTML-файла в ответ
            self.wfile.write(bytes(my_content, "UTF-8"))
        except FileNotFoundError:
            # Если файл не найден, отправляем код 404
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>404 - Page Not Found</h1>")

    def do_POST(self):
        """ Метод для обработки входящих POST-запросов """
        try:
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            print(body)
            self.send_response(200)
            self.end_headers()
        except Exception as e:
            print(f"Ошибка обработки POST-запроса {e}")


if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрам в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил
    # адрес и порт в сети, которые занимал - "ctrl + c" или "ctrl + d"
    webServer.server_close()
    print("Server stopped.")

    with open("catalog/templates/catalog/contacts.html", encoding="UTF-8") as file:
        content = file.read()
