"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""


def find_repeats(number, symbol):
    if number == 0:
        return 0

    count = find_repeats(number // 10, symbol)
    if number % 10 == symbol:
        count += 1
    return count


if __name__ == "__main__":
    numbers = input("Введите числа через запятую: ")
    symbol = int(input("Введите цифру от 0 до 9, которую надо посчитать: "))

    count = 0
    for number in numbers.split(','):
        number = int(number)
        repeats = find_repeats(number, symbol)
        count += repeats
        print(f"В числе {number} количество цифр {symbol} = {repeats}")

    print(f"Всего цифра {symbol} встречается {count} раз")
