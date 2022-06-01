# Написать Contex Manager FileReader, который пишет в лог timestamp когда файл был открыт,
# timestamp когда файл был закрыт, имя файла, и как долго файл был открыт с точностью до секунд.

from datetime import datetime


class FileReader:
    log = ''
    instance = None

    def __new__(cls, *args):
        if cls.instance is None:
            cls.instance = super(FileReader, cls).__new__(cls)
        return cls.instance

    def __init__(self, filename):
        self.file = None
        self.opened = False
        self.filename = filename
        self.timestamp = None

    def __enter__(self):
        self.file = open(self.filename, 'r', encoding='utf-8')
        self.opened = True
        self.timestamp = datetime.now().timestamp()
        msg = '{:<20}|{:^15}| open \n'.format(self.timestamp, self.filename)
        self.log += msg
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.opened:
            self.file.close()
            timestamp = datetime.now().timestamp()
            diff = timestamp - self.timestamp
            msg = '{:<20}|{:^15}| closed {:>15}s \n'.format(timestamp, self.filename, round(diff, 6))
            self.log += msg
        self.opened = False


reader = FileReader('new_file.txt')

with reader as f:
    print(f.read())

# print(reader.log)

reader = FileReader('01_fw.py')

with reader as f:
    print(f.read())

print(reader.log)
