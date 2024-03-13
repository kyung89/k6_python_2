alphabet = input().lower()

count = {}
for a in alphabet:
    if a in count: count[a] += 1
    else: count[a] = 0

max = max(count.values())

result = []
for k, v in count.items(): 
    if v == max: result.append(k)

if len(result) > 1: print("?")
else: print(result[0].upper())