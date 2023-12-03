spell_book = {}
while True:
    command = input()
    if command == "End":
        break
    if "Enroll" in command:
        cmnd, hero_name = command.split()
        if hero_name not in spell_book.keys():
            spell_book[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")
    elif "Learn" in command:
        cmnd, hero_name, spell_name = command.split()
        if hero_name in spell_book.keys():
            if spell_name in spell_book[hero_name]:
                print(f"{hero_name} has already learnt {spell_name}.")
            else:
                spell_book[hero_name].append(spell_name)
        else:
            print(f"{hero_name} doesn't exist.")
    elif "Unlearn" in command:
        cmnd, hero_name, spell_name = command.split()
        if hero_name in spell_book.keys():
            if spell_name in spell_book[hero_name]:
                spell_book[hero_name].remove(spell_name)
            else:
                print(f"{hero_name} doesn't know {spell_name}.")
        else:
            print(f"{hero_name} doesn't exist.")
print("Heroes:")
for hero_name, info in spell_book.items():
    print(f"== {hero_name}: {', '.join(info)}")
