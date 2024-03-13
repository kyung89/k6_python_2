n = int(input())

logs = {}
for _ in range(n):
    person, state = input().rstrip().split()
    if state == "enter": logs[person] = True
    else: del logs[person]

print("\n".join(sorted(logs.keys(), reverse=True))),

