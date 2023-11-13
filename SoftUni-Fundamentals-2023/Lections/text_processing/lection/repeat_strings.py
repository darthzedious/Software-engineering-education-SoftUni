text = input().split()
output_text = ""
for word in text:
    output_text += word * len(word)
print(output_text)
