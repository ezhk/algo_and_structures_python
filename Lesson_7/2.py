"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

import random
import timeit


def merge_sort(arr):
    """
    Неотптимальная реализация сортировкой слиянием.
    Данный алгоритм уже был написан на 3 уроке.
    """
    if len(arr) == 1:
        return [arr[0]]

    result_arr = []
    sorted_arr_one = merge_sort(arr[:len(arr) // 2])
    sorted_arr_two = merge_sort(arr[len(arr) // 2:])

    while sorted_arr_one and sorted_arr_two:
        if sorted_arr_one[0] > sorted_arr_two[0]:
            result_arr.append(sorted_arr_two.pop(0))
            continue
        result_arr.append(sorted_arr_one.pop(0))

    result_arr.extend(sorted_arr_one)
    result_arr.extend(sorted_arr_two)

    return result_arr


if __name__ == "__main__":
    len_arr = int(input("Введите длину списка: "))
    init_array = [round(random.uniform(0, 50), 2) for _ in range(len_arr)]

    print(f"Исходный массив: {init_array}")
    print(f"Результат сортировки слиянием: {merge_sort(init_array)}")
