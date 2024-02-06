from collections import defaultdict


def forecast(*args):
    country_weather = defaultdict(str)

    for country, weather in args:
        country_weather[country] = weather

    sorted_data = sorted(country_weather.items(), key=lambda x: (-x[1].startswith("S"), -x[1].startswith("C"), -x[1].startswith("R"), x[0]))
    return "\n".join(f'{country} - {weather}' for country, weather in sorted_data)


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
