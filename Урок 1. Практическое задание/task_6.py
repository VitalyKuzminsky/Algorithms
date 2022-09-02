"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте класс-структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class MyQueueClass:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return self.elements == []

    def add_queue(self, el):
        self.elements.insert(0, el)

    def del_queue(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)


class MyTaskBoard:
    def __init__(self):
        self.base_queue = MyQueueClass()    # базовая очередь
        self.queue_for_revision = MyQueueClass()   # очередь на доработку
        self.completed_tasks_list = []  # список решенных задач

    def add_work(self, task: str):
        """Добавляем задачу в базовую очередь"""
        self.base_queue.add_queue(task)

    def task_at_work(self):
        """Задача в работе"""
        return self.base_queue.elements[len(self.base_queue.elements) - 1]

    def finished_task(self):
        """Завершение задачи, добавление в список решенных задач"""
        task = self.base_queue.del_queue()
        self.completed_tasks_list.append(task)

    def add_revision_task(self):
        """Отправка задачи в очередь на доработку"""
        task = self.base_queue.del_queue()
        self.queue_for_revision.add_queue(task)

    def task_at_revision(self):
        """Задача в доработке"""
        return self.queue_for_revision.elements[len(self.queue_for_revision.elements) - 1]

    def from_revision_task(self):
        """Отправка из доработки в базовую очередь"""
        task = self.queue_for_revision.del_queue()
        self.base_queue.add_queue(task)


if __name__ == '__main__':
    task_board = MyTaskBoard()
    task_board.add_work('Задача 1: разработать ТЗ')
    task_board.add_work('Задача 2: сделать дизайн')
    task_board.add_work('Задача 3: написать код')
    task_board.add_work('Задача 4: провести тестирование')
    print(f'Базовая очередь: {task_board.base_queue.elements}')
    print(f'Текущая задача: {task_board.task_at_work()}')
    task_board.finished_task()  # Завершение задачи
    print(f'Базовая очередь: {task_board.base_queue.elements}')
    print(f'Текущая задача: {task_board.task_at_work()}')
    task_board.add_revision_task()  # Отправка задачи в очередь на доработку
    print(f'Задача в доработке: {task_board.task_at_revision()}')
    print(f'Базовая очередь: {task_board.base_queue.elements}')
    task_board.from_revision_task()  # Отправка из доработки в базовую очередь
    print(f'Базовая очередь: {task_board.base_queue.elements}')
    # Упс, теперь дизайн будет делаться после тестирования =))
    # Но доска задач работает верно
    print(f'Текущая задача: {task_board.task_at_work()}')
    print(f'Список решенных задач: {task_board.completed_tasks_list}')
