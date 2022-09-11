"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""


from random import randint
from timeit import timeit


def heap_sort_in(list_input):
    def heap_sort(list_in):
        build_max_heap(list_in)
        for i in range(len(list_in) - 1, 0, -1):
            list_in[0], list_in[i] = list_in[i], list_in[0]
            max_heapify(list_in, index=0, size=i)


    def parent(i):
        return (i - 1) // 2


    def left(i):
        return 2 * i + 1


    def right(i):
        return 2 * i + 2


    def build_max_heap(list_in):
        length = len(list_in)
        start = parent(length - 1)
        while start >= 0:
            max_heapify(list_in, index=start, size=length)
            start = start - 1


    def max_heapify(list_in, index, size):
        l = left(index)
        r = right(index)
        if (l < size and list_in[l] > list_in[index]):
            largest = l
        else:
            largest = index
        if (r < size and list_in[r] > list_in[largest]):
            largest = r
        if (largest != index):
            list_in[largest], list_in[index] = list_in[index], list_in[largest]
            max_heapify(list_in, largest, size)
    return heap_sort(list_input)


m = 10
my_list = [randint(0, 100) for i in range(2 * m + 1)]
print(my_list)
heap_sort_in(my_list)
print(timeit('heap_sort_in(my_list[:])', globals=globals(), number=100))
print(my_list)

m = 100
my_list = [randint(0, 100) for i in range(2 * m + 1)]
print(my_list)
heap_sort_in(my_list)
print(timeit('heap_sort_in(my_list[:])', globals=globals(), number=100))
print(my_list)

m = 1000
my_list = [randint(0, 100) for i in range(2 * m + 1)]
print(my_list)
heap_sort_in(my_list)
print(timeit('heap_sort_in(my_list[:])', globals=globals(), number=100))
print(my_list)

"""
Сортировка Кучей
0.007658199989236891    10 элементов
0.13244169997051358     100 элементов
1.8442926000570878      1000 элементов
"""
