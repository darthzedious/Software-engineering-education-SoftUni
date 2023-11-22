import re
pattern = r"\b_([A-Za-z\d]+)\b"
line = input()
match = re.findall(pattern, line)
print(",".join(match))
