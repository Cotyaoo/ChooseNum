
import random

def choose_number():
    a = random.randint(1, 100)

    b = int(input("Введите число от 1 до 100:    "))

    p = 0

    while p < 15:

        if a != b:

            print("Не угадали! Компьютер загадал число: ", a)

            return choose_number()

            p += 1

        elif a == b:

            print("Вы угадали")

        break


choose_number()
