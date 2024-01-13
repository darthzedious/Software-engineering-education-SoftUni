first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())

for _ in range(int(input())):
    command = input()
    if "Add First" in command:
        for num in command.split():
            if num.isdigit():
                first.add(int(num))
    elif "Add Second" in command:
        for num in command.split():
            if num.isdigit():
                second.add(int(num))
    elif "Remove First" in command:
        for num in command.split():
            if num.isdigit() and int(num) in first:
                first.remove(int(num))
    elif "Remove Second" in command:
        for num in command.split():
            if num.isdigit() and int(num) in second:
                second.remove(int(num))
    elif "Check Subset" in command:
        if first.issubset(second):
            print("True")
        elif second.issubset(first):
            print("True")
        else:
            print("False")
print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")
