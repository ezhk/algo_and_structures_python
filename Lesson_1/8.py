#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 8.	Определить, является ли год, который ввел пользователем,
# високосным или не високосным.
# Год является високосным в двух случаях: либо он кратен 4,
# но при этом не кратен 100, либо кратен 400.


def is_leap_year(year):
    if (year % 400 == 0
            or (year % 100 != 0
                and year % 4 == 0)):
        return True
    return False


if __name__ == '__main__':
    year = int(input("Введите год: "))
    print("Это високосный год:", 'Да' if is_leap_year(year) else 'Нет')
