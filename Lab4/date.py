import datetime

class Date:
    # конструктор по умолчанию и с заданными аргументами
    def __init__(self, day = 1, month = 1, year = 1970):
        self.__day = day
        self.__month = month
        self.__year = year

    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month
    
    @property
    def year(self):
        return self.__year

    @day.setter
    def day(self, day):
        if self.__month == 1 or self.__month == 3 or self.__month == 5 or self.__month == 7 or self.__month == 8 or self.__month == 10 or self.__month == 12:
            if 1 <= day <= 31:
                self.__day = day
            else:
                print("Нет такого дня в этом месяце")
        if self.__month == 2:
            if self.check_even_year(self.__year):
                if 1 <= day <= 29:
                    self.__day = day
                else:
                    print("Нет такого дня в этом месяце")
            else:
                if 1 <= day <= 28:
                    self.__day = day
                else:
                    print("Нет такого дня в этом месяце")

    @month.setter
    def month(self, month):
        if 1 <= month <= 12:
            self.__month = month
        else:
            print("Нет такого месяца")

    @year.setter
    def year(self, year):
        if year >= 0:
            if year <= 2020:
                self.__year = year
            else:
                print("Вы из будущего?")
        else:
            print("Введите корректное значение")


    # проверка на високосность
    def check_even_year(self, year):
        temp = year
        if temp % 4 == 0:
            if (temp // 100) % 4 != 0:
                return False
            else:
                return True
        else:
            return False
