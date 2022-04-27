'''
Задача: Сортировка файлов в папке. Скопировать файлы из указанной папки и положить в новую папку с  расширениям этого файла.
'''

import argparse
from pathlib import Path
from shutil import copyfile

parser = argparse.ArgumentParser(description='Sorting folder')
parser.add_argument('--source', '-s', required=True, help='Source folder')
parser.add_argument('--output', '-o', default='dist', help='Output folder')
args = vars(parser.parse_args())
source = args.get('source')
output = args.get('output')


def read_folder(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            read_folder(el)
        else:
            copy_file(el)
            # ext = el.suffix
            # new_path = output_folder / ext
            # new_path.mkdir(exist_ok=True, parents=True)
            # copyfile(el, new_path / el.name)


def copy_file(file: Path) -> None:
    ext = file.suffix
    new_path = output_folder / ext
    new_path.mkdir(exist_ok=True, parents=True)
    copyfile(file, new_path / file.name)


output_folder = Path(output)  # dist
read_folder(Path(source))
