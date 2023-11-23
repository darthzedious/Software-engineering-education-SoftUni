import re
pattern = r"([=|\/])([A-Z][A-Za-z]{2,})\1"
places = input()
travel_points = 0
match = re.findall(pattern, places)
destinations = []
for country in match:
    destinations.append(country[1])
for country in destinations:
    travel_points += len(country)
print(f"Destinations: {', '.join(x for x in destinations)}")
print(f"Travel Points: {travel_points}")
