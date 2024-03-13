N, M = input().split() 

S =  {}
result = 0

for _ in range(int(N)):
    word = input()
    S[word] = 0

for _ in range(int(M)):
    word = input()
    if S.keys().__contains__(word): result += 1

print(result)

