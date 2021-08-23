import book
import library
import date

def load():
    try:
        name = input("Введите имя файла(не забудьте расширение .bin): ")
        file = open(name, 'rb')
        try:
            l = int(file.readline())
        except:
            print("Файл ни разу не записывался")
        book_array = [book.Book(library.Library(str(file.readline())), str(file.readline()), int(file.readline()), int(file.readline()), date.Date(int(file.readline()), int(file.readline()), int(file.readline())))]
        for item in range(1, l):
            book_array.insert(book.Book(library.Library(str(file.readline())), str(file.readline()), int(file.readline()), int(file.readline()), date.Date(int(file.readline()), int(file.readline()), int(file.readline()))))
        return book_array
    except:
        print("Не удалось найти файл либо ошибка при чтении")
        return 0
    file.close()


def save(book_array, name):
    file = open(name, 'wb')
    file.write((str(len(book_array)) + "\n").encode())
    for item in book_array:
        file.write((item.library_name.library_name + "\n").encode())
        file.write((item.name + "\n").encode())
        file.write((str(item.count) + "\n").encode())
        file.write((str(item.price) + "\n").encode())
        file.write((str(item.date.day) + "\n").encode())
        file.write((str(item.date.month) + "\n").encode())
        file.write((str(item.date.year) + "\n").encode())
    file.close()


class NameException(Exception):
    pass


i = 0
t1 = 0
t2 = 0
k = int(input("Вы хотите ввести новую книгу?\n1. Да\n2. Нет\n3. Загрузить\n"))
assert 0 < k < 4, "Неправильный ввод"
if k == 1:
    t1 = 0
    t2 = 0
    while t1 <= t2:
        try:
            library_name = input("Введите название библиотеки: ")
            if type(library_name, int):
                raise NameException
            t1 += 1
        except:
            t2 += 1
            print("Неправильный ввод")
    t1 = 0
    t2 = 0
    while t1 <= t2:
        try:
            name = input("Введите название книги: ")
            t1 += 1
        except:
            t2 += 1
            print("Неправильный ввод")
    t1 = 0
    t2 = 0
    while t1 <= t2:
        try:
            count = int(input("Введите количество копий: "))
            if int(count) < 0:
                raise Exception
            t1 += 1
        except:
            t2 += 1
            print("Неправильный ввод")
    t1 = 0
    t2 = 0
    while t1 <= t2:
        try:
            price = int(input("Введите цену книги: "))
            if price < 0:
                raise Exception
            t1 += 1
        except:
            t2 += 1
            print("Неправильный ввод")
    t1 = 0
    t2 = 0
    while t1 <= t2:
        try:
            day = int(input("Введите день релиза: "))
            if day < 0 or day > 31:
                raise Exception
            t1 += 1
        except:
            t2 += 1
            print("Неправильный ввод")
    t1 = 0
    t2 = 0
    while t1 <= t2:
        try:
            month = int(input("Введите месяц релиза: "))
            if month < 0 or month > 12:
                raise Exception
            t1 += 1
        except:
            t2 += 1
            print("Неправильный ввод")
    t1 = 0
    t2 = 0
    while t1 <= t2:
        try:
            year = int(input("Введите год релиза: "))
            if year < 0:
                raise Exception
            t1 += 1
        except:
            t2 += 1
            print("Неправильный ввод")

    book_array = [book.Book(library.Library(library_name), name, count, price, date.Date(day, month, year))]

    book_array[i].display_info()
    print("\n" + str(book_array[i].age_of_book()) + " лет книге")
    print(str(book_array[i].days_of_book()) + " дней книге\n")

    t1 = 0
    t2 = 0
    while t1 <= t2:
        try:
            k = int(input("Вы хотите ввести новую книгу?\n1. Да\n2. Нет\n3. Загрузить\n4. Сохранить\n"))
            t1 += 1
        except:
            t2 += 1
            print("Неправильный ввод")
if k == 3:
    try:
        book_array = load()
    except:
        print("Такого файла нет или ошибка при загрузке")
    t1 = 0
    t2 = 0
    while t1 <= t2:
        try:
            k = int(input("Вы хотите ввести новую книгу?\n1. Да\n2. Нет\n3. Загрузить\n4. Сохранить\n"))
            t1 += 1
        except:
            t2 += 1
            print("Неправильный ввод")
elif k == 4:
    name = input("Введите имя файла(не забудьте расширение .bin): ")
    try:
        save(book_array, name)
    except:
        print("Ошибка при сохранении")
    t1 = 0
    t2 = 0
    while t1 <= t2:
        try:
            k = int(input("Вы хотите ввести новую книгу?\n1. Да\n2. Нет\n3. Загрузить\n4. Сохранить\n"))
            t1 += 1
        except:
            t2 += 1
            print("Неправильный ввод")
while k != 2:
    i += 1
    t1 = 0
    t2 = 0
    if k == 1:
        t1 = 0
        t2 = 0
        while t1 <= t2:
            try:
                library_name = input("Введите название библиотеки: ")
                t1 += 1
            except:
                t2 += 1
                print("Неправильный ввод")
        t1 = 0
        t2 = 0
        while t1 <= t2:
            try:
                name = input("Введите название книги: ")
                t1 += 1
            except:
                t2 += 1
                print("Неправильный ввод")
        t1 = 0
        t2 = 0
        while t1 <= t2:
            try:
                count = int(input("Введите количество копий: "))
                if int(count) < 0:
                    raise Exception
                t1 += 1
            except:
                t2 += 1
                print("Неправильный ввод")
        t1 = 0
        t2 = 0
        while t1 <= t2:
            try:
                price = int(input("Введите цену книги: "))
                if price < 0:
                    raise Exception
                t1 += 1
            except:
                t2 += 1
                print("Неправильный ввод")
        t1 = 0
        t2 = 0
        while t1 <= t2:
            try:
                day = int(input("Введите день релиза: "))
                if day < 0 or day > 31:
                    raise Exception
                t1 += 1
            except:
                t2 += 1
                print("Неправильный ввод")
        t1 = 0
        t2 = 0
        while t1 <= t2:
            try:
                month = int(input("Введите месяц релиза: "))
                if month < 0 or month > 12:
                    raise Exception
                t1 += 1
            except:
                t2 += 1
                print("Неправильный ввод")
        t1 = 0
        t2 = 0
        while t1 <= t2:
            try:
                year = int(input("Введите год релиза: "))
                if year < 0:
                    raise Exception
                t1 += 1
            except:
                t2 += 1
                print("Неправильный ввод")

        book_array.append(book.Book(library.Library(library_name), name, count, price, date.Date(day, month, year)))

        book_array[i].display_info()
        print("\n" + str(book_array[i].age_of_book()) + " лет книге")
        print(str(book_array[i].days_of_book()) + " дней книге\n")

        t1 = 0
        t2 = 0
        while t1 <= t2:
            try:
                k = int(input("Вы хотите ввести новую книгу?\n1. Да\n2. Нет\n3. Загрузить\n4. Сохранить\n"))
                t1 += 1
            except:
                t2 += 1
                print("Неправильный ввод")
    if k == 3:
        try:
            book_array = load()
        except:
            print("Такого файла нет или ошибка при загрузке")
        t1 = 0
        t2 = 0
        while t1 <= t2:
            try:
                k = int(input("Вы хотите ввести новую книгу?\n1. Да\n2. Нет\n3. Загрузить\n4. Сохранить\n"))
                t1 += 1
            except:
                t2 += 1
                print("Неправильный ввод")
    elif k == 4:
        name = input("Введите имя файла(не забудьте расширение .bin): ")
        try:
            save(book_array, name)
        except:
            print("Ошибка при сохранении")
        t1 = 0
        t2 = 0
        while t1 <= t2:
            try:
                k = int(input("Вы хотите ввести новую книгу?\n1. Да\n2. Нет\n3. Загрузить\n4. Сохранить\n"))
                t1 += 1
            except:
                t2 += 1
                print("Неправильный ввод")

    