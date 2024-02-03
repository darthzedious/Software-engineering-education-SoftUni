def shop_from_grocery_list(budget: int, products: list, *args):
    for product, price in args:
        if product in products:
            if (budget - float(price)) < 0:
                break
            else:
                products.remove(product)
                budget -= float(price)
        else:
            continue

    if not products:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(str(x) for x in products)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
