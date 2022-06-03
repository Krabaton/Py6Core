from time import time


def read_file_yield(filename):
    text_file = open(filename, 'r')
    while True:
        line = text_file.readline()
        if not line:
            text_file.close()
            break
        yield line


start = time()
data = read_file_yield('data.txt')
for l in data:
    print(l)
print(time() - start)

