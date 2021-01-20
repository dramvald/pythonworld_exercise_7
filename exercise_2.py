# Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True,
# если год високосный, и False иначе.
i = "еще"
while i == "еще":
    def is_year_leap(x):
        if x % 4 == 0 and (x % 100 != 0 or x % 400 == 0):
            print(True)
        else:
            print(False)


    is_year_leap(int(input("Введите год ")))
    i = input("Введите \'еще\' для продолжения ")
