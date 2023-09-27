n = int(input())
magic_word = input()
all_words = []
for _ in range(n):
    word = input()
    all_words.append(word)
print(all_words)
magic_word_only = []
for current_string in all_words:
    if magic_word in current_string:
        magic_word_only.append(current_string)
print(magic_word_only)
