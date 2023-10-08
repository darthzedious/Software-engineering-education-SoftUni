def total_price(product, price):
    if product == "coffee":
        return 1.50 * price
    elif product == "water":
        return 1.00 * price
    elif product == "coke":
        return 1.40 * price
    elif product == "snacks":
        return 2.00 * price


prod = input()
cost = int(input())
print(f"{total_price(prod, cost):.2f}")
