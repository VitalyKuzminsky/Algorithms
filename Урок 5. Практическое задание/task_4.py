"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""


from timeit import timeit
from collections import OrderedDict

my_dict = {}
my_ordereddict = OrderedDict()
number_iterations = 10 ** 3


def add_dict(dict_in, number):
    for el in range(number):
        dict_in[el] = el


def add_ordered_dict(ordereddict_in, number):
    for el in range(number):
        ordereddict_in[el] = el


def time_check(*args):
    times = {}
    for func in args:
        times[func] = timeit(f'{func}', globals=globals(), number=number_iterations)
    for key, value in times.items():
        print(f'Время выполнения функции {key}: {value}')


list_func = [
    'add_dict(my_dict, number_iterations)',
    'add_ordered_dict(my_ordereddict, number_iterations)'
]
for el in list_func:
    time_check(el)


"""
Время выполнения функции add_dict(my_dict, number_iterations): 0.07382839999627322
Время выполнения функции add_ordered_dict(my_ordereddict, number_iterations): 0.10072369989939034
Обычный словарь заполняется быстрее, чем упорядоченный словарь OrderedDict 
"""
