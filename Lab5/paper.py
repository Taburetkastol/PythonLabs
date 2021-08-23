import book
import date
import library

class paper():
    def __init__(self, library1 = library.Library("Глобальная"), book = book.Book(name = "Мастер и Маргарита", count = 500, price = 666, date = date.Date(1, 1, 1970)), text = "", number = 1):
        self.__library1 = library1
        self.__book = book
        self.__text = text
        self.__number = number
        print("Страница создана")

    def __del__(self):
        print("Страница уничтожена")

    @property
    def text(self):
        return self.__text

    @property
    def number(self):
        return self.__number

    def print_text(self):
        print(self.__text)