#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

def search_middle_number(a, b, c):
    min = a
    if min > b:
        min = b
    if min > c:
        min = c

    max = a
    if max < b:
        max = b
    if max < c:
        max = c

    print(f"\tМинимальное число: {min}")
    print(f"\tМаксмиальное число: {max}")

    if max > a > min:
        return a
    if max > b > min:
        return b
    if max > c > min:
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
