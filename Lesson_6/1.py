"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""

from pympler import asizeof
from memory_profiler import profile, memory_usage

import math


@profile
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


@profile
def wrapper_calculate_odd_even_numbers_recursion(number):
    return calculate_odd_even_numbers_recursion(number)


@profile
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


@profile
def slow_prime_search_generator(n):
    primes = i = 0
    while primes < n:
        i += 1
        if i < 2:
            continue
        is_prime = True
        for j in range(2, int(math.sqrt(i) + 1)):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes += 1
            yield i


@profile
def search_eratosthenes_performance(n):
    primes = []

    max_value = n
    init_arr = [1] * max_value
    init_arr[0], init_arr[1] = 0, 0

    shift = 0
    while len(primes) < n:
        for i in range(2, int(math.sqrt(max_value) + 1)):
            start_shift = max(2, shift // i)
            for j in range(start_shift, math.ceil(len(init_arr) / i)):
                init_arr[j * i] = 0

        for idx in range(max(0, shift), len(init_arr)):
            if len(primes) >= n:
                break
            if init_arr[idx] == 1:
                primes.append(idx)

        # extend array
        shift = max_value
        max_value = int(max_value * 1.4)
        init_arr += [1] * (max_value - shift)

    print(f"Итоговый размер временного массива: {asizeof.asizeof(init_arr)}")

    return primes


if __name__ == "__main__":
    print(f"Стартовый размер используемой памяти: {memory_usage()}")

    print("Подсчет четных и нечетных цифр натурального числа")
    calculate_odd_even_numbers(1234567890 ** 50)
    print(f"Размер используемой памяти после calculate_odd_even_numbers: {memory_usage()}")

    print("Подсчет четных и нечетных цифр натурального числа с использованием рекурсии")
    wrapper_calculate_odd_even_numbers_recursion(1234567890 ** 50)
    print(f"Размер используемой памяти после wrapper_calculate_odd_even_numbers_recursion: {memory_usage()}")

    print("Простой поиск простых чисел")
    slow_prime_search(5000)
    print(f"Размер используемой памяти после slow_prime_search: {memory_usage()}")

    # здесь результат профилирования не увидим
    print("Простой поиск простых чисел с использованием геренатора")
    list(slow_prime_search_generator(5000))
    print(f"Размер используемой памяти после slow_prime_search_generator: {memory_usage()}")

    for _ in slow_prime_search_generator(5000):
        pass
    print(f"Размер используемой памяти после slow_prime_search_generator с использованием цикла: {memory_usage()}")

    print("Оптимизированный алгоритм поиска простых чисел с помощью решета Эратосфена")
    search_eratosthenes_performance(5000)
    print(f"Размер используемой памяти после search_eratosthenes_performance: {memory_usage()}")

'''
Подсчет четных и нечетных цифр натурального числа
Filename: ./Lesson_6/1.py

Line #    Mem usage    Increment   Line Contents
================================================
    17     11.2 MiB     11.2 MiB   @profile
    18                             def calculate_odd_even_numbers(number):
    19                                 """
    20                                 Вычисляем количество четных и нечетных символов.
    21                                 Итерации по цифрам с конца с помощью деления на 10 и остатка от деления на 10:
    22                                   123 => 3 -> 2 -> 1.
    23                                 """
    24     11.2 MiB      0.0 MiB       odd, even = 0, 0
    25                             
    26     11.2 MiB      0.0 MiB       iteration = 0
    27     11.2 MiB      0.0 MiB       while True:
    28     11.2 MiB      0.0 MiB           current_number = number // (10 ** iteration)
    29     11.2 MiB      0.0 MiB           if current_number == 0:
    30     11.2 MiB      0.0 MiB               break
    31                             
    32                                     # берем последний символ текущего числа
    33     11.2 MiB      0.0 MiB           current_number %= 10
    34     11.2 MiB      0.0 MiB           if current_number % 2 == 0:
    35     11.2 MiB      0.0 MiB               even += 1
    36                                     else:
    37     11.2 MiB      0.0 MiB               odd += 1
    38     11.2 MiB      0.0 MiB           iteration += 1
    39     11.2 MiB      0.0 MiB       return (odd, even)


Подсчет четных и нечетных цифр натурального числа с использованием рекурсии
Filename: ./Lesson_6/1.py

Line #    Mem usage    Increment   Line Contents
================================================
    68     11.2 MiB     11.2 MiB   @profile
    69                             def wrapper_calculate_odd_even_numbers_recursion(number):
    70     11.8 MiB      0.5 MiB       return calculate_odd_even_numbers_recursion(number)

============================================================================================================
============================================================================================================

Простой поиск простых чисел
Filename: ./Lesson_6/1.py

Line #    Mem usage    Increment   Line Contents
================================================
    17     11.3 MiB     11.3 MiB   @profile
    18                             def slow_prime_search(n):
    19     11.3 MiB      0.0 MiB       primes = []
    20                             
    21     11.3 MiB      0.0 MiB       i = 0
    22     11.5 MiB      0.0 MiB       while len(primes) < n:
    23     11.5 MiB      0.0 MiB           i += 1
    24     11.5 MiB      0.0 MiB           if i < 2:
    25     11.3 MiB      0.0 MiB               continue
    26     11.5 MiB      0.0 MiB           is_prime = True
    27     11.5 MiB      0.0 MiB           for j in range(2, int(math.sqrt(i) + 1)):
    28     11.5 MiB      0.0 MiB               if i % j == 0:
    29     11.5 MiB      0.0 MiB                   is_prime = False
    30     11.5 MiB      0.0 MiB                   break
    31     11.5 MiB      0.0 MiB           if is_prime:
    32     11.5 MiB      0.0 MiB               primes.append(i)
    33                             
    34     11.5 MiB      0.0 MiB       return primes


Оптимизированный алгоритм поиска простых чисел с помощью решета Эратосфена
Итоговый размер временного массива: 664256 байт.
Filename: ./Lesson_6/1.py

Line #    Mem usage    Increment   Line Contents
================================================
    37     11.5 MiB     11.5 MiB   @profile
    38                             def search_eratosthenes_performance(n):
    39     11.5 MiB      0.0 MiB       primes = []
    40                             
    41     11.5 MiB      0.0 MiB       max_value = n
    42     11.5 MiB      0.0 MiB       init_arr = [1] * max_value
    43     11.5 MiB      0.0 MiB       init_arr[0], init_arr[1] = 0, 0
    44                             
    45     11.5 MiB      0.0 MiB       shift = 0
    46     12.8 MiB      0.0 MiB       while len(primes) < n:
    47     12.0 MiB      0.0 MiB           for i in range(2, int(math.sqrt(max_value) + 1)):
    48     12.0 MiB      0.0 MiB               start_shift = max(2, shift // i)
    49     12.0 MiB      0.0 MiB               for j in range(start_shift, math.ceil(len(init_arr) / i)):
    50     12.0 MiB      0.0 MiB                   init_arr[j * i] = 0
    51                             
    52     12.0 MiB      0.0 MiB           for idx in range(max(0, shift), len(init_arr)):
    53     12.0 MiB      0.0 MiB               if len(primes) >= n:
    54     12.0 MiB      0.0 MiB                   break
    55     12.0 MiB      0.0 MiB               if init_arr[idx] == 1:
    56     12.0 MiB      0.0 MiB                   primes.append(idx)
    57                             
    58                                     # extend array
    59     12.0 MiB      0.0 MiB           shift = max_value
    60     12.0 MiB      0.0 MiB           max_value = int(max_value * 1.4)
    61     12.8 MiB      0.8 MiB           init_arr += [1] * (max_value - shift)
    62                             
    63     12.8 MiB      0.0 MiB       print(f"Итоговый размер временного массива: {asizeof.asizeof(init_arr)}")
    64                             
    65     12.8 MiB      0.0 MiB       return primes

============================================================================================================
============================================================================================================

В реализации подсчета чисел с рекурсией видно как увеличился размер используемой
памяти на 0.5 MiB — необходимость хранить стек.

Из вывода поиска простых чисел, что реализация простым перебором проще по памяти,
в том числе за счет того, что нет необходимости инициализировать
исходный массив — который заполнен единицами, его размер 664256 байт.


Что интересно — мы не можем произвести замер используемой памяти генератором,
но попробуем это посмотреть с помощью memory_usage.

    Стартовый размер используемой памяти: [11.04296875]
    Размер используемой памяти после calculate_odd_even_numbers: [11.296875]
    Размер используемой памяти после wrapper_calculate_odd_even_numbers_recursion: [11.81640625]
      Здесь видно подтверждение того, что рекурсия заняла порядка 0.5Мб,
      когда простой перебор 0.25Мб.
    
    Размер используемой памяти после slow_prime_search: [11.85546875]
    Размер используемой памяти после slow_prime_search_generator: [11.88671875]
      Здесь мы можем оценить использование генератора (на самом деле не можем):
      - без генератора slow_prime_search: 11.85546875 - 11.81640625 = 0.0390625
      - с использованием генератора: 11.88671875 - 11.85546875 = 0.03125

      Используем генератор, почему нет разницы — потому что мы в основном теле
      программы всё-равно делаем список из генератора (чтобы его перебрать):
        list(slow_prime_search_generator(5000))
      Попробуем через цикл for _ in slow_prime_search_generator(5000): pass:
        Размер используемой памяти после slow_prime_search: [11.87890625]
        Размер используемой памяти после slow_prime_search_generator: [11.90625]
        Размер используемой памяти после slow_prime_search_generator с использованием цикла: [11.90625]
        И теперь мы видим,. что:
        - с использованием генератора и формированием списка: 11.90625 - 11.87890625 = 0.02734375
        - с использованием генератора и пустого цикла: 11.90625 - 11.90625 = 0
        
    Размер используемой памяти после search_eratosthenes_performance: [13.26953125]
      Ещё одно подтверждение, что временный массив в алгоритме поиска простых чисел
      с помощью решета Эратосфена приводит к увеличению используемой памяти — ~1.5Мб.
'''
