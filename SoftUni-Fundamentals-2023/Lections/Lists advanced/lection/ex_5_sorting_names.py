names = input().split(", ")
sorted_names = list(sorted(names, key=lambda x: (-len(x), x)))
print(sorted_names)
