import re
date = input()
test = r"(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})"
match = re.findall(test, date)

for info in match:
    print(f"Day: {info[0]}, Month: {info[2]}, Year: {info[3]}")
