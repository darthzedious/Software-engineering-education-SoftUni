import re
text = input()
regex = r"([:]{2}|[*]{2})([A-Z][a-z]{2,})(\1)"
digit_regex = f"\d"
cool_threshold = 1
emoji_match = re.finditer(regex, text)
digit_match = re.findall(digit_regex, text)

digit_match_as_int = [int(x) for x in digit_match]
for number in digit_match_as_int:
    cool_threshold *= number

emojies = []
cool_emojies = []

for match in emoji_match:
    emojies.append(match.group(2))
    ascii_sum = sum(list(ord(x) for x in match.group(2)))
    if ascii_sum >= cool_threshold:
        cool_emojies.append("".join(match.groups()))

print(f"Cool threshold: {cool_threshold}")
print(f"{len(emojies)} emojis found in the text. The cool ones are: ")
for emoji in cool_emojies:
    print(emoji)
