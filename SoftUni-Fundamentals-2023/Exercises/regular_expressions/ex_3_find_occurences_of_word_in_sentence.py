import re
line = input()
searched_word = input()
pattern = fr"(?i)\b{searched_word}\b"
match = re.findall(pattern, line)
print(len(match))
