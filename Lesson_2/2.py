"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""


def calculate_odd_even_numbers(number):
    """
    Вычисляем количество четных и нечетных символов.
    Итерации по цифрам с конца с помощью деления на 10 и остатка от деления на 10:
      123 => 3 -> 2 -> 1.
    """
    odd, even = 0, 0

    iteration = 0
    while True:
        current_number = number // (10 ** iteration)
        if current_number == 0:
            break

        # берем последний символ текущего числа
        current_number %= 10
        if current_number % 2 == 0:
            even += 1
        else:
            odd += 1
        iteration += 1
    return (odd, even)


def calculate_odd_even_numbers_recursion(number):
    """
    Логика аналогичная той, что в calculate_odd_even_numbers,
    за тем лишь исключением что в текущем теле функции берем
    последний символ, а оставшуюся часть числа передаем рекурсивно:
    123 =>
      3, передаем в рекурсивный вызов 12 =>
      2, передаем в рекурсивный вызов 1 =>
      1, передаем в рекурсивный вызов 0 =>
      0 — условие выхода из рекусии
    """
    if number == 0:
        return (0, 0)

    # send number without last symbol to recursion call: 123 -> 12
    (odd, even) = calculate_odd_even_numbers_recursion(number // 10)

    # processing current symbol: 123 -> 3
    current_number = number % 10
    if current_number % 2 == 0:
        even += 1
    else:
        odd += 1
    return (odd, even)


if __name__ == "__main__":
    number = abs(int(input("Input natural number: ")))
    (odd, even) = calculate_odd_even_numbers(number)
    print(f"{number} = odd: {odd}, even: {even}")

    number = abs(int(input("Input natural number: ")))
    (odd, even) = calculate_odd_even_numbers_recursion(number)
    print(f"{number} = odd: {odd}, even: {even}")
