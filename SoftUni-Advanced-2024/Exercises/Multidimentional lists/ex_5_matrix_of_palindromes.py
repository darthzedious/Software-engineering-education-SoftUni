rows, cols = [int(x) for x in input().split()]

char = ord("a")

for r in range(char, char + rows):
    for c in range(r, r + cols):
        print(f"{chr(r)}{chr(c)}{chr(r)}", end=" ")

    print()
