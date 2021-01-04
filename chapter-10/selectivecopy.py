# "Selective Copy" program of Chapter 9
# The code shows an error but works fine
# By JITHIN JOHN
import shutil
import os
import pathlib
subfolder = pathlib.Path()
os.makedirs(pathlib.Path.cwd()/pathlib.Path('result'))
loc = pathlib.Path.cwd()/pathlib.Path('result')
for folderName, subfolders, filenames in os.walk(pathlib.Path.cwd()):
    for filename in filenames:
        if folderName != pathlib.Path.cwd()/pathlib.Path('result'):
            print('FILE INSIDE ' + folderName + ': '+ filename)
            if filename.endswith('pdf'):
                shutil.copy(os.path.join(folderName, filename), loc)
    print('')
