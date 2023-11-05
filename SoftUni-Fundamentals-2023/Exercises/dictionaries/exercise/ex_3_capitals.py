country_names = input().split(", ")
capitals = input().split(", ")
dict = {country_names[index]: capitals[index] for index in range(len(country_names))}
for country, capital in dict.items():
    print(f"{country} -> {capital}")
