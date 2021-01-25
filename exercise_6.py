# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно
# простое, и False - иначе.

def is_prime(i):
    if 0 <= i <= 1000:  # i >= 0 and i <= 1000:
        if i % 2 != 0 and i % 3 != 0 or (i == 2 or i == 3):
            print(True)
        else:
            print(False)
    else:
        print("Вы ввели недопустимое число!")


is_prime(int(input("Введите число от 0 до 1000: ")))
