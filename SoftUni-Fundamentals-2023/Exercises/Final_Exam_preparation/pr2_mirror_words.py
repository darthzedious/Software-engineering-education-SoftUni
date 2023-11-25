import re
regex = r"(@|#)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"
words = input()
match = re.findall(regex, words)
mirror_pairs = []

for mirror in match:
    if mirror[1] == mirror[2][::-1]:
        mirror_pairs.append(f"{mirror[1]} <=> {mirror[2]}")

if len(match) > 0:
    print(f"{len(match)} word pairs found!")
    if len(mirror_pairs) == 0:
        print(f"No mirror words!")
    else:
        print("The mirror words are:")
        print(", ".join(mirror_pairs))
else:
    print("No word pairs found!")
    print("No mirror words!")
