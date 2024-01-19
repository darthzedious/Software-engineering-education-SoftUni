from collections import deque

materials = deque(int(x) for x in input().split())
magic = deque(int(x) for x in input().split())

presents = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
collection = []

while materials and magic:
    current_box = materials.pop()
    current_magic = magic.popleft()

    magic_level = current_box * current_magic

    if magic_level in presents.keys():
        present = presents[magic_level]
        collection.append(present)

    elif magic_level < 0:
        new_value = current_box + current_magic
        materials.append(new_value)

    elif magic_level not in presents and magic_level > 0:
        current_box += 15
        materials.append(current_box)
    else:
        if current_box != 0:
            materials.append(current_box)
        if current_magic != 0:
            magic.appendleft(current_magic)

if {"Doll", "Wooden train"}.issubset(collection) or {"Teddy bear", "Bicycle"}.issubset(collection):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    materials = list(reversed(materials))
    print("Materials left: ", end="")
    print(*materials, sep=", ")
if magic:
    print("Magic left: ", end="")
    print(*magic, sep=", ")

for toy in sorted(set(collection)):
    print(f"{toy}: {collection.count(toy)}")
