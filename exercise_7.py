# Написать функцию date, принимающую 3 аргумента — день, месяц и год. Вернуть True, если такая дата есть в
# нашем календаре, и False иначе.
from datetime import date


def data(day, month, year):
    try:
        date(year, month, day)
        print("Дата существует")
    except:
        print("Даты нет")


day = int(input("Введите день: "))
month = int(input('Введите месяц: '))
year = int(input('Введите год: '))
print(data(day, month, year))
