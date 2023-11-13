char_to_remove = input()
text = input()
while char_to_remove in text:
    text = text.replace(char_to_remove, "")
print(text)
