lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_helmet_broken = lost_fights_count // 2
total_swords_broken = lost_fights_count // 3
total_shields_broken = lost_fights_count // (2*3)
total_armor_broken = total_shields_broken // 2

final_price = helmet_price * total_helmet_broken\
              + sword_price * total_swords_broken\
              + shield_price * total_shields_broken\
              + armor_price * total_armor_broken
print(f'Gladiator expenses: {final_price:.2f} aureus')
