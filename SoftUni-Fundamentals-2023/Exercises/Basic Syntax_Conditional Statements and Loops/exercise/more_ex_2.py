word = input()
index = []
for i in range(len(word)):
    if word[i].isupper():
        index.append(i)
    else:
        continue
print(index)
