import date

class Library():
    def __init__(self, library_name = "Глобальная"):
        self.__library_name = library_name
        print("Библиотека создана")

    def __del__(self):
        print(self.__library_name + " библиотека уничтожена")

    @property
    def library_name(self):
        return self.__library_name

    @library_name.setter
    def library_name(self, name):
        self.__library_name = name

    # виртуальный метод вывода информации о библиотеке
    def display_info(self):
        print("\nБиблиотека: " + self.__library_name)

    def __str__(self):
        return "Библиотека: {}".format(self.__library_name)