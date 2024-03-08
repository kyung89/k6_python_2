import os

from pathlib import Path

# dir_path = Path ('./aaa')
# print(dir_path)

file_path = Path ('./aaa/a.txt')
print(file_path)

# print(os.path.isdir(dir_path))
# print(os.path.isdir(file_path))

# for d in os.listdir():
#     print(d, os.path.isdir(d))
#     if '.txt' in d:
#         print('FOUND!')

#no_file = Path ('./aaa/b.txt')
#print(no_file.exists())
#print(file_path.exists())

#print(os.path.split(Path('./aaa/b.txt')))
#print(Path('aaa', 'b.txt'))


# top = Path('.')

# for root, dirs, files in top.walk(top_down=False):
#     for name in files:
#         (root / name).unlink()
#     for name in dirs:
#         (root / name).rmdir()

path = Path ('./aaa/aa.txt')

with open(path, 'w') as file:
    file.write('a\n')
    file.write('aa\n')
    file.write('aaa\n')
    file.write('aaaa\n')

# path = Path ('./aaa/aaa.txt')

# try:
#     if path.exists():
#         with open(path) as file:
#             for line in file:
#                 print(line)

# except Exception as e:
#     pass
#     #print(e)


#import json
#import pickle

#json.dumps("{'name':'kim', 'age': 22}")
#json.loads("{'name':'kim', 'age': 22}")
 


# data = json.parse("{'name':'kim', 'age': 22}")
# type(data) #json
# print(data.name) #1
# print(data.age) #2


