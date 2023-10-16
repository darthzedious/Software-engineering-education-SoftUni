substrings = input().split(", ")
full_list = input().split(", ")
new_list = []
for word in substrings:
    for new_word in full_list:
        if word in new_word:
            new_list.append(word)
            break
print(new_list)
