word = input()
new_word = ""
for ch in range(len(word)):
    if ch == 0 and word[ch] == word[ch - 1]:
        new_word += word[ch]
    if word[ch] != word[ch - 1]:
        new_word += word[ch]
print(new_word)
