"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""


from random import randint
from timeit import timeit


def non_sort(list_in):
    temp = list_in
    left_list = []
    right_list = []
    for i in range(len(temp)):
        for j in range(len(temp)):
            if temp[i] > temp[j]:
                left_list.append(temp[j])
            if temp[i] < temp[j]:
                right_list.append(temp[j])
            if temp[i] == temp[j] and i > j:
                left_list.append(temp[j])
            if temp[i] == temp[j] and i < j:
                right_list.append(temp[j])
        if len(left_list) == len(right_list):
            return temp[i]
        left_list.clear()
        right_list.clear()


m = 10
my_list = [randint(0, 100) for i in range(2 * m + 1)]
print(my_list)
print(non_sort(my_list))
print(timeit('non_sort(my_list[:])', globals=globals(), number=100))

m = 100
my_list = [randint(0, 100) for i in range(2 * m + 1)]
print(my_list)
print(non_sort(my_list))
print(timeit('non_sort(my_list[:])', globals=globals(), number=100))

m = 200
my_list = [randint(0, 100) for i in range(2 * m + 1)]
print(my_list)
print(non_sort(my_list))
print(timeit('non_sort(my_list[:])', globals=globals(), number=100))

"""
0.016603800002485514    10 элементов
0.11920870002359152     100 элементов
4.529515700065531       200 элементов  
1000 элементов я не дождался, было более 2-х минут, когда я прервал скрипт
"""
