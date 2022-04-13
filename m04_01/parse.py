from pathlib import Path

p = Path('.')

# print(p.parent)
# print(p.name)
# print(p.suffix)
# print(p.exists())
# print(p.is_dir())
# print(p.is_file())
# iterdir


def parse_folder(path):
    for el in path.iterdir():
        if el.is_dir():
            print(f"This is folder: {el}")
        else:
            print(f"This is file: {el}")


def parse_file(path):
    for el in path.iterdir():
        if el.is_dir():
            parse_file(el)
        else:
            print(f"This is file: {el}")


parse_file(p)
