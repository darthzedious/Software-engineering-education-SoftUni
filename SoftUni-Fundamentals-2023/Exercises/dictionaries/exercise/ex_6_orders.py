products = {}
while True:
    product_order = input()
    if product_order == "buy":
        for key, value in products.items():
            print(f"{key} -> {(value[0] * value[1]):.2f}")
        break
    name, price, quantity = product_order.split()
    price = float(price)
    quantity = int(quantity)

    if name not in products.keys():
        products[name] = []
        products[name].append(price)
        products[name].append(quantity)
    else:
        products[name][1] += quantity
        products[name][0] = price

