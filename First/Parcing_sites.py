# Импортируем модуль
import requests


# создаем класс виртуальных сайтов
class Virtualsite:
    # Стандартная функцция Init
    def __init__(self, name):
        self.name = name

    # создаем запрос на сайт, st_accept- желаемый формат получения данных, st_useragent - данные браузера,
    # с которого отправляется запрос. page- страница сайта(В нынешнем случае валюта)
    def request(self, st_accept="text/html", st_useragent="", src="", page=""):
        self.headers = {"Accept": st_accept,
                        "User-Agent": st_useragent}
        src1 = src + "/" + page
        req = requests.get(src1, self.headers)
        return req

    # Получение значения нужных переменных
    def get_count(self, *variable):
        ...


__name__ = '__main__'
