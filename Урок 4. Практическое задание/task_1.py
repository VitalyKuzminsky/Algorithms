"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""


from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


t1 = timeit('func_1', globals=globals())  # -> 0.04465719999279827
t2 = timeit('func_2', globals=globals())  # -> 0.026877099997363985
print(f'функция func_2 на {(100 - (t2 * 100 / t1)):.2f}% быстрее, чем func_1')
# list comprehension выполняется быстрее, чем перебор элементов
