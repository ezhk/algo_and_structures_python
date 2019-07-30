#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""

from random import random


def get_randfloat(min_value, max_value):
    return min_value + random() * (max_value - min_value)


def get_randint(min_value, max_value):
    # make round() logic as (float_X + 0.5) // 1
    return int((get_randfloat(min_value, max_value) + 0.5) // 1)


def get_randsymbol(min_symbol, max_symbol):
    min_value, max_value = ord(min_symbol), ord(max_symbol)
    return chr(get_randint(min_value, max_value))


if __name__ == '__main__':
    min_input_value = float(input("Введите начальное значение числа с плавающей точкой: "))
    max_input_value = float(input("Введите конечное значение числа с плавающей точкой: "))
    print(f"Float {min_input_value} .. {max_input_value} = {get_randfloat(min_input_value, max_input_value)}")

    min_input_value = int(input("Введите начальное значение целого числа: "))
    max_input_value = int(input("Введите конечное значение елого числа: "))
    print(f"Integer {min_input_value} .. {max_input_value} = {get_randint(min_input_value, max_input_value)}")

    min_input_symbol = input("Введите начальный символ алфавита: ")
    max_input_symbol = input("Введите конечный символ алфавита: ")
    print(f"Alphabet {min_input_symbol} .. {max_input_symbol} = {get_randsymbol(min_input_symbol, max_input_symbol)}")
