cities = {}
while True:
    command = input()
    if command == "Sail":
        break
    city, population, gold = command.split("||")
    population, gold = int(population), int(gold)
    if city not in cities.keys():
        cities[city] = [population, gold]
    else:
        cities[city][0] += population
        cities[city][1] += gold
while True:
    command = input()
    if command == "End":
        break
    if "Plunder" in command:
        cmd, city, people, gold = command.split("=>")
        people, gold = int(people), int(gold)
        cities[city][0] -= people
        cities[city][1] -= gold
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[city][0] <= 0 or cities[city][1] <= 0:
            print(f"{city} has been wiped off the map!")
            cities.pop(city)
    elif "Prosper" in command:
        cmd, city, gold = command.split("=>")
        if "-" in gold:
            print("Gold added cannot be a negative number!")
        else:
            gold = int(gold)
            cities[city][1] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city][1]} gold.")

if len(cities) > 0:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, info in cities.items():
        print(f"{city} -> Population: {info[0]} citizens, Gold: {info[1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
