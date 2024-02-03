from collections import deque, defaultdict

textiles = deque([int(x) for x in input().split(" ")])
medicaments = [int(x) for x in input().split(" ")]

healing_items = {"Patch": 30, "Bandage": 40, "MedKit": 100}
created_items = defaultdict(int)

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()

    combination = textile + medicament

    for key, value in healing_items.items():
        if combination == value:
            created_items[key] += 1

    if combination > 100:
        created_items["MedKit"] += 1
        remaining_res = combination - 100
        medicaments[-1] += remaining_res

    if combination <= 100 and combination not in healing_items.values():
        medicament += 10
        medicaments.append(medicament)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

sorted_items = dict(sorted(created_items.items(), key=lambda x: (-x[1], x)))
print("\n".join(f'{key} - {value}' for key, value in sorted_items.items()))

if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")
if medicaments:
    print(f"Medicaments left: {', '.join(str(x) for x in medicaments[::-1])}")
