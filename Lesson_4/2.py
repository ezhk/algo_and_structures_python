"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""

import math
import timeit


def slow_prime_search(n):
    primes = []

    i = 0
    while len(primes) < n:
        i += 1
        if i < 2:
            continue
        is_prime = True
        for j in range(2, int(math.sqrt(i) + 1)):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    return primes


def search_eratosthenes(n, max_value=None):
    if max_value is None:
        max_value = n
    init_arr = [1] * max_value
    init_arr[0], init_arr[1] = 0, 0

    for i in range(2, int(math.sqrt(max_value) + 1)):
        for j in range(2, len(init_arr) // i):
            init_arr[j * i] = 0

    primes = []
    for idx, el in enumerate(init_arr):
        if len(primes) >= n:
            break
        if el == 1:
            primes.append(idx)

    if len(primes) < n:
        return search_eratosthenes(n, int(max_value * 1.5))

    return primes


if __name__ == "__main__":
    print("Реализация собственного алгоритма поиска простого по счету числа: ", end='')
    print(timeit.timeit("slow_prime_search(20000)", setup="from __main__ import slow_prime_search", number=10))
    print("Для 100 простых чисел результат: ", slow_prime_search(100))

    print("\nРеализация поиска простого с помощью решета Эратосфена по счету числа;\n"
          "\tс постоянным увеличением размера инициализированного списка,\n"
          "\tпоскольку решето Эратосфена предполагает работу в конечном диапазоне:\n\t", end='')
    print(timeit.timeit("search_eratosthenes(20000)", setup="from __main__ import search_eratosthenes", number=10))
    print("Для 100 простых чисел результат: ", search_eratosthenes(100))

    print("\nЧем больше диапазон, тем эффективнее второй алгоритм,\n"
          "но уверен, что можно более точно угадывать конечную границу диапазона.")
