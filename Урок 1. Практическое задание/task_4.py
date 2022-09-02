"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

dict_users = {
    'alex': {
        'password': 'qwerty',
        'activation': True
    },
    'max': {
        'password': 'god',
        'activation': True
    },
    'leo': {
        'password': '1111',
        'activation': False
    }
}


def authentication_1(users: dict, login: str, password: str) -> str:
    """
    O(n) линейная
    Проводит проверку, может ли пользователь быть допущен к ресурсу по логину,
    паролю и активации учётной записи.
    Если учетная запись не активирована, то польз-лю предлагается ее пройти.
    :param users: dict словарь с пользователями веб-ресурса.
    :param login: str логин пользователя.
    :param password: str пароль пользователя.
    :return: str результат аутентификации
    """
    for key, val in users.items():              # O(n) линейная
        if key == login:                        # O(1) константная
            if val['password'] == password and val['activation']:        # O(1) константная
                return 'Доступ разрешён!'                                # O(1) константная
            elif val['password'] == password and not val['activation']:  # O(1) константная
                return 'Вам необходимо активировать учётную запись!'     # O(1) константная
            elif val['password'] != password:                            # O(1) константная
                return 'Не верный пароль!'                               # O(1) константная

    return 'Пользователь с таким именем не найден в системе!'            # O(1) константная


def authentication_2(users: dict, login: str, password: str) -> str:
    """
    O(1) константная
    Проводит проверку, может ли пользователь быть допущен к ресурсу по логину,
    паролю и активации учётной записи.
    Если учетная запись не активирована, то польз-лю предлагается ее пройти.
    :param users: dict словарь с пользователями веб-ресурса.
    :param login: str логин пользователя.
    :param password: str пароль пользователя.
    :return: str результат аутентификации
    """
    if users.get(login):                                                            # O(1) константная
        if users[login]['password'] == password and users[login]['activation']:     # O(1) константная
            return 'Доступ разрешён!'                                               # O(1) константная
        elif users[login]['password'] == password and not users[login]['activation']:   # O(1) константная
            return 'Вам необходимо активировать учётную запись!'                    # O(1) константная
        elif users[login]['password'] != password:                                  # O(1) константная
            return 'Не верный пароль!'                                              # O(1) константная
    else:
        return 'Пользователь с таким именем не найден в системе!'                   # O(1) константная


print(authentication_1(dict_users, 'alex', 'zaq1'))
print(authentication_1(dict_users, 'max', 'god'))
print(authentication_1(dict_users, 'leo', '1111'))
print(authentication_1(dict_users, 'kate', 'qwerty'))
print()
print(authentication_2(dict_users, 'alex', 'zaq1'))
print(authentication_2(dict_users, 'max', 'god'))
print(authentication_2(dict_users, 'leo', '1111'))
print(authentication_2(dict_users, 'kate', 'qwerty'))

"""
Вывод: 2-ая функция (authentication_2) эффективнее, т.к. сложность алгоритма O(1) константная 
предпочтительней, чем O(n) линейная
"""
