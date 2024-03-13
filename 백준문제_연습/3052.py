remain = list()

for i in range(0, 10):
    num = int(input())
    remain.append(num % 42)

result = len(set(remain))
print(result)