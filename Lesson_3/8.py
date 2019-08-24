"""
8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

import random


def init_matrix(rows, columns, start_int, stop_int):
    matrix = []
    for i in range(rows):
        row_arr = []
        for j in range(columns):
            row_arr.append(random.randint(start_int, stop_int))
        matrix.append(row_arr)
    return matrix


def input_matrix(rows, columns):
    arr = []
    for row in range(rows):
        row_input = input(f"Введите {columns} чисел черех запятую для строки {row + 1}: ")
        values = row_input.split(',', columns)[:columns]
        arr.append(list(map(int, values)))
    return arr


def get_sum(arr):
    """
    Вычисление суммы элементов списка
    """
    sum = 0
    for el in arr:
        sum += el
    return sum


def calc_rows_sum(arr):
    """
    Вычисляет сумму элементов для каждой строки и
    добавляет результат последним значением
    """
    for row in range(len(arr)):
        sum = get_sum(arr[row])
        arr[row].append(sum)
    return arr


def print_matrix(arr):
    for row in range(len(arr)):
        row_data = arr[row]
        for column in range(len(row_data)):
            print(f"{arr[row][column]:7d}", end='')
        print()


if __name__ == "__main__":
    rows = int(input("Введите количество строк матрицы: "))
    columns = int(input("Введите количество стоблцов матрицы: "))

    generate = input("Хотите ли вы сгенерировать матрицу автоматически (y/n)? ")
    if generate == 'y':
        matrix = init_matrix(rows, columns - 1, -100, 100)
        print("Сгенерированная матрица: ")
    else:
        matrix = input_matrix(rows, columns - 1)
        print("Введенная матрица")
    print_matrix(matrix)

    print("Расчитанная матрица: ")
    matrix = calc_rows_sum(matrix)
    print_matrix(matrix)
