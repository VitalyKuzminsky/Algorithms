"""
Задание 1.

Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете,
опираясь на примеры с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""


def algorithm_haffman(text_in):
    count_el = Counter(text_in)
    sorted_elements = deque(sorted(count_el.items(), key=lambda item: item[1]))
    print(sorted_elements)
    if len(sorted_elements) != 1:
        while len(sorted_elements) > 1:
            value = sorted_elements[0][1] + sorted_elements[1][1]
            comb = {0: sorted_elements.popleft()[0],
                    1: sorted_elements.popleft()[0]}
            for i, _count in enumerate(sorted_elements):
                if value > _count[1]:
                    continue
                else:
                    sorted_elements.insert(i, (comb, value))
                    break
            else:
                sorted_elements.append((comb, value))
    else:
        value = sorted_elements[0][1]
        comb = {0: sorted_elements.popleft()[0], 1: None}
        sorted_elements.append((comb, value))
    return sorted_elements[0][0]


encrypted_text = {}


def haffman_encode(tree, path=''):
    if not isinstance(tree, dict):
        encrypted_text[tree] = path
    else:
        haffman_encode(tree[0], path=f'{path}0')
        haffman_encode(tree[1], path=f'{path}1')


text = 'This is my code!'
haffman_encode(algorithm_haffman(text))
code = []
for el in encrypted_text:
    code.append(encrypted_text[el])
print(' '.join(code))
