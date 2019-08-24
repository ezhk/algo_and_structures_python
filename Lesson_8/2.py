"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""

import hashlib


def get_substrings(input_string):
    uniq_substrings = {}

    len_str = len(input_string)
    window_size = len_str - 1

    while window_size > 0:
        for idx in range(0, len_str - window_size + 1):
            encode_string = input_string[idx:idx + window_size].encode('utf-8')
            hash_substring = hashlib.sha1(encode_string).hexdigest()

            # проверяем, что ключа ещё нет
            if hash_substring in uniq_substrings:
                continue
            uniq_substrings[hash_substring] = encode_string.decode('utf-8')
        window_size -= 1

    return uniq_substrings


if __name__ == "__main__":
    init_string = input("Введите исходную строку: ")
    string_hashes = get_substrings(init_string)

    print(f"Количество подстрок = {len(string_hashes)}")
    print("\tхеши и их строки:")
    print("\n".join((f"{k} = {v}" for k, v in string_hashes.items())))

    """
    Введите исходную строку: qazq
    Количество подстрок = 8
            хеши и их строки:
    7c286a779653e0c1d9cbc2b9c772fbea7033e452 = qaz
    87f2b544a9eb902ae78b9e05d5e2fe4f1094076f = azq
    d3c583412a36313ab5e24293924c39a36b842c56 = qa
    90283840d90de49b8e7984bd99b47fee0d4bd50d = az
    56164622c104ef8e076c1707304ed92a62f7013c = zq
    22ea1c649c82946aa6e479e1ffd321e4a318b1b0 = q
    86f7e437faa5a7fce15d1ddcb9eaeaea377667b8 = a
    395df8f7c51f007019cb30201c49e884b46b92fa = z
    """
