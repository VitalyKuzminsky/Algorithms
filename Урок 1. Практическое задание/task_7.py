"""
Задание 7. На закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов,
например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить
проверку на палиндром и в таких строках (включающих пробелы)

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--код с нуля писать не нужно, требуется доработать пример с урока
"""


class MyDequeClass:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return self.elements == []

    def add_first(self, el):
        self.elements.append(el)

    def add_to_end(self, el):
        self.elements.insert(0, el)

    def remove_first(self):
        return self.elements.pop()

    def remove_end(self):
        return self.elements.pop(0)

    def size(self):
        return len(self.elements)


def palindrome_check(text_in: str):
    mdc_obj = MyDequeClass()
    new_text = text_in.replace(' ', '')
    for el in new_text:
        mdc_obj.add_to_end(el)

    palindrome = 'Это палиндром'

    while mdc_obj.size() > 1 and palindrome:
        first = mdc_obj.remove_first()
        end = mdc_obj.remove_end()
        if first != end:
            palindrome = 'Это не палиндром'

    return palindrome


print(palindrome_check("молоко делили ледоколом"))
print(palindrome_check("молоко делил ледоколом"))
