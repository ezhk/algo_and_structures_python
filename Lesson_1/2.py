#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2. Выполнить логические побитовые операции "И", "ИЛИ" и др.
# над числами 5 и 6. Выполнить
# над числом 5 побитовый сдвиг вправо и влево на два знака.


def operator_and(a, b):
    return a & b


def operator_or(a, b):
    return a | b


def left_shift(a, count):
    return a << count


def right_shift(a, count):
    return a >> count


if __name__ == '__main__':
    # 5 & 6 = 0b101 & 0b110 = 0b100 = 4
    print(f"5 AND 6 = {operator_and(5, 6)}")

    # 5 | 6 = 0b101 | 0b110 = 0b111 = 7
    print(f"5 OR 6 = {operator_or(5, 6)}")

    # 5 << 2 = 0b101 << 2 = 0b1010 << 1 = 0b10100 = 16+4 = 20
    print(f"5 << 2 = {left_shift(5, 2)}")

    # 5 << 2 = 0b101 >> 2 = 0b10 >> 1 = 0b1 = 1
    print(f"5 >> 2 = {right_shift(5, 2)}")
