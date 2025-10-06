import os
from pathlib import Path

# get current work-directory
path = os.getcwd()

folder = Path('/Users/felix/Development/projects/learnPhython/learnPython/Day_6/')
file = folder / 'test_2.txt'

print('folder', folder)

folderFile = Path('/Users/felix/Development/projects/learnPhython/learnPython/Day_6/test_1.txt')
# content of the test_file
print('folderFile read_text()', folderFile.read_text())
# my_file = open(file)

print('folder name: ', folderFile.name)
# suffix-function name suffix of file
print('folder.suffix', folderFile.suffix)
# name of file
print('stem name of file', folderFile.stem)

if not folderFile.exists():
    print('this file does not exist')
else:
    print('yes. it exits')


# print('myfile', my_file.read())
# create a directory
# new_directory = os.makedirs('new_dir')
# path_chdir = os.chdir('/Users/felix/Development/projects/learnPhython/learnPython/Day_3')



print(path)
# print(new_directory)