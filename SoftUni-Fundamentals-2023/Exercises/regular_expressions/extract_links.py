import re
line = input()
pattern = r"(w{3}\.([A-Za-z\d\-]+)\.([a-z\.]+))"
while line:
    match = re.search(pattern, line)
    if match:
        correct_email = match.group(1)
        print(correct_email)
    line = input()
