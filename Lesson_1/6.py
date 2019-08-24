#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

def get_symbol_by_positiion(pos):
    init_value = ord('a')
    return chr(init_value + pos - 1)


if __name__ == '__main__':
    symbol_pos = int(input("Введите номер буквы в алфавите: "))
    if 1 > symbol_pos or symbol_pos > 26:
        raise ValueError("В анлгийском алфавите 26 букв, введите число от 1 до 26")
    print(f"Под номером {symbol_pos} символ {get_symbol_by_positiion(symbol_pos)}")
