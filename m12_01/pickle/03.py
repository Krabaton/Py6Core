from pickle import loads, dumps


class A:
    x = 'some'

    def __init__(self):
        print('new A!')
        self.y = 'Другая переменная'


