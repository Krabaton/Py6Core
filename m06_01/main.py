'''
Задача: Сортировка файлов папке. Скопировать файлы из указанной папки и положить в новую, в папки с  расширениями этих файлов.
'''

import argparse
from pathlib import Path
from shutil import copyfile
