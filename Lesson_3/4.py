"""
4. Определить, какое число в массиве встречается чаще всего.
"""


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
    print(f"Сортировка слиянием: {sorted_arr}")

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


if __name__ == "__main__":
    init_array = input("Введите начальный массив целых чисел, как список элементов через запятую: ").split(',')
    init_array = list(map(int, init_array))

    print(f"Наиболее часто встречающийся элемент: {search_most_frequently_el(init_array)}")
