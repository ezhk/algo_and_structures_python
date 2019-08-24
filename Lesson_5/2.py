# -*- coding: utf-8 -*-

"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import UserList


class HexNumbers:
    def __init__(self, value):
        self.key = value.lower()
        self.presentation = UserList([x for x in value.upper()])

    def __str__(self):
        return f"{self.presentation.data}"

    def __mul__(self, other):
        return HexNumbers(f"{int(self.key, 16) * int(other.key, 16):x}")

    def __add__(self, other):
        return HexNumbers(f"{int(self.key, 16) + int(other.key, 16):x}")


if __name__ == "__main__":
    first_hex = HexNumbers(input("Введите первое 16-ричное число: "))
    second_hex = HexNumbers(input("Введите второе 16-ричное число: "))

    print(f"Сумма чисел {first_hex} и {second_hex}: {first_hex + second_hex}")
    print(f"Произведение чисел {first_hex} и {second_hex}: {first_hex * second_hex}")
