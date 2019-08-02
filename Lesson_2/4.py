"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


def get_sum(count):
    summary_value = 0

    last_value = 1
    for _ in range(count):
        print(last_value)
        summary_value += last_value
        last_value /= -2
    return summary_value


if __name__ == "__main__":
    counter = int(input("Введите число элементов: "))
    print(f"Сумма элементов {get_sum(counter)}")
