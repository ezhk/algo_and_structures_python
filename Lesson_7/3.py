"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""

import random
import timeit


def coctail_sort(input_arr):
    arr = list(input_arr)
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


def solution_without_full_sort(input_arr):
    """
    Результатом не будет честная сортировка массива,
    цикл продолжается до тех пор, пока серединный элемент
    смещается, как он не сместился — медиана найдена.
    """

    arr = list(input_arr)
    base_element_idx = len(arr) // 2

    while True:
        middle_value = arr[base_element_idx]
        left, middle, right = [], [], []

        for idx in range(0, len(arr)):
            if arr[idx] > middle_value:
                right.append(arr[idx])
            elif arr[idx] < middle_value:
                left.append(arr[idx])
            else:
                middle.append(arr[idx])

        arr = left + middle + right
        if middle_value == arr[base_element_idx]:
            # тут мы уже можем вывести медиану, но делаем break и возвращаем
            # список, чтобы убедиться, что у нас не произошла полная сортировка.
            break
    return arr


if __name__ == "__main__":
    m = int(input("Введите множитель m: "))
    init_array = [round(random.uniform(-50, 50), 2) for _ in range(2 * m + 1)]
    print(f"Исходный массив: {init_array}")

    coctail_sort_arr = coctail_sort(init_array)
    print(f"Результат после шейкерной сортировки: {coctail_sort_arr}"
          f"\n\tи медиана по нему: {coctail_sort_arr[len(coctail_sort_arr) // 2]}")

    without_full_sort_arr = solution_without_full_sort(init_array)
    print(f"Массив с медианным элементом: {without_full_sort_arr}, "
          f"\n\tи медиана: {without_full_sort_arr[len(without_full_sort_arr) // 2]}")

    """
    Оценим какой вариант быстрее
    """
    print("Время обработки массива коктельной сортировкой: ",
          timeit.timeit("coctail_sort(init_array)",
                        setup="from __main__ import coctail_sort, init_array",
                        number=100))
    print("Время обработки массива при поиске медианы без полной сортирки: ",
          timeit.timeit("solution_without_full_sort(init_array)",
                        setup="from __main__ import solution_without_full_sort, init_array",
                        number=100))

    """
    Введите множитель m: 15
    Исходный массив: [-38.49, -6.76, 47.54, -39.25, 25.09, -48.98, -19.0, -32.31, 5.69, -22.75, 11.13, -9.68, -21.19,
                      -4.89, -40.85, -7.48, 11.03, -21.0, -25.01, 30.31, 24.1, -12.67, 42.9, -33.09, -20.27, -22.03,
                      33.02, -13.31, 8.93, -8.28, -13.28]
    Результат после шейкерной сортировки: [-48.98, -40.85, -39.25, -38.49, -33.09, -32.31, -25.01, -22.75, -22.03,
                                           -21.19, -21.0, -20.27, -19.0, -13.31, -13.28, -12.67, -9.68, -8.28, -7.48,
                                           -6.76, -4.89, 5.69, 8.93, 11.03, 11.13, 24.1, 25.09, 30.31, 33.02, 42.9,
                                           47.54]
        и медиана по нему: -12.67
    Массив с медианным элементом: [-38.49, -39.25, -48.98, -19.0, -32.31, -22.75, -21.19, -40.85, -21.0, -25.01, -33.09,
                                   -20.27, -22.03, -13.31, -13.28, -12.67, -9.68, -8.28, -7.48, -6.76, 47.54, 25.09,
                                   5.69, 11.13, -4.89, 11.03, 30.31, 24.1, 42.9, 33.02, 8.93], 
        и медиана: -12.67
    Время обработки массива коктельной сортировкой:  0.007203760999999975
    Время обработки массива при поиске медианы без полной сортирки:  0.001875449000000029

    За счет solution_without_full_sort мы можем существенно сократить поиск медианы
    (на самом деле любого процентиля, достаточно лишь правильно выбрать base_element_idx),
    ведь нам не нужно постоянно сортировать массив, как в случае с шейкерной сортировкой.
    В текущем тесте удалось сократить результат выполнения в 4 раза.
    """