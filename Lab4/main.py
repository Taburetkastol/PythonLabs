import book
import library
import date

i = 0
k = int(input("Вы хотите ввести новую книгу?\n1. Да\n2. Нет\n"))
if k == 1:
    library_name = input("Введите название библиотеки: ")
    name = input("Введите название книги: ")
    count = int(input("Введите количество копий: "))
    price = int(input("Введите цену книги: "))
    day = int(input("Введите день релиза: "))
    month = int(input("Введите месяц релиза: "))
    year = int(input("Введите год релиза: "))

    book_array = [book.Book(library.Library(library_name), name, count, price, date.Date(day, month, year))]

    book_array[i].display_info()
    print("\n" + str(book_array[i].age_of_book()) + " лет книге")
    print(str(book_array[i].days_of_book()) + " дней книге\n")

    k = int(input("\nВы хотите ввести новую книгу?\n1. Да\n2. Нет\n"))
while k == 1:
    i += 1
    library_name = input("Введите название библиотеки: ")
    name = input("Введите название книги: ")
    count = int(input("Введите количество копий: "))
    price = int(input("Введите цену книги: "))
    day = int(input("Введите день релиза: "))
    month = int(input("Введите месяц релиза: "))
    year = int(input("Введите год релиза: "))

    book_array.append(book.Book(library.Library(library_name), name, count, price, date.Date(day, month, year)))

    book_array[i].display_info()
    print("\n" + str(book_array[i].age_of_book()) + " лет книге")
    print(str(book_array[i].days_of_book()) + " дней книге\n")

    k = int(input("\nВы хотите ввести новую книгу?\n1. Да\n2. Нет\n"))