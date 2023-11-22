import re
furniture = []
total_money_spent = 0
pattern = r">>([A-Za-z]+)<<([\d\.]+)!(\d+)"
while True:
    command = input()
    if command == "Purchase":
        break
    match = re.search(pattern, command)
    if match:
        furniture_type, price, quantity = match.groups()
        furniture.append(furniture_type)
        total_money_spent += float(price) * int(quantity)

print(f"Bought furniture:")
for item in furniture:
    print(item)
print(f"Total money spend: {total_money_spent:.2f}")
