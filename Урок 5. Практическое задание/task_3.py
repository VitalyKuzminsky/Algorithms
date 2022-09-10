"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""


from timeit import timeit
from collections import deque

number_iterations = 1000
my_list = [i for i in range(number_iterations)]
my_deque = deque([i for i in range(number_iterations)])

""" 1) сравнить операции """


def append_list(list_in):
    for i in range(number_iterations):
        list_in.append(i)
    return list_in


def append_deque(deque_in):
    for i in range(number_iterations):
        deque_in.append(i)
    return deque_in


def pop_list(list_in):
    for i in range(number_iterations):
        list_in.pop()
    return list_in


def pop_deque(deque_in):
    for i in range(number_iterations):
        deque_in.pop()
    return deque_in


def extend_list(list_in):
    for i in range(number_iterations):
        list_in.extend([1, 2, 3])
    return list_in


def extend_deque(deque_in):
    for i in range(number_iterations):
        deque_in.extend([1, 2, 3])
    return deque_in


""" 2) сравнить операции """


def append_left_list(list_in):
    for i in range(number_iterations):
        list_in.insert(0, i)
    return list_in


def appendleft_deque(deque_in):
    for i in range(number_iterations):
        deque_in.appendleft(i)
    return deque_in


def pop_left_list(list_in):
    for i in range(int(number_iterations / 10)):
        list_in.pop(i)
    return list_in


def popleft_deque(deque_in):
    for i in range(int(number_iterations / 10)):
        deque_in.popleft()
    return deque_in


def extend_left_list(list_in):
    for i in range(number_iterations):
        list_in.insert(0, [1, 2, 3])
    return list_in


def extendleft_deque(deque_in):
    for i in range(number_iterations):
        deque_in.extendleft([1, 2, 3])
    return deque_in


""" 3) сравнить операции получения элемента списка и дека """


def get_list(list_in):
    for i in range(number_iterations):
        list_in[i] = i
    return list_in


def get_deque(deque_in):
    for i in range(number_iterations):
        deque_in[i] = i
    return deque_in


# ==================================================================================


def time_check(*args):
    times = {}
    for func in args:
        times[func] = timeit(f'{func}', globals=globals(), number=number_iterations)
    for key, value in times.items():
        print(f'Время выполнения функции {key}: {value}')


list_func = [
    'append_list(my_list.copy())',
    'append_deque(my_deque.copy())',
    'pop_list(my_list.copy())',
    'pop_deque(my_deque.copy())',
    'extend_list(my_list.copy())',
    'extend_deque(my_deque.copy())',
    'append_left_list(my_list.copy())',
    'appendleft_deque(my_deque.copy())',
    'pop_left_list(my_list.copy())',
    'popleft_deque(my_deque.copy())',
    'extend_left_list(my_list.copy())',
    'extendleft_deque(my_deque.copy())',
    'get_list(my_list.copy())',
    'get_deque(my_deque.copy())'
]
for el in list_func:
    time_check(el)

"""
Время выполнения функции append_list(my_list.copy()): 0.0701069999486208
Время выполнения функции append_deque(my_deque.copy()): 0.0796786000719294

Время выполнения функции pop_list(my_list.copy()): 0.0818734000204131
Время выполнения функции pop_deque(my_deque.copy()): 0.12245540006551892

Время выполнения функции extend_list(my_list.copy()): 0.14017810008954257
Время выполнения функции extend_deque(my_deque.copy()): 0.1901623000157997

Время выполнения функции append_left_list(my_list.copy()): 0.9332645999966189
Время выполнения функции appendleft_deque(my_deque.copy()): 0.07406100002117455

Время выполнения функции pop_left_list(my_list.copy()): 0.041647300007753074
Время выполнения функции popleft_deque(my_deque.copy()): 0.013414100045338273

Время выполнения функции extend_left_list(my_list.copy()): 1.014370399992913
Время выполнения функции extendleft_deque(my_deque.copy()): 0.22532159998081625

Время выполнения функции get_list(my_list.copy()): 0.05103069997858256
Время выполнения функции get_elem_deque(my_deque.copy()): 0.06757529999595135
"""
