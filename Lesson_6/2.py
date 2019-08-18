"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""

from pympler import asizeof
from collections import UserList


class HexNumbers:
    def __init__(self, value):
        self.key = value.lower()
        self.presentation = UserList([x for x in value.upper()])

    def __str__(self):
        return f"{self.presentation.data}"

    def __mul__(self, other):
        return HexNumbers(f"{int(self.key, 16) * int(other.key, 16):x}")

    def __add__(self, other):
        return HexNumbers(f"{int(self.key, 16) + int(other.key, 16):x}")


class HexNumbersSlots:
    __slots__ = ('key', 'presentation')

    def __init__(self, value):
        self.key = value.lower()
        self.presentation = UserList([x for x in value.upper()])

    def __str__(self):
        return f"{self.presentation.data}"

    def __mul__(self, other):
        return HexNumbers(f"{int(self.key, 16) * int(other.key, 16):x}")

    def __add__(self, other):
        return HexNumbers(f"{int(self.key, 16) + int(other.key, 16):x}")


if __name__ == "__main__":
    hex_first = HexNumbers('e2e4')
    hex_slots = HexNumbersSlots('e2e4')

    print(f"Представление аттрибутов объектов обычного класса: {hex_first.__dict__}")
    print(f"Слоты оптимизированного класса {hex_slots.__slots__}")

    print(f"Стандартный размер экземпляра класса: {asizeof.asizeof(hex_first)}")
    print(f"Размер экземпляра класса с использованием slots: {asizeof.asizeof(hex_slots)}")

"""
Представление аттрибутов объектов обычного класса: {'key': 'e2e4', 'presentation': ['E', '2', 'E', '4']}
Слоты оптимизированного класса ('key', 'presentation')
Стандартный размер экземпляра класса: 896
Размер экземпляра класса с использованием slots: 656

По выводу видно, что ипользование в классе слотов (__slots__) привело
  к уменьшению размера экземпляра, что и требовалось получить.
"""
