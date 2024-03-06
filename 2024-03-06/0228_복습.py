type(1), type('1'), type("1") # (int, str, str)

a, b = input().split()
a, b = int(a), int(b)

a , b = 7, 3
a + b, a - b, a * b, type(a/b), a % b # (10, 4, 21, float, 1)

s = input()

s, len(input()) # ("pulljima", 8)

a = list()
b = []
type(a), type(b) # (list, list)

a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
a # [1, 2, 3, 4, 5]

# 생성, 조회, 수정, 삭제
a = [1, 2, 3, 4, 5]
a[::-1], a[-1], a[:-2], a[2:] # ([5, 4, 3, 2, 1], 5, [1, 2], [3, 4, 5])

s = "abcde"
s[::-1], s[-1], s[:2], s[2:] # ("edcba", 'e', 'ab', 'cde')

for i in [1,2,3,4,5]:
    print(i)

for s in "abcde":
    print(s)

for i in range(1, 6):
    print(i)

a[2] = 10 # 리스트의 요소 수정하기



