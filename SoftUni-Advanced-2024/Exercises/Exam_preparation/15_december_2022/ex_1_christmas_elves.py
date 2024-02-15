from collections import deque

elf_energy = deque([int(x) for x in input().split()])
number_of_materials = [int(x) for x in input().split()]

elf_turn = 1
santa_bag = 0
used_energy = 0

while elf_energy and number_of_materials:
    elf = elf_energy.popleft()
    material = number_of_materials.pop()

    if elf < 5:
        number_of_materials.append(material)
        continue

    if elf < material:
        number_of_materials.append(material)
        elf *= 2
        elf_energy.append(elf)
        elf_turn += 1
        continue

    if elf_turn % 5 == 0:
        if elf_turn % 3 == 0:
            if elf >= material * 2:
                elf -= material * 2
                used_energy += material * 2
                elf_energy.append(elf)
                elf_turn += 1
                continue
        else:
            if elf >= material:
                elf -= material
                used_energy += material
                elf_energy.append(elf)
                elf_turn += 1
                continue

    if elf_turn % 3 == 0 and elf_turn != 1:
        if elf >= material * 2:
            santa_bag += 2
            elf -= material * 2
            elf += 1
            used_energy += material * 2
            elf_turn += 1
            elf_energy.append(elf)
            continue
        else:
            elf *= 2
            elf_energy.append(elf)
            number_of_materials.append(material)
            elf_turn += 1
            continue

    if elf >= material:
        santa_bag += 1
        elf_turn += 1
        used_energy += material
        elf -= material
        elf += 1
        elf_energy.append(elf)

print(f"Toys: {santa_bag}")
print(f"Energy: {used_energy}")
if elf_energy:
    print(f"Elves left: {', '.join(str(x) for x in elf_energy)}")
if number_of_materials:
    print(f"Boxes left: {', '.join(str(x) for x in number_of_materials)}")
