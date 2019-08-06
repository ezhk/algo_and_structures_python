"""
6. В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""


def search_min_max_idx(arr):
    min_idx = max_idx = 0
    if not arr:
        return min_idx, max_idx

    min_value = max_value = arr[0]
    for (idx, el) in enumerate(arr):
        if el > max_value:
            max_value = el
            max_idx = idx
            continue
        if el < min_value:
            min_value = el
            min_idx = idx

    print(f"Минимальное значение и индекс: {min_value}, {min_idx}")
    print(f"Максимальное значение и индекс: {max_value}, {max_idx}")
    return min_idx, max_idx


def calc_sum(arr, start_idx, stop_idx):
    sum = 0
    while start_idx <= stop_idx:
        sum += arr[start_idx]
        start_idx += 1
    return sum


if __name__ == "__main__":
    init_array = input("Введите начальный массив целых чисел, как список элементов через запятую: ").split(',')
    init_array = list(map(int, init_array))

    min_idx, max_idx = search_min_max_idx(init_array)
    (from_idx, to_idx) = (min_idx, max_idx) if min_idx < max_idx else (max_idx, min_idx)

    print(f"Сумма элементов между min и max значениями: {calc_sum(init_array, from_idx + 1, to_idx - 1)}")
