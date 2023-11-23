n = int(input())
plants = {}

for plant in range(n):
    plant_info = input()
    plant_type, rarity = plant_info.split("<->")
    rarity = int(rarity)
    plants[plant_type] = {"rarity": rarity, "ratings": []}

while True:
    command = input()
    if command == "Exhibition":
        break
    if "Rate" in command:
        cmd, info = command.split(": ")
        plant_type, rating = info.split(" - ")
        rating = int(rating)
        if plant_type in plants.keys():
            plants[plant_type]["ratings"].append(rating)
        else:
            print("error")
    elif "Update" in command:
        cmd, info = command.split(": ")
        plant_name, rarity = info.split(" - ")
        if plant_name in plants.keys():
            plants[plant_name]["rarity"] = rarity
        else:
            print("error")
    elif "Reset" in command:
        cmd, plant_name = command.split(": ")
        if plant_name in plants.keys():
            plants[plant_name]["ratings"] = []
        else:
            print("error")

print("Plants for the exhibition:")
for plant, info in plants.items():
    plant_rarity = info["rarity"]
    plant_rating = info["ratings"]
    average_sum = sum(plant_rating) / len(plant_rating) if plant_rating else 0
    print(f"- {plant}; Rarity: {plant_rarity}; Rating: {average_sum:.2f}")
