sublists = input().split("|")
final = []
for x in sublists[::-1]:
    final.extend(x.split())

print(*final)
