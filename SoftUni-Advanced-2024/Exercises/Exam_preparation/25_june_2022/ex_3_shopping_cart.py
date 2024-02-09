
def shopping_cart(*args):
    max_possible_products = {"Soup": 3, "Pizza": 4, "Dessert": 2}
    cart = {"Soup": [], "Pizza": [], "Dessert": []}
    result = []

    for arg in args:
        if arg == "Stop":
            break
        meal = arg[0]
        product = arg[1]
        if len(cart[meal]) < max_possible_products[meal] and product not in cart[meal]:
            cart[meal].append(product)

    for value in cart.values():
        if len(value) > 0:
            break
    else:
        return "No products in the cart!"

    sorted_cart = dict(sorted(cart.items(), key=lambda x: (-len(x[1]), x[0])))

    for meal, value in sorted_cart.items():
        result.append(f'{meal}:')
        for product in sorted(value):
            result.append(f' - {product}')

    return "\n".join(result)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))


