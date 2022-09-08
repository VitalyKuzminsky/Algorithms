"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""


from timeit import timeit
from cProfile import run


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    return ''.join(reversed(str(enter_num)))


def time_check(number_in: int, *args):
    times = {}
    for el in args:
        times[el] = timeit(f'{el}({number_in})', globals=globals())
    for key, value in times.items():
        print(f'Время выполнения функции {key}: {value}')


number = 4789
time_check(number, 'revers_1', 'revers_2', 'revers_3', 'revers_4')
print()
run('revers_1(number)')
run('revers_2(number)')
run('revers_3(number)')
run('revers_4(number)')

"""
Время выполнения функции revers_1: 1.6248673999216408
Время выполнения функции revers_2: 1.0988760999171063
Время выполнения функции revers_3: 0.37664820009376854
Время выполнения функции revers_4: 0.6481388999382034

Самым шустырм оказался срез, за ним встроенная функция реверса,
а так как в рекурсии и цикле есть расчёты, поэтому они проигрывают в 2-5 раз.
"""
