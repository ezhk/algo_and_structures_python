"""
2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
надо заполнить значениями 1, 4, 5, 6
(или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""


def custom_enumerate(arr):
    for idx in range(len(arr)):
        yield (idx, arr[idx])


def get_indexes_of_odd(array):
    result_array = []
    for idx, el in custom_enumerate(array):
        if float(el) % 2 == 0:
            result_array.append(idx + 1)
    return result_array


if __name__ == '__main__':
    init_array = input("Введите начальный массив, как список элементов через запятую: ").split(',')
    print(f"Позиция четных элементов массива {init_array}: {get_indexes_of_odd(init_array)}")
