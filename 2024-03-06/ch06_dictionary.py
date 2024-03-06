a, b = {}, []
type(a) # dict
type(b) # list

a = {1: 'a', 2: 'b', 3: 'c'} # dictionary 는 key 와 value 로 이루어짐
b = [1, 2, 3]
type(a),type(b) # (dict, list)

a = {'a': 1, 'b': 2, 'c': 3} # 키는 중복이 없어야 한다: 중복이 없나? 중복이 없게 만들 수 있는가? unique + sort
a['b'], a[1] # (2, 2)
# 'b' 는 unique 하다. 

a['d'] = 4 # dictionary 요소 추가하기 
a # {'a': 1, 'b': 2, 'c': 3, 'd': 4} 

a['b'] = 5 # dictionary 요소 수정하기
a # {'a': 1, 'b': 5, 'c': 3}

del a['b'] # dictionary 요소 삭제하기

# dictionary 만들기
scores = {'정원': "A+", "윤정":"A+", "도영":"A+"}

scores = {
    1: {"정원":"A+"},
    2: {"윤정":"A+"},
    3: {"도영":"A+"},
}

scores = {
    1: ["정원","A+"],
    2: ["윤정","A+"],
    3: ["도영","A+"],
}

scores = {
    1: [1,"정원","A+"],
    2: [2,"윤정","A+"],
    3: [3,"도영","A+"],
}

scores[3], scores.get(3) # ([1,"정원","A+"], [1,"정원","A+"])
scores[4] # KeyError
if 4 in scores: scores[4]
scores.get(4) # None: 없음. 에러는 나지않음
scores.get(4, 0) # None 이면 0(값이 없을 때를 대비한 값) 리턴

for row in scores:
    print(row) # key 값

for row in scores.items():
    print(row, type(row)) 
# (1 [1,"정원","A+"] <class 'tuple'>)
# (2 [2,"윤정","A+"] <class 'tuple'>)
# (3 [3,"도영","A+"] <class 'tuple'>)
    
for k, v in scores.items():
    print(k, v)


for row in scores.items():
    print(row[0], row[1], type(row)) #(1 [1,"정원","A+"] <class 'tuple'>)

b = [1,2,3]
b[3] # IndexError

n = len(b)
b[n-1], b[-1] # (3,3)

e = [3,2,1]
e.sort() # e 를 변경한다: [1,2,3]

e = [3,2,1]
sorted(e), e # ([1,2,3], [3,2,1])

sorted(scores) # 키값만 정렬되어 나온다
sorted(scores.items())

db = {9:"B", 7:"A", 3:"C", 5:"C"}
# 성적순으로 sorting 하려면?
first = lambda x:x[0]
second = lambda x:x[1]
for row in db.items():
    print(first(row), second(row))
# 9 B
# 7 A
# 3 C
# 5 C
    
sorted(db.items(), key=second) # [(7, 'A'),(9, 'B'),(3, 'C'),(5 'C')]
sorted(db.items(), key=second, reverse=True) # [(5, 'C'),(3 'C'),(9 'B'),(7 'A')]: 거꾸로 정렬

d1 = {}
d1[3] = False
d1['3'] = False

# 중첩
# for 문 중첩
for x in range(5):
    for y in range(10):
        print(x, y)
    
# if 문 중첩
if x < 5:
    if x < 2:
        print('low')
    else: 
        print('high')

# 리스트 중첩
lst = [[1,2,3],[4,5,6]] # 리스트 중첩 가능
lst # [[1,2,3],[4,5,6]]

# any type

type(1) # int : 객체

# 딕셔너리 중첩
d1 = {
    'a': {
        'aa': 1,
        'aa1': 2
    },
    'b': {
        'bb': 1,
        'bb1': 2
    }
}

d1 = {
    'a': {
        'aa': 1,
        'aa1': 2
    },
    'b': [] # 가능! any type
}

h = "hello"
h # 'hello'
h[0] = "H" # 오류! string 은 수정 불가

def add(x,y):
    return x + y

d1 = {
    'a': {
        'aa': 1,
        'aa1': 2
    },
    'b': add # 가능! any type
}

d1 = {
    'a': {
        'aa': 1,
        'aa1': 2
    },
    'b': range(10) # 가능! any type
}

db2 = {}
db2['a'].append('3') # 에러! a 라는 게 없다
db2['a'].append('옥경림')
db2['a'].append('A+')

db2['a'] = list() # 리스트 쓸려면 선언해줘야 한다
db2['a'].append('3') 
db2['a'].append('옥경림')
db2['a'].append('A+')

db2['b'] = list()
db2['b'] = 3 # 에러! 
db2['b'].append(3) # 리스트에 요소 추가하려면 append 사용해야함

def add(a,b):
    return a + b
data={'a':1, 'b':2}
add(**data) # 3 

data_key = {'a':1, 'b':2, 'c':3}
data_idx = {v:k for k, v in data_key.items()}
data_idx # {1:'a', 2:'b', 3:'c'}

def pow(n):
    return [x**2 for x in range(n) if x % 2 == 0] # [0, 4, 16]

def pow(n):
    lst = []
    for x in range(n):
        if x % 2 == 0:
            lst.append(x**2)
    return lst

# Colab AI 참고
# Notion 을 쓰십시오!



