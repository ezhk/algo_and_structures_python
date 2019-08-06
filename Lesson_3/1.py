"""
1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""


def get_init_range():
    i = 2
    while i <= 9:
        yield i
        i += 1


def get_numbers(number):
    return 99 // number


if __name__ == "__main__":
    for i in get_init_range():
        print(f"Для числа {i} кратных чисел в диапазоне [2, 99]: {get_numbers(i)}")
