N, X = input().split()
nums = list(map(int,input().split()))

smallThan = []
for num in nums:
    if int(X) > num: 
        smallThan.append(str(num))
    
print(" ".join(smallThan))