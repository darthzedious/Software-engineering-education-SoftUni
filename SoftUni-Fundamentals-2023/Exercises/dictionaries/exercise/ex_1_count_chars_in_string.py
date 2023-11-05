symbols = [character for character in input() if character != " "]
dict = {}

for char in symbols:
    if char not in dict.keys():
        dict[char] = 0
    dict[char] += 1

for char, value in dict.items():
    print(f"{char} -> {value}")
