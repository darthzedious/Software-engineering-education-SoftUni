import re
total_ckal = 0
pattern = r"([\|#])([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1"
line = input()
matches = re.finditer(pattern, line)
for match in matches:
    total_ckal += int(match.groups()[3])
days = total_ckal // 2000
print(f"You have food to last you for: {days} days!")
matches = re.finditer(pattern, line)
for match in matches:
    sep, food, date, ckal = match.groups()
    print(f"Item: {food}, Best before: {date}, Nutrition: {ckal}")
