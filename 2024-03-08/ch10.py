# 2024-03-08

# 백준 풀이:
# 	3052 나머지 
# 	2675 문자열 반복 
# 	1152 단어의 개수 

# 	10815 숫자 카드 
# 	14425 문자열 집합 

with open("name.txt", encoding="utf-8") as file:
   # for line in file:
        #print(line.rstrip()) # 끝에 날리기
    print(file.readlines()) # ['양하늘\n', '김호인\n', '구애진\n', '선미진']
print()

print('A', end="\n") # default
print('A', end="")
print('B', end="")
print()
print()

def add(a = 1, b = 2):
    return a+b

print(add()) #3
print()

print('A', end=", ")
print('B', end="")
print()
print()

print('A', 'B', "C", sep=", ")
print('B', end="\n")
print()

# CSV 파일 읽기 쓰기: https://docs.python.org/ko/3/library/csv.html
import csv

with open('grade.csv') as file:
    reader = csv.reader(file)
    header = next(reader) # header 따로 빼기
    for line in reader:
        print(line)
    #print(next(reader)) # 에러! StopIteration
    print(header)
print()

n = range(5) # range: class
print(n)
r = iter(n)
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
#print(next(r)) # 에러! StopIteration
print()

# 경로
from pathlib import Path

file_path = Path("./aaa/test.txt")
print(file_path)
print()

dir_path = Path("./aaa")
print(dir_path)
print()

# 김태연 교수님이 많이 쓰시는 것
import os
from pathlib import PurePath
# 윈도우(\)와 리눅스(/)는 경로 표시가 다르다: 관련된 에러날 수 있음!!!
 
# os.path.isdir
print(os.path.isdir(file_path)) # False
print(os.path.isdir(dir_path)) # True
print()

# os.listdir()
# if '.txt' in d
for d in os.listdir():
    print(d, os.path.isdir(d))
    if '.txt' in d:
        print("FOUND!")
print()

# os.path.exists
no_file = Path("./aaa/b.txt")
print(os.path.exists(no_file)) # False
print(os.path.exists(file_path)) # True
print()

# 경로 끊기
print(os.path.split(Path("./aaa/b.txt")))
print(Path('aaa', 'a.txt'))
print()

# test.py [1] 참조할 것 START
top = Path('aaa') # aaa 폴더에 있는 모든 것 삭제하는 코드임!
for root, dirs, files in os.walk(top, topdown=False): # 체크 필요
    for name in files:
        os.unlink(root +"/"+ name)
    for name in dirs:
        os.rmdir(root +"/"+ name)
# test.py [1] 참조할 것 END

path = Path("./aaa/aa.txt")

with open(path, 'w') as file:
    file.write('a\n')
    file.write('aa\n')
    file.write('aaa')

path = Path("./aaa/aaa.txt")
if path.exists():
    with open(path) as file:
        for line in file:
            print(line)
     
try:
    with open(path) as file:
        for line in file:
            print(line)
except Exception as e:
    pass
    print(e)
print()

# JSON: https://docs.python.org/ko/3/library/json.html#module-json
import json
#import pickle

# test.py [2] 참조할 것 START
data = json.loads('{"a": 1, "b": 2}')
type(data) # json
print(data["a"]) # 1
print(data["b"]) # 2
# test.py [2] 참조할 것 END

# w 와 a 구분하기: w 덮어쓰기, a 이어쓰기
with open(path, 'a') as file:
    file.write('a\n')
    file.write('aa\n')
    file.write('aaa')

with open(path, 'w') as file:
    file.write('a\n')
    file.write('aa\n')
    file.write('aaa')

# pygame: https://www.pygame.org/news
# dev 폴더에 교재 깃허브 파일 다운로드 했음

