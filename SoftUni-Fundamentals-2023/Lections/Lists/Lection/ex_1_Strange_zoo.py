lst = []

for _ in range(3):
    body_part = input()
    lst.append(body_part)

lst[0], lst[2] = lst[2], lst[0]
print(lst)
