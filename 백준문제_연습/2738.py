N, M = input().split()

N = int(N)
M = int(M)

A = []
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

B = []
for _ in range(N):
    row = list(map(int, input().split()))
    B.append(row)

C = []
for row_idx in range(N):
    c_row = []
    for item_idx in range(M):
        c_row.append(str(A[row_idx][item_idx] + B[row_idx][item_idx]))
    C.append(c_row)

for row in C:
    print(" ".join(row))