words = []
for _ in range(5):
    word = input()
    words.append(word)

max = max([len(word) for word in words])

chg_words = []
for word in words:
    chg_word = []
    for i in range(max):
        if len(word) > i: chg_word.append(word[i])
        else: chg_word.append("")
    chg_words.append(chg_word)

str = ""

for j in range(max):
    for i in range(len(chg_words)):
        str += chg_words[i][j]

print(str)