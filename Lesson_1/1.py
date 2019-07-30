#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.


def find_numbers(value):
    """
    Function get all numbers in string as determinate symbols
    :param value: number string
    :return (numbers,): tuple of numbers
    """
    int_value = int(value)
    first = int_value // 100 % 100
    second = int_value // 10 % 10
    third = int_value % 10

    return first, second, third


def calc_sum(value):
    """Calculate sum of string numbers.
    :param value: number string
    :return number: integer value
    """
    first, second, third = find_numbers(value)
    return first + second + third


def calc_mul(value):
    """Calculate multiple of string numbers.
    :param value: number string
    :return number: integer value
    """
    first, second, third = find_numbers(value)
    return first * second * third


if __name__ == '__main__':
    value = input("Введите 3-значное число: ")
    print(f"Сумма чисел числа {value} = {calc_sum(value)}")
    print(f"Произведение чисел числа {value} = {calc_mul(value)}")
