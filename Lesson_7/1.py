"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import random


def bubble_sort(arr):
    if len(arr) < 2:
        return arr

    len_arr = len(arr)
    shift = 0
    cycle_counter = 0

    while shift < len_arr:
        # is_shifted is optimization: check, that element has been moved;
        # if it's false, than array already sorted
        is_shifted = False

        for idx in range(1, len_arr - shift):
            cycle_counter += 1
            if arr[idx] < arr[idx - 1]:
                arr[idx], arr[idx - 1] = arr[idx - 1], arr[idx]
                is_shifted = True

        if not is_shifted:
            break
        shift += 1

    print(f"Массив осортирован за {cycle_counter} циклов")
    return arr


if __name__ == "__main__":
    len_arr = int(input("Введите длину списка: "))
    init_array = [round(random.uniform(-100, 100), 2) for _ in range(len_arr)]
    print(f"Исходный массив: {init_array}")
    print(f"Результат сортировки пузырьком: {bubble_sort(init_array)}")

    """
    Введите длину списка: 10
    Исходный массив: [28.67, -14.3, -94.06, 82.07, -13.75, -35.11, -78.25, 36.36, -95.73, -70.35]
    Массив осортирован за 45 циклов
    Результат сортировки пузырьком: [-95.73, -94.06, -78.25, -70.35, -35.11, -14.3, -13.75, 28.67, 36.36, 82.07]
    """
