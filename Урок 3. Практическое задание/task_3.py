"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв

Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.

Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""


import hashlib
from random import choice


def str_s_len_n(len_str: int) -> str:
    """
    Создаёт строку заданной длины, состоящую только из строчных латинских букв.
    :param len_str: int - длина строки
    :return: str
    """
    my_list = []
    while len(my_list) < len_str:
        number_el = choice(range(97, 123))
        my_list.append(chr(number_el))
    return ''.join(my_list)


def unique_hash_set(str_in: str) -> set:
    """
    Из строки символов создает уникальные подстроки из этих символов.
    Преобразует полученный результат в хеш-функцию и возвращает множество из них.
    :param str_in: str - строка символов.
    :return: set
    """
    my_set = set()
    for i in range(len(str_in)):
        for j in range(i + 1, len(str_in) + 1):
            if str_in[i:j] != str_in:
                my_set.add(hashlib.sha256(str_in[i:j].encode()).hexdigest())
                print(str_in[i:j])
    return my_set


uhs = unique_hash_set(str_s_len_n(3))
print(uhs)
print(len(uhs))
