
'''
Работа с архивами
'''


import shutil


print(shutil.get_archive_formats())

archive_file = shutil.make_archive('my_archive_file', 'zip', 'Temp')
print(archive_file)
shutil.unpack_archive(archive_file, 'Test/Temp/Test/Inner')
