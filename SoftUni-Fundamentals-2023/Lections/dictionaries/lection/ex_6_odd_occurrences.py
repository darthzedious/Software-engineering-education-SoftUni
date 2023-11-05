words = input().split()
words_count = {}
for word in words:
    word_lower = word.lower()
    if word_lower not in words_count:
        words_count[word_lower] = 0
    words_count[word_lower] += 1

for word, value in words_count.items():
    if int(value) % 2 != 0:
        print(word, end=" ")
