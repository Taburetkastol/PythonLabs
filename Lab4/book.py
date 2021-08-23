import date
import library
import datetime

class Book():
    # конструктор по умолчанию и с заданными аргументами
    def __init__(self, library1 = library.Library("Глобальная"), name = "Мастер и Маргарита", count = 500, price = 666, date = date.Date(1, 1, 1970)):
        self.__library1 = library1
        self.__name = name
        self.__count = count
        self.__price = price
        self.__date = date
        print("Книга создана")

    # деструктор
    def __del__(self):
        print(self.__name, "удалена")


    # геттеры
    @property
    def name(self):
        return self.__name

    @property
    def count(self):
        return self.__count
    
    @property
    def price(self):
        return self.__price

    # сеттеры
    @name.setter
    def name(self, name):
        if name == "":
            print("Вы ничего не ввели")
        else:
            self.__name = name
    
    @count.setter
    def count(self, count):
        if count > 0:
            self.__count = count
        else:
            print("Количество страниц должно быть положительным")

    @price.setter
    def price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Цена должна быть положительной")

    # метод вычисления кол-ва лет книге
    def age_of_book(self):
        now = datetime.datetime.now()
        return now.year - self.__date.year

    # метод вычисления кол-ва дней книге с учетом високосности года
    def days_of_book(self):
        now = datetime.datetime.now()
        sum = 0
        d = self.__date.day
        m = self.__date.month
        y = self.__date.year
        while d != now.day or m != now.month or y != now.year:
            if y != now.year:
                while m != 13:
                    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                        while d != 32:
                            d += 1
                            sum += 1
                        d = 1
                    elif m == 2:
                        if self.__date.check_even_year(y):
                            while d != 30:
                                d += 1
                                sum += 1
                            d = 1
                        else:
                            while d != 29:
                                d += 1
                                sum += 1
                            d = 1
                    else:
                        while d != 31:
                            d += 1
                            sum += 1
                        d = 1
                    m += 1
                y += 1
                m = 1
            else:
                while m != now.month:
                    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                        while d != 32:
                            d += 1
                            sum += 1
                        d = 1
                    elif m == 2:
                        if self.__date.check_even_year(y):
                            while d != 30:
                                d += 1
                                sum += 1
                            d = 1
                        else:
                            while d != 29:
                                d += 1
                                sum += 1
                            d = 1
                    else:
                        while d != 31:
                            d += 1
                            sum += 1
                        d = 1
                    m += 1
                while d != now.day:
                    d += 1
                    sum += 1
        return sum


    # переопределение метода вывода информации об объекте
    def display_info(self): 
        print("Библиотека: " + str(library.Library.library_name))
        print("Название: " + self.__name + "\nКоличество страниц: " + str(self.__count) + "\nЦена: " + str(self.__price) + "\nДата выхода: {}.{}.{}".format(self.__date.day, self.__date.month, self.__date.year))

    # переопределение стандартного метода суперкласса Object __str__
    def __str__(self):
        s = library.Library.__str__(self)
        s += "\nНазвание: {}\nКоличество страниц: {}\nЦена: {}\nДата выхода: {}.{}.{}".format(self.__name, self.__count, self.__price, self.__date.day, self.__date.month, self.__date.year)
        return s