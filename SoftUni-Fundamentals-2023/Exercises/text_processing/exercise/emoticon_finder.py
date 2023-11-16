text = input()
for ch in range(len(text)):
    if text[ch] == ":":
        print(f":{text[ch + 1]}")
        