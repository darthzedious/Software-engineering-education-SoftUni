def naughty_or_nice_list(santa_list, *args, **kwargs):
    santa_list_two = santa_list.copy()
    nice_list = []
    naughty_list = []
    not_found_list = []

    # Sorting the kids into nice, naughty, and not found lists
    for kid in santa_list:
        if kid[1] in kwargs:
            if santa_list.count(kid) == 1:
                if kwargs[kid[1]] == "Nice":
                    nice_list.append(kid[1])
                    santa_list_two.remove(kid)
                elif kwargs[kid[1]] == "Naughty":
                    naughty_list.append(kid[1])
                    santa_list_two.remove(kid)
        else:
            if santa_list.count(kid) == 1:
                if f"{kid[0]}-Nice" in args:
                    nice_list.append(kid[1])
                    santa_list_two.remove(kid)
                elif f"{kid[0]}-Naughty" in args:
                    naughty_list.append(kid[1])
                    santa_list_two.remove(kid)

    for kid in santa_list_two:
        not_found_list.append(kid[1])

    # Generating the final lists
    result = []
    if nice_list:
        result.append("Nice: " + ", ".join(nice_list))
    if naughty_list:
        result.append("Naughty: " + ", ".join(naughty_list))
    if not_found_list:
        result.append("Not found: " + ", ".join(not_found_list))

    return "\n".join(result)


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
