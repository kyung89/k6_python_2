# data = []
# for _ in range(10):
#     data.append(int(input()) % 42)

# answer = []
# for d in data:
#     if d not in answer:
#         answer.append(d)
# print(len(answer))

#print(data)
#data = [int(input()) % 42 for _ in range(10)]
#print(len(set(data)))

# T = int(input())
# for _ in range(T):
#     N, S = input().split()
#     N = int(N)
#     print(''.join([c*N for c in S]))

#s = input()
#print(len(s.split()))

# N = int(input())
# data = { int(i):1 for i in input().split()}
# print(data)
# M = int(input())
# query = [int(i) for i in input().split()]
# print(query)
# for q in query:
#     print(data.get(q, 0), end=' ')

# N, M = map(int, input().split())
# S = {input():1 for _ in range(N)}
# Q = [input() for _ in range(M)]
# print(S)
# print(Q)
# print(sum([True for q in Q if q in S]))
