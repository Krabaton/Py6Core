from time import time


def read_file(filename):
    text_file = open(filename, 'r')
    lines = text_file.readlines()
    text_file.close()
    return lines


start = time()
data = read_file('data.txt')
for l in data:
    print(l)
print(time() - start)

