#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3.	По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.


def calc_coefficient(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


def calc_const(x1, y1, x2, y2):
    return y1 - (x1 * calc_coefficient(x1, y1, x2, y2))


if __name__ == '__main__':
    x1 = int(input("Введите x-координату (абсциссу) первой точки: "))
    y1 = int(input("Введите y-координату (ординату) первой точки: "))
    x2 = int(input("Введите x-координату (абсциссу) второй точки: "))
    y2 = int(input("Введите y-координату (ординату) второй точки: "))
    print(f"Для точек ({x1}, {y1}) и ({x2}, {y2}) уравнение имеет вид:"
          f" y = {calc_coefficient(x1, y1, x2, y2)} * x + {calc_const(x1, y1, x2, y2)}")
