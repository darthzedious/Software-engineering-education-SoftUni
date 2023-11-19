import re

phone_numbers = input()
regex = "\\+359-2-\d{3}-\d{4}\\b|\\+359 2 \d{3} \d{4}\\b"

test = re.findall(regex, phone_numbers)

print(", ".join(test))
