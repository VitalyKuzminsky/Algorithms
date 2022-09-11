"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""


from memory_profiler import profile


@profile
def func_in_func(number_in_first):
    def revers_numbers(number_in):
        if number_in < 10:
            return str(number_in)
        else:
            return str(number_in % 10) + revers_numbers(number_in // 10)
    return revers_numbers(number_in_first)


number_to_revers = 123456789
print(f'Перевернутое число: {func_in_func(number_to_revers)}')

"""
Проблема профилирования памяти в скрипте с рекурсией в том, что таблица будет появляться 
при каждой вызове рекурсии
"""
