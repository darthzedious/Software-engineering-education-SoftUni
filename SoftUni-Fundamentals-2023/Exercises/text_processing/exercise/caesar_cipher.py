text = input()
encrypted_message = ""
for ch in text:
    ascii_char = chr(ord(ch) + 3)
    encrypted_message += ascii_char
print(encrypted_message)
