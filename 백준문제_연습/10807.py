size = int(input())
lists = list(map(int,input().split()))
find = int(input())

count = 0
for item in lists:
    if item == find: 
        count += 1

print(count)