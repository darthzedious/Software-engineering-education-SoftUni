import re
line = input()
pattern = r"\s(([a-z\d]+[a-z\d\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"
match = re.findall(pattern, line)
for mail in match:
    searched_mail = mail[0]
    print(searched_mail)
