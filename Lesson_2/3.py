"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""


def reverse(number):
    """
    Уменьшаем на порядок число с каждой итерацией,
    остаток от деления на 10 записываем в конец результата.
    """
    result = ''
    while number != 0:
        result = result + str(number % 10)
        number //= 10
    return result


def reverse_recurion(number):
    """
    Как reverse, только с рекурсией, просто вместо уменьшения
    на каждой итерации — мы передаем в рекурсивный вызов уменьшенное
    значение.
    """
    if number == 0:
        return ''
    result = str(number % 10) + reverse_recurion(number // 10)
    return result


if __name__ == '__main__':
    number = int(input("Введите целое число: "))
    print(f"Число наоборот {reverse(number)}")
    print(f"Число наоборот с рекурсией: {reverse_recurion(number)}")
