n = int(input())
collection = set()
for _ in range(n):
    name = input()
    collection.add(name)
print(*collection, sep="\n")