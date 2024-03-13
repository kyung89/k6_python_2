N, k = list(map(int, input().split()))
students = list(map(int, input().split()))
students.sort(reverse=True)
print(students[k-1])
   
