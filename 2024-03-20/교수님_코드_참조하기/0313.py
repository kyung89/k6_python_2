# import numpy as np

# M, N = map(int, input().split())
# print(M, N)
# A = [list(map(int, input().split())) for _ in range(M)]
# B = [list(map(int, input().split())) for _ in range(N)]

# #print(np.array(A).dot(np.array(B)))

# for a, b in zip(A, B):
#     print(' '.join([str(a[i]+b[i]) for i in range(M)]))
import numpy as np
import sys
data = [list(map(int, d.split())) for d in sys.stdin.readlines()]
print(np.max(data))

# max_val = 0
# max_pos = (0, 0)
# for i, rows in enumerate(data, start=1):
#     for j, row in enumerate(rows, start=1):
#         if max_val < row:
#             max_val = row
#             max_pos = (i, j)
# print(max_val)
# print(max_pos)

# import numpy as np
# print(np.array([]))

#print(max([2, 3, 41, 44]))
