"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""

import random


def get_randfloat(min_value, max_value):
    return min_value + random.random() * (max_value - min_value)


def get_randint(min_value, max_value):
    # make round() logic as (float_X + 0.5) // 1
    return int((get_randfloat(min_value, max_value) + 0.5) // 1)


def play_the_game():
    print(f"Попробуйте угадать число от 0 до 100, у тебя 10 попыток")
    value = get_randint(0, 100)

    for i in range(10):
        user_value = int(input(f"Попытка {i + 1}, введите целое число: "))
        if user_value == value:
            print("Вы выиграли!")
            return True
        elif user_value > value:
            print("Ваше число больше")
        elif user_value < value:
            print("Ваше число меньше")

    print("Вы проиграли")
    return False


if __name__ == "__main__":
    play_the_game()
