"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

from collections import Counter, deque
import bisect


def build_huffman_tree(input_string):
    """
    Как строим дерево:
    - берем строку и вычисляем количество повторений элементов с помощью Count
    - по полученному списку кортежей итеририруемся до тех пор, пока не останется один кортеж с общим весом всех символов
    - в цикле берем два последних кортежа (они уже остортированы) и вычисляем их суммарный вес и новый кортеж,
        состоящий из элементов предыдущих символов или кортежей
    - полученный кортеж добавляем в соответствии с его весом и порядком сортировки
    - на выхоже получаем кортеж, где левый элемент — вес всех правых элементов,
        а правый — символ или тоже вложенный кортеж

    То есть из списка
        [('e', 4), ('b', 3), ('p', 2), (' ', 2), ('o', 2), ('r', 1), ('!', 1)]
    должны получить нечто похожее на
            (
                (((('b', 3),
                ('e', 4)
            ), 7),
                (
                    (((('o', 2),
                    (' ', 2)
                ), 4),
                (
                    (('p', 2),
                    (
                        (('!', 1),
                        ('r', 1)
                    ), 2)
                ), 4)
            ), 8)
        ), 15)
    """

    freq_counter = Counter(input_string).most_common()
    queue = list(freq_counter)

    while len(queue) > 1:
        first, second = queue.pop(), queue.pop()
        weight = first[1] + second[1]
        new_node = ((first, second), weight)

        insert_idx = 0
        for idx in range(len(queue) - 1, -1, -1):
            if weight >= queue[idx][1]:
                insert_idx = idx
                continue
            break
        queue.insert(insert_idx, new_node)

    return queue.pop()


def convert_tree_to_dict(tree, code=''):
    huffman_dict = {}
    node, weight = tree
    if not isinstance(node, tuple):
        return {node: code}

    huffman_dict.update(convert_tree_to_dict(node[0], f"{code}0"))
    huffman_dict.update(convert_tree_to_dict(node[1], f"{code}1"))

    return huffman_dict


if __name__ == "__main__":
    input_string = input("Введите строку: ")
    tree = build_huffman_tree(input_string)
    huffman_dict = convert_tree_to_dict(tree)

    values = (huffman_dict[x] for x in input_string)
    print(" ".join(values))

    print(f"Словарь: {huffman_dict}")

    """
    Введите строку: beep boop beer!
    00 01 01 110 101 00 100 100 110 101 00 01 01 1111 1110
    Словарь: {'b': '00', 'e': '01', 'o': '100', ' ': '101', 'p': '110', '!': '1110', 'r': '1111'}

    Не обязательно, что словарь будет одинаковым для разных решений, всё зависит
    от изначальной сортировки freq_counter = Counter(input_string).most_common(),
    символы с одной частотностью могут оказаться в разных позициях.

    Также, насколько понимаю, в кодировке не определено куда вставлять поддерево
    с существующим весом, если такие же веса уже есть с другими символами или поддеревьями —
    до или после текущего символа.
    """
