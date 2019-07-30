#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

def search_middle_number(a, b, c):
    def _find_min(a, b, c):
        """
        Function search minimum value from 3 params
        :param a: integer or float value
        :param b: integer or float value
        :param c: integer or float value
        :return minimum value: integer or float
        """
        min = a
        if min > b:
            min = b
        if min > c:
            min = c
        return min

    def _find_max(a, b, c):
        """
        Function search maximum value from 3 params
        :param a: integer or float value
        :param b: integer or float value
        :param c: integer or float value
        :return maximum value: integer or float
        """
        max = a
        if max < b:
            max = b
        if max < c:
            max = c
        return max

    def _is_middle(min, value, max):
        """
        Function check that middle argument less than max and more than min
        :param min: integer or float value
        :param value: integer or float value
        :param max: integer or float value
        :return result of expression: bool
        """
        return min < value < max

    min = _find_min(a, b, c)
    max = _find_max(a, b, c)
    print(f"\tМинимальное число: {min}")
    print(f"\tМаксмиальное число: {max}")

    if _is_middle(min, a, max):
        return a
    if _is_middle(min, b, max):
        return b
    if _is_middle(min, c, max):
        return c

    return None


if __name__ == '__main__':
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    c = float(input("Введите третье число: "))

    result = search_middle_number(a, b, c)
    if result is None:
        print("Среднее число не найдено")
        quit()

    print(f"Среднее число: {result}")
