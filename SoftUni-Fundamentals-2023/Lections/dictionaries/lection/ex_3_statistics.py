stock = {}

while True:
    command = input()
    if command == "statistics":
        break

    product, quantity = command.split(":")
    quantity = int(quantity)
    if product in stock:
        stock[product] += quantity
    else:
        stock[product] = quantity

print("Products in stock:")
for product, quantity in stock.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(stock)}")
print(f"Total Quantity: {sum(stock.values())}")
