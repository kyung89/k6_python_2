N = input()
n_nums = input().split()

M = input()
m_nums = input().split()

result = {}
for m in m_nums: result[m] = 0
for n in n_nums: 
    if n in result: result[n] = 1

for r in result:
    print(result[r], end=" ")