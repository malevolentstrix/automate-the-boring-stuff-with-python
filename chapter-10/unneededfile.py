# "Deleting Unneeded Files" program of Chapter 10
# By JITHIN JOHN
import os
import pathlib
folder = pathlib.Path.cwd()
for foldername, subfolders, filenames in os.walk(folder):
    for file in filenames:
        path = os.path.join(foldername, file)
        size = os.path.getsize(full_path)
        if size > 100000000:
            print(path)
