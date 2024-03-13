row_num = 1
col_num = 1
max_num = 0
for i in range(9):
    row = list(map(int, input().split()))
    if max_num < max(row):
        max_num = max(row)
        row_num = i + 1
        col_num = row.index(max_num) + 1

print(max_num)
print(str(row_num) + " " + str(col_num))
