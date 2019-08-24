"""
3.В массиве случайных целых чисел поменять местами минимальный
и максимальный элементы.
"""


def search_idx_min_max(array):
    min_idx = max_idx = 0
    min_value = max_value = float(array[0])

    for idx, el in enumerate(array):
        el = float(el)
        if el > max_value:
            max_value = el
            max_idx = idx
            continue
        if el < min_value:
            min_value = el
            min_idx = idx

    return min_idx, max_idx


def replace_min_max(array):
    min_idx, max_idx = search_idx_min_max(array)
    print(min_idx, max_idx)
    array[min_idx], array[max_idx] = array[max_idx], array[min_idx]
    return array


if __name__ == "__main__":
    init_array = input("Введите начальный массив, как список элементов через запятую: ").split(',')
    print(f"Массив, в котором изменены местами max и min элементы: {replace_min_max(init_array)}")
