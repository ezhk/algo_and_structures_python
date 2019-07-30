#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

def get_symbol_positiion(symbol):
    init_value = ord('a')
    return ord(symbol.lower()) - init_value + 1


def get_symbols_range(first_letter, second_letter):
    value = abs(get_symbol_positiion(second_letter) - get_symbol_positiion(first_letter)) - 1
    return 0 if value < 0 else value


if __name__ == '__main__':
    first_symbol = input("Введите первый символ алфавита: ")
    second_symbol = input("Введите второй символ алфавита: ")

    first_pos = get_symbol_positiion(first_symbol)
    second_pos = get_symbol_positiion(second_symbol)
    print(f"Позиция {first_symbol}: {first_pos}")
    print(f"Позиция {second_symbol}: {second_pos}")
    print(f"Букв между {first_symbol} и {second_symbol}: {get_symbols_range(first_symbol, second_symbol)}")
