text = tuple(input())
text_data = {}
for ch in text:
    if ch not in text_data.keys():
        text_data[ch] = 0
    text_data[ch] += 1
for ch, number in sorted(text_data.items()):
    print(f"{ch}: {number} time/s")
