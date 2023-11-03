stock = {}
owned_products = input().split()
searched_products = input().split()
for x in range(0, len(owned_products), 2):
    product = owned_products[x]
    quantity = int(owned_products[x + 1])
    stock[product] = quantity

for item in searched_products:
    if item in stock:
        print(f"We have {stock[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
