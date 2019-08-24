#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
7.	По длинам трех отрезков, введенных пользователем, определить возможность
существования треугольника, составленного из этих отрезков. Если такой
треугольник существует, то определить, является ли он
разносторонним, равнобедренным или равносторонним.
"""


def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False


def is_equilateral_triangle(a, b, c):
    return a == b == c


def is_right_triangle(a, b, c):
    a_sq, b_sq, c_sq = a ** 2, b ** 2, c ** 2
    if (a_sq + b_sq == c_sq
            or a_sq + c_sq == b_sq
            or b_sq + c_sq == a_sq):
        return True
    return False


def is_isosceles_triangle(a, b, c):
    if a == b or a == c or b == c:
        return True
    return False


if __name__ == '__main__':
    a = float(input("Введите длину первой стороны треугольника: "))
    b = float(input("Введите длину второй стороны треугольника: "))
    c = float(input("Введите длину третьей стороны треугольника: "))

    if is_triangle(a, b, c):
        print("Такой треугольник существовать может")
    else:
        print("Такой треугольник существовать не может")
        quit()

    if is_equilateral_triangle(a, b, c):
        print("\t- это равносторонний треугольник")
        quit()

    print(f"\t- это равнобедренный треугольник: {is_isosceles_triangle(a, b, c)}")
    print(f"\t- это прямоугольный треугольник: {is_right_triangle(a, b, c)}")
