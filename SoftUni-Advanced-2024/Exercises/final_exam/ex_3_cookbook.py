def cookbook(*recipes):
    cuisines = {}

    # Group recipes by cuisine
    for recipe in recipes:
        name, cuisine, ingredients = recipe
        if cuisine not in cuisines:
            cuisines[cuisine] = []
        cuisines[cuisine].append((name, ingredients))

    # Sort cuisines by number of recipes (descending), then alphabetically
    sorted_cuisines = sorted(cuisines.items(), key=lambda x: (-len(x[1]), x[0]))

    output = []
    for cuisine, recipes in sorted_cuisines:
        output.append(f"{cuisine} cuisine contains {len(recipes)} recipes:")
        for recipe in sorted(recipes):
            recipe_name, ingredients = recipe
            output.append(f"  * {recipe_name} -> Ingredients: {', '.join(ingredients)}")

    return "\n".join(output)


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
print()

print(cookbook(
    ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
    ))

print()
print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))
