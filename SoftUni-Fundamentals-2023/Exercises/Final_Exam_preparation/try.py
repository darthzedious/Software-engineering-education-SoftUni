import re


def validate_input(input_str):
    pattern = r'^\|([A-Z]{4,})\|:#([A-Za-z]+\s[A-Za-z]+)#$'
    match = re.match(pattern, input_str)
    if match:
        boss_name = match.group(1)
        title = match.group(2)
        return boss_name, title
    else:
        return False


num_inputs = int(input())
for _ in range(num_inputs):
    input_str = input()
    validated_input = validate_input(input_str)
    if validated_input:
        boss_name, title = validated_input
        print(f"{boss_name}, The {title} \n"
              f">> Strength: {len(boss_name)}\n"
              f">> Armor: {len(title)}")
    else:
        print("Access denied!")
