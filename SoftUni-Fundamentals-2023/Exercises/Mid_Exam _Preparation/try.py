stock = {}
owned_products = input().split()

for x in range(0, len(owned_products) - 1, 2):
    product = owned_products[x]
    quantity = int(owned_products[x + 1])
    stock[product] = quantity

print(stock)