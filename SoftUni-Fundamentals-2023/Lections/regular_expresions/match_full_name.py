import re
names = input()
tester = "\\b[A-Z][a-z]+ [A-Z][a-z]+\\b"

test = re.findall(tester, names)

for name in test:
    print(name, end=" ")
