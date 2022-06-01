"""
Для того, чтобы объект можно было использовать в конструкции with ... as ...: в объекте должны быть определены два
метода: __enter__, __exit__.
__enter__ -- метод, который принимает только один аргумент self. Если метод что-то возвращает, то его вывод будет
записан в переменную val в конструкции with context_manager as val:.
__exit__ -- обязательно принимает 4 аргумента: self, exception type, exception value, exception traceback.
Эти аргументы нужны для корректной обработки исключений внутри __exit__.
"""


class FileWrite:
    def __init__(self, filename):
        self.file = None
        self.opened = False
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w')
        self.opened = True
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)
        if self.opened:
            self.file.close()
        self.opened = False


if __name__ == '__main__':
    with FileWrite('new_file.txt') as f:
        f.write('Hello world!\n')
        f.write('The end\n')


