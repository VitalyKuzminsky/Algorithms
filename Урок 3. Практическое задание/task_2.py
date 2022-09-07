"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""


from hashlib import sha256


def save_pass(path_bd_password: str):
    with open(path_bd_password, 'w', encoding='utf-8') as f:
        login = input('Введите логин:\n')
        password = input('Введите пароль:\n')
        hash_obj = sha256(login.encode() + password.encode()).hexdigest()
        f.write(f'{login}:{hash_obj}')


def authentication(path_bd_password: str):
    with open(path_bd_password, 'r', encoding='utf-8') as f:
        print('Вход в систему:')
        login = input('Введите логин:\n')
        password = input('Введите пароль:\n')
        hash_obj = sha256(login.encode() + password.encode()).hexdigest()
        for line in f:
            a = line.split(':')
            key, value = a[0], a[1]
            if key == login:
                if value == hash_obj:
                    print('Вы ввели правильный пароль')
                else:
                    print('Пароль не верен')
            else:
                print('Такого пользователя нет')


save_pass('bd_password.cvs')
authentication('bd_password.cvs')
