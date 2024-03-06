print("hello world!")
print()

type(1), type('1'), type("1")

s = "abcde"

print(s[:2], s[2:])
print()

for s in [1,2,3,4,5]:
    print(s)
print()
for s in "abcde":
    print(s)
print()

for s in range(1,6):
    print(s)
print()

type([1,2,3,4,5]), type((1,2,3,4,5)), type("abcde"), type(range(1,6))

d = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

type(d)

for i in d: 
    print(d[i])
print()

for i in range(1,6):
    if i % 2 == 0:
        print(i, "2")
    elif i % 3 == 0:
        print(i, "3")
    else:
        print("unknown")
print()

# 에러내고 F8 누르면 에러 난 데로 바로 간다
# 들여쓰기 주의!

