import statistics

nums = []
for _ in range(5):
    nums.append(int(input()))

print(statistics.mean(nums))
print(statistics.median(nums))