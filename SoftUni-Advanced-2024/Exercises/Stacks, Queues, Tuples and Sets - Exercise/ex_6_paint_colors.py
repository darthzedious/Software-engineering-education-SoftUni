from collections import deque
main_colors = deque(input().split())
all_colors = ["red", "yellow", "blue", "orange", "purple", "green"]
secondary_colors = {"orange": ["red", "yellow"],
                   "purple": ["red", "blue"],
                   "green": ["yellow", "blue"],
}
new_colors = []
while main_colors:
    if len(main_colors) > 1:
        first = main_colors.popleft()
        second = main_colors.pop() if main_colors else ""

        if (first + second) in all_colors:
            new_colors.append(first + second)
        elif (second + first) in all_colors:
            new_colors.append(second + first)
        else:
            main_colors.insert(len(main_colors) // 2, first[:-1])
            main_colors.insert(len(main_colors) // 2, second[:-1])

    elif len(main_colors) == 1:
        color = main_colors.pop()
        if color in all_colors:
            new_colors.append(color)

for key, value in secondary_colors.items():
    if key in new_colors:
        for color in secondary_colors[key]:
            if color not in new_colors:
                new_colors.remove(key)
print(new_colors)
