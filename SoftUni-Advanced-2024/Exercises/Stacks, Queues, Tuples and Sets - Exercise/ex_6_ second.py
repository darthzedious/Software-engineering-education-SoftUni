from collections import deque
main_colors = deque(input().split())
all_colors = {"red", "yellow", "blue", "orange", "purple", "green"}
secondary_colors = {"orange": {"red", "yellow"},
                   "purple": {"red", "blue"},
                   "green": {"yellow", "blue"},}

new_colors = []
while main_colors:
    first = main_colors.popleft()
    second = main_colors.pop() if main_colors else ""

    for color in (first + second, second + first):
        if color in all_colors:
            new_colors.append(color)
            break
    else:
        for el in (first[:-1], second[:-1]):
            if el:
                main_colors.insert(len(main_colors) // 2, el)


for col in set(secondary_colors.keys()).intersection(new_colors):
    if not secondary_colors[col].issubset(new_colors):
        new_colors.remove(col)
print(new_colors)
