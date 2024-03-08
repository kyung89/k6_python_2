from functools import reduce

def add(a,b):
    return a + b

square = lambda x:x**2
even = lambda x:x%2 ==0

reduce(add, filter(even, map(square, range(11))))
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 4 + 16 + 36 + 64 + 100
# 220

# while 문
print("# while 문")
n = 0
while n < 2:
    print(n)
    n += 1
print()

# break 사용
print("# break 사용")
n = 0
while True:
    print(n)
    n += 1
    if n == 6: break
print()

# flag 사용
print('# flag 사용')
n = 0
active = True
while active:
    print(n)
    n += 1
    if n == 6: active = False
print()

# continue 사용
print("# continue 사용")
n = 0
while True:
    n += 1
    if n == 2: continue
    print(n)
    if n == 6: break
print()

# 리스트, 딕셔너리와 함께 while 루프 사용하기
print("# 리스트, 딕셔너리와 함께 while 루프 사용하기")
for i in [1,2,3]: print(i)
# 1
# 2
# 3
print()
[i for i in range(10)] # [0,1,2,3,4,5,6,7,8,9]

# 리스트에서 다른 리스트로 요소 옮기기
# 파일에서 다른 파일로 요소 옮기기
print('# 리스트에서 다른 리스트로 요소 옮기기')
a = [1,2,3]
b = []
for i in a: b.append(i)

a = [1,2,3]
b = []
for _ in range(3): 
    p = a.pop()
    b.append(p)
print("a", a)
print("b", b)
print()

a = [1,2,3]
b = []
while a: # p.187
    p = a.pop()
    b.append(p)
print("a", a)
print("b", b)
print()

a = [1,2,3,2,3]
a.remove(2) # [1,3,2,3]

d1 = {}
d1["정원"] = list(map(int, input().split()))
# 입력: 1 2 3 4 5
d1 # {"정원": [1,2,3,4,5]}

# data 변형 map("f", data)
# data 조건 filter("f", data)
# data 줄이기 reduce("f", data)

data = range(11)
square = lambda x:x**2
even = lambda x:x%2 ==0
square(2)

list(map(square, data)) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list(filter(even, data)) # [0, 2, 4, 6, 8, 10]

add = lambda a,b:a+b
reduce(add, data) #550