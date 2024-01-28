def sorting_cheeses(**kwargs):
    final = ""
    sorted_result = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    for name, quantity in sorted_result:
        final += f"{name}" + "\n"
        for number in sorted(quantity, reverse=True):
            final += f"{number}\n"
    return final


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
