"""
Задание 1.

Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.

Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""


from random import randint
from timeit import timeit


def bubble_sort_reverse(list_in):
    for i in range(len(list_in)):
        for j in range(len(list_in) - 1):
            if list_in[j] < list_in[j + 1]:
                list_in[j], list_in[j + 1] = list_in[j + 1], list_in[j]
    return list_in


def bubble_sort_upgrade(list_in):
    flag = True
    while flag:
        flag = False
        for i in range(len(list_in) - 1):
            if list_in[i] < list_in[i + 1]:
                list_in[i], list_in[i + 1] = list_in[i + 1], list_in[i]
                flag = True
    return list_in


my_list = [randint(-100, 100) for i in range(100)]
print(my_list)
print(bubble_sort_reverse(my_list[:]))
print(bubble_sort_upgrade(my_list[:]))


def time_check(*args):
    times = {}
    for func in args:
        times[func] = timeit(f'{func}', globals=globals(), number=100)
    for key, value in times.items():
        print(f'Время выполнения функции {key}: {value}')


list_func = [
    'bubble_sort_reverse(my_list[:])',
    'bubble_sort_upgrade(my_list[:])'
]
for el in list_func:
    time_check(el)

"""
Время выполнения функции bubble_sort_reverse(my_list[:]): 0.1644845000701025
Время выполнения функции bubble_sort_upgrade(my_list[:]): 0.1480413000099361

Время доработанного чуть лучше исходного варианта
"""
