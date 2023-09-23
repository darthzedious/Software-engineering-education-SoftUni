number_of_orders = int(input())
total_sum = 0
sum = 0
for i in range(number_of_orders):

    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if 0.01 <= capsule_price <= 100 and 1 <= days <= 31 and 1 <= capsules_per_day <= 2000:
        sum = capsules_per_day * days * capsule_price
        print(f'The price for the coffee is: ${sum:.2f}')
    else:
        continue
    total_sum += sum

print(f"Total: ${total_sum:.2f}")
