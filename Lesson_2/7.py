"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""


def summary(n):
    if n < 1:
        return 0
    return n + summary(n-1)


if __name__ == "__main__":
    n = int(input("Введите число элементов: "))
    print(f"1+2+...+n = n(n+1)/2; так как {summary(n)} = {n * (n + 1) / 2}")
