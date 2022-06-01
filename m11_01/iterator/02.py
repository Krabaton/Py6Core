"""
Реализуем итератор, который выполняет итерацию заданное количество раз по заданной последовательности
"""


class MyIterator:
    def __init__(self, seq, count_loop):
        self.seq = seq
        self.count_loop = count_loop
        self.loop = 0
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.loop >= self.count_loop:
            raise StopIteration
        else:
            value = self.seq[self.index]
            self.index += 1
            if self.index == len(self.seq):
                self.index = 0
                self.loop += 1
            return value


seq = ['a', 'b', 'c']
my_iter = MyIterator(seq, 10)

for el in my_iter:
    print(el, end=' ')

