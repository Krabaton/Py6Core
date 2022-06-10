# Печать и нумерация строк в текстовом файле.
import pickle


class SongReader:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, encoding='utf-8')
        self.line_count = 0

    def readline(self):
        self.line_count += 1
        line = self.file.readline()
        if not line:
            return None
        if line.endswith('\n'):
            line = line[:-1]
        return f'{self.line_count}: {line}'

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['file']  # Незначащая информация
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        file = open(self.filename, encoding='utf-8')
        for _ in range(self.line_count):
            file.readline()
        self.file = file


if __name__ == '__main__':
    reader = SongReader('song.txt')
    print(reader.readline())
    print(reader.readline())
    new_reader = pickle.loads(pickle.dumps(reader))
    while True:
        line = new_reader.readline()
        if line is None:
            break
        else:
            print(line)

    print('----------')
    print(reader.readline())
    print(reader.readline())
