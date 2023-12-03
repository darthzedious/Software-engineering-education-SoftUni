import re

text = input()
regex = r"[@\/#]+([a-z]{3,})[@\/#]+[\W]+([\d]+)[\/{1,}]"
matches = re.findall(regex, text)

for match in matches:
    print(f"You found {match[1]} {match[0]} eggs!")
    