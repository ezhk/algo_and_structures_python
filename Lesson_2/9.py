"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""


def get_sum(number):
    sum = 0
    while number != 0:
        sum += number % 10
        number //= 10
    return sum


if __name__ == "__main__":
    numbers = input("Введите числа через запятую: ")
    max_value = 0
    max_number = 0

    for number in numbers.split(','):
        number = int(number)
        current_value = get_sum(number)
        if max_value < current_value:
            max_value = current_value
            max_number = number
            continue

        if max_value == current_value:
            max_number = f"{max_number}, {number}"

    print(f"Максимальная сумма чисел = {max_value} у числа/чисел {max_number}")
