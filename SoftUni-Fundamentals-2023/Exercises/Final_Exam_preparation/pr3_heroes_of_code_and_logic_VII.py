n = int(input())
heroes = {}
for hero in range(n):
    hero_stat = input()
    hero_name, hp, mp = hero_stat.split()
    hp, mp = int(hp), int(mp)
    heroes[hero_name] = [hp, mp]

while True:
    command = input()
    if command == "End":
        break
    if "CastSpell" in command:
        cmd, hero_name, mp_needed, spell_name = command.split(" - ")
        mp_needed = int(mp_needed)
        if heroes[hero_name][1] >= mp_needed:
            heroes[hero_name][1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif "TakeDamage" in command:
        cmd, hero_name, damage, attacker = command.split(" - ")
        damage = int(damage)
        if damage >= heroes[hero_name][0]:
            print(f"{hero_name} has been killed by {attacker}!")
            heroes.pop(hero_name)
        else:
            heroes[hero_name][0] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")

    elif "Recharge" in command:
        cmd, hero_name, amount = command.split(" - ")
        amount = int(amount)
        max_mana = 200
        recharged_amount = max_mana - heroes[hero_name][1]
        heroes[hero_name][1] += amount
        if heroes[hero_name][1] > max_mana:
            heroes[hero_name][1] = max_mana
            amount = recharged_amount
            print(f"{hero_name} recharged for {amount} MP!")
        else:
            print(f"{hero_name} recharged for {amount} MP!")
    elif "Heal" in command:
        cmd, hero_name, amount_hp = command.split(" - ")
        amount_hp = int(amount_hp)
        max_hp = 100
        recharged_amount_hp = max_hp - heroes[hero_name][0]
        heroes[hero_name][0] += amount_hp
        if heroes[hero_name][0] > max_hp:
            heroes[hero_name][0] = max_hp
            amount_hp = recharged_amount_hp
            print(f"{hero_name} healed for {amount_hp} HP!")
        else:
            print(f"{hero_name} healed for {amount_hp} HP!")
for hero_name, info in heroes.items():
    print(f"{hero_name}")
    print(f"  HP: {info[0]}")
    print(f"  MP: {info[1]}")
