number_of_cars = int(input())
cars = {}
for i in range(number_of_cars):
    parameters = input()
    car, mileage, fuel = parameters.split("|")
    mileage = int(mileage)
    fuel = int(fuel)
    cars[car] = [mileage, fuel]

while True:
    command = input()
    if command == "Stop":
        break
    if "Drive" in command:
        cmd, car, distance, fuel = command.split(" : ")
        distance = int(distance)
        fuel = int(fuel)
        if cars[car][1] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car][0] += distance
            cars[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[car][0] >= 100000:
                print(f"Time to sell the {car}!")
                cars.pop(car)
    elif "Refuel" in command:
        cmd, car, fuel = command.split(" : ")
        fuel = int(fuel)
        filled_liters = 75 - cars[car][1]
        cars[car][1] += fuel
        if cars[car][1] > 75:
            cars[car][1] = 75
            fuel = filled_liters
        print(f"{car} refueled with {fuel} liters")
    elif "Revert" in command:
        cmd, car, kilometers = command.split(" : ")
        kilometers = int(kilometers)
        cars[car][0] -= kilometers
        if cars[car][0] > 10000:
            print(f"{car} mileage decreased by {kilometers} kilometers")
        if cars[car][0] < 10000:
            cars[car][0] = 10000

for car in cars:
    print(f"{car} -> Mileage: {cars[car][0]} kms, Fuel in the tank: {cars[car][1]} lt.")

