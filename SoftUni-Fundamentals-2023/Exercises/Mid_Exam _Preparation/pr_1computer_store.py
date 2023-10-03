price_without_tax = 0
total_price = 0

while True:
    command = input()
    valid_command = True
    if command == "special" or command == "regular":
        break
    if float(command) < 0:
        valid_command = False
        print("Invalid price!")
    if valid_command:
        price_without_tax += float(command)

taxes = price_without_tax * 0.2
special_discount = (price_without_tax + taxes) * 0.1
if command == "special":
    total_price = (price_without_tax + taxes) - special_discount
elif command == "regular":
    total_price =(price_without_tax + taxes)
if total_price == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_tax:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")
