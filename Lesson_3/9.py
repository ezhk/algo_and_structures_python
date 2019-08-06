"""
 9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.
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


def print_matrix(arr):
    for row in range(len(arr)):
        row_data = arr[row]
        for column in range(len(row_data)):
            print(f"{arr[row][column]:7d}", end='')
        print()


def get_min(arr):
    """
    Вычисление суммы элементов списка
    """
    min = None
    for el in arr:
        if min is None or min > el:
            min = el
    return min


def get_max(arr):
    """
    Вычисление суммы элементов списка
    """
    max = None
    for el in arr:
        if max is None or max < el:
            max = el
    return max


def get_max_from_min(arr, rows, columns):
    """
    Финкция итерируется по строкам для каждого столбца,
    составляет временную матрицу из строковых значений,
    находит минимальный элемент и добавляет его в
    список минимальных элементов.
    В конце возвращает max элемент из списка минимальных.
    """
    min_value_columns = []
    for column in range(columns):
        col_arr = []
        for row in range(rows):
            col_arr.append(arr[row][column])
        col_min = get_min(col_arr)
        print(f"Минимальное значение в столбце {col_arr}: {col_min}")

        min_value_columns.append(col_min)
    return get_max(min_value_columns)


if __name__ == "__main__":
    rows = int(input("Введите количество строк матрицы: "))
    columns = int(input("Введите количество стоблцов матрицы: "))

    matrix = init_matrix(rows, columns, -100, 100)
    print("Сгенерированная матрица: ")
    print_matrix(matrix)

print(f"Максимальный элемент среди минимальных элементов столбцов матрицы: {get_max_from_min(matrix, rows, columns)}")
