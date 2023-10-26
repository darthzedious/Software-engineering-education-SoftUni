rout = input().split("||")
starting_fuel = int(input())
starting_ammunition = int(input())

for order in range(len(rout)):
    command = rout[order].split(" ")[0]
    if command == "Travel":
        number = rout[order].split(" ")[1]
        light_years = int(number)
        starting_fuel -= light_years
        if starting_fuel >= 0:
            print(f"The spaceship travelled {light_years} light-years.")
        else:
            print("Mission failed.")
            break
    elif command == "Enemy":
        number = rout[order].split(" ")[1]
        enemy_armor = int(number)
        if starting_ammunition >= enemy_armor:
            starting_ammunition -= enemy_armor
            print(f"An enemy with {enemy_armor} armour is defeated.")
        else:
            starting_fuel -= 2 * enemy_armor
            if starting_fuel > 0:
                print(f"An enemy with {enemy_armor} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break
    elif command == "Repair":
        number = rout[order].split(" ")[1]
        number_of_ammunition_and_fuel = int(number)
        starting_fuel += number_of_ammunition_and_fuel
        starting_ammunition += number_of_ammunition_and_fuel * 2
        print(f"Ammunitions added: {number_of_ammunition_and_fuel * 2}.")
        print(f"Fuel added: {number_of_ammunition_and_fuel}.")
    elif command == "Titan":
        print("You have reached Titan, all passengers are safe.")
