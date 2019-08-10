"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

import timeit


def merge_sort(arr):
    """
    Неотптимальная реализация сортировкой слиянием.
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


def search_most_frequently_el(arr):
    sorted_arr = merge_sort(init_array)
    # print(f"Сортировка слиянием: {sorted_arr}")

    counter = max_counter = 1
    last_value = max_value = sorted_arr[0]

    # Чтобы не делать доп. условие после цикла
    sorted_arr.append('EOF')

    for idx in range(1, len(sorted_arr)):
        if last_value == sorted_arr[idx]:
            counter += 1
            continue

        if max_counter < counter:
            max_counter = counter
            max_value = last_value

        counter = 1
        last_value = sorted_arr[idx]

    return max_value


def search_most_frequently_el_sorted(arr):
    sorted_arr = sorted(init_array)
    # print(f"Сортировка слиянием: {sorted_arr}")

    counter = max_counter = 1
    last_value = max_value = sorted_arr[0]

    # Чтобы не делать доп. условие после цикла
    sorted_arr.append('EOF')

    for idx in range(1, len(sorted_arr)):
        if last_value == sorted_arr[idx]:
            counter += 1
            continue

        if max_counter < counter:
            max_counter = counter
            max_value = last_value

        counter = 1
        last_value = sorted_arr[idx]

    return max_value


def search_max_only(arr):
    return max(arr, key=arr.count)


if __name__ == "__main__":
    init_array = [54, 2, -20, 33, 679, 2, 212, 345, 20, 74, -69, 0]

    print(search_most_frequently_el(init_array))
    print(search_most_frequently_el_sorted(init_array))
    print(search_max_only(init_array))

    print("Оценка алгоритмов сортировки: ")
    print("\tНеоптимальная собственная реалзация алгоритма сортировки слиянием: ", end='')
    print(timeit.timeit("search_most_frequently_el(init_array)",
                        setup="from __main__ import init_array, merge_sort, search_most_frequently_el",
                        number=100000))

    print("\tиспользование встроенной функции sort: ", end='')
    print(timeit.timeit("search_most_frequently_el_sorted(init_array)",
                        setup="from __main__ import init_array, search_most_frequently_el_sorted",
                        number=100000))

    print("\t\tНесмотря на примерно схожую сложность функций сортировки (N * logN)\n"
          "\t\tв моей реализации очень медленные операции расширения массива и взятия\n"
          "\t\tпервого элемента через pop. Также в python используется timsort.")

    print("\tиспользование встроенной функции max вместо search_most_frequently_el: ", end="")
    print(timeit.timeit("search_max_only(init_array)",
                        setup="from __main__ import init_array, search_max_only",
                        number=100000))

    print("Наиболее быстрым оказался вариант c search_most_frequently_el_sorted,\n"
          "где используется встроенный алгоритм сортировки, но собственный подсчёт частотности.")
