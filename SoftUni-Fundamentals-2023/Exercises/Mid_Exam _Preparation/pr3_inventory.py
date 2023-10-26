journal = input().split(", ")
command = input()
while command != "Craft!":
    order, item = (command.split(" - "))
    if order == "Collect":
        if item not in journal:
            journal.append(item)
    elif order == "Drop":
        if item in journal:
            journal.remove(item)
    elif order == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in journal:
            journal.insert(journal.index(old_item) + 1, new_item)
    elif order == "Renew":
        if item in journal:
            journal.remove(item)
            journal.append(item)
    command = input()
print(", ".join(journal))
