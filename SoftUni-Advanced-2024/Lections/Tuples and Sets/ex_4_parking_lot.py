n = int(input())
parking_lot = set()
for _ in range(n):
    direction, number = input().split(", ")
    if direction == "IN":
        parking_lot.add(number)
    else:
        parking_lot.remove(number)
if not parking_lot:
    print("Parking Lot is Empty")
else:
    for car in parking_lot:
        print(car)
