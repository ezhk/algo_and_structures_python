"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


def print_symbols(pairs_per_line=10):
    results_in_line = 0
    for i in range(32, 127 + 1):
        print(f"{i}. {chr(i)}\t", end='')
        results_in_line += 1

        if results_in_line == pairs_per_line:
            print()
            results_in_line = 0
    print()
    return True


if __name__ == '__main__':
    print_symbols()
