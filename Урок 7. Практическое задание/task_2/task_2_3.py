"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

3) с помощью встроенной функции поиска медианы

сделайте замеры на массивах длиной 10, 100, 1000 элементов

В конце сделайте аналитику какой трех из способов оказался эффективнее
"""


from random import randint
from timeit import timeit


def median(list_in):
    new_list = list_in
    for i in range(len(list_in) // 2):
        new_list.remove(max(new_list))
    return max(new_list)


m = 10
orig_list = [randint(0, 100) for i in range(2 * m + 1)]
print(orig_list)
print(median(orig_list))
print(timeit('median(orig_list[:])', globals=globals(), number=100))

m = 100
orig_list = [randint(0, 100) for i in range(2 * m + 1)]
print(orig_list)
print(median(orig_list))
print(timeit('median(orig_list[:])', globals=globals(), number=100))

m = 1000
orig_list = [randint(0, 100) for i in range(2 * m + 1)]
print(orig_list)
print(median(orig_list))
print(timeit('median(orig_list[:])', globals=globals(), number=100))

"""
0.0006162000354379416   10 элементов
0.009178999927826226    100 элементов
0.773911299998872       1000 элементов
"""
