collection_of_items = input().split("|")
train_ticket = 150
profit = 0
budget = float(input())
new_prices = []
for items in collection_of_items:
    item, price = items.split("->")
    price = float(price)
    valid_price = False
    if item == "Clothes":
        if price <= 50.00:
            valid_price = True
    elif item == "Shoes":
        if price <= 35.00:
            valid_price = True
    elif item == "Accessories" and price <= 20.50:
        valid_price = True
    if valid_price:
        if budget >= price:
            budget -= price
            new_prices.append(price * 1.4)
            profit += price * 1.4 - price

final_budget = budget + sum(list(new_prices))
print(" ".join([f"{prices:.2f}" for prices in new_prices]))
print(f"Profit: {profit:.2f}")
if final_budget >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")
#Clothes->43.30|Shoes->25.25|Clothes->36.52|Clothes->20.90|Accessories->15.60
#Shoes->41.20|Clothes->20.30|Accessories->40|Shoes->15.60|Shoes->33.30|Clothes->48.60