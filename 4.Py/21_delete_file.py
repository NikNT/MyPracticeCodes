import os
import shutil

path = 'text.txt'

try:
    os.remove(path)
    os.rmdir('test')
    shutil.rmtree('empty')
except FileNotFoundError:
    print(f'File {path} not found!')
except PermissionError:
    print('You do not have permission to delete that!')
except OSError:
    print('Folder is not empty')
else:
    print(f'{path} was deleted')    