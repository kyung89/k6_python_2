N = int(input())

words = []
for _ in range(N):
    words.append(input())

group_word_count = 0
for word in words:
    is_group_word = True
    exists = []
    w1 = word[0]
    for w2 in range(len(word)):

        if word[w2] in exists: 
            is_group_word = False
            break

        if w1 == word[w2]:
            continue
        else:
            exists.append(w1) 
            w1 = word[w2]
    if is_group_word: group_word_count += 1

print(group_word_count)
