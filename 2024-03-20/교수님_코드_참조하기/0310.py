import sys

#data =[i.rstrip() for i in sys.stdin.readlines()]
#print('\n'.join(sorted(data)))

# data =[int(i.rstrip()) for i in sys.stdin.readlines()]
# S = sum(data)
# N = len(data)
# print(int(S/N), data[int(N/2)], sep='\n')


# N, k = map(int, input().split())
# data = list(map(int, input().split()))
# print(sorted(data, reverse=True)[k-1])

import sys

N = int(input())
#EOF
data = [d.rstrip() for d in sys.stdin.readlines()]
print(" ".join(sorted(data)))
#print(data)
#data.sort()
#print(data)