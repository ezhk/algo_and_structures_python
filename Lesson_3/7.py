"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""


def search_two_min(arr):
    absolute_min = second_min = None
    for el in arr:
        if absolute_min is None:
            absolute_min = el
            continue

        if second_min is None:
            # добавляем с учетом сортировки значения:
            # absolute_min - самый минимальный, second_min - максимальный из минимальных
            (absolute_min, second_min) = (el, absolute_min) if el < absolute_min else (absolute_min, el)
            continue

        if absolute_min > el:
            absolute_min, second_min = el, absolute_min
            continue
        if second_min > el:
            second_min = el

    return absolute_min, second_min


if __name__ == "__main__":
    init_array = input("Введите начальный массив целых чисел, как список элементов через запятую: ").split(',')
    init_array = list(map(int, init_array))

    print(f"Два наименших значения {init_array}: {search_two_min(init_array)}")
