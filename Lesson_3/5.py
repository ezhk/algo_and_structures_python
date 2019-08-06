"""
5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.
"""


def search_max_negative(arr):
    max_negative_value = max_negative_idx = None

    for (idx, el) in enumerate(arr):
        if el > 0:
            continue

        if max_negative_value is None or max_negative_value < el:
            max_negative_value = el
            max_negative_idx = idx

    return max_negative_value, max_negative_idx


if __name__ == "__main__":
    init_array = input("Введите начальный массив целых чисел, как список элементов через запятую: ").split(',')
    init_array = list(map(int, init_array))

    max_negative_value, max_negative_idx = search_max_negative(init_array)
    if max_negative_value is None:
        print(f"Максимальный отрицательный элемент не найден")
        quit()
    print(f"Максимальный отрицательный элемент {max_negative_value} и его индекс (с нуля): {max_negative_idx}")
