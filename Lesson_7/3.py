"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""

import random


def coctail_sort(arr):
    start_shift = 0
    end_shift = len(arr) - 1

    while start_shift <= end_shift:
        is_shift = False
        for idx in range(start_shift, end_shift):
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                is_shift = True
        end_shift -= 1
        if not is_shift:
            break

        for idx in range(end_shift, start_shift, -1):
            if arr[idx] < arr[idx - 1]:
                arr[idx], arr[idx - 1] = arr[idx - 1], arr[idx]
        start_shift += 1
        if not is_shift:
            break

    return arr


if __name__ == "__main__":
    m = int(input("Введите множитель m: "))
    init_array = [round(random.uniform(0, 50), 2) for _ in range(2 * m + 1)]

    print(f"Исходный массив: {init_array}")
    sorted_init_array = coctail_sort(init_array)
    print(f"Результат шейкерной сортировки: {coctail_sort(sorted_init_array)}")
    print(f"Мадиана массива: {sorted_init_array[len(sorted_init_array) // 2]}")
