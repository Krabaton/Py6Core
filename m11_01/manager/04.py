from contextlib import contextmanager


@contextmanager
def managed_resource(*args, **kwargs):
    file_handler = open(*args, **kwargs)
    try:
        yield file_handler
    finally:
        file_handler.close()


with managed_resource('new_file.txt', 'r') as f:
    print(f.read())

with managed_resource('01_fw.py', 'r', encoding='utf-8') as f:
    print(f.read())

with managed_resource('new_file.txt', 'r') as f:
    print(f.read())
