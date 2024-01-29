from collections import defaultdict


def team_lineup(*args):
    country_data = defaultdict(list)

    for player, country in args:
        country_data[country].append(player)

    sorted_country_data = dict(sorted(country_data.items(), key=lambda x: (-len(x[1]), x[0])))

    final_data = []

    for country, players in sorted_country_data.items():
        final_data.append(f"{country}:")
        for player in players:
            final_data.append(f"  -{player}")

    return "\n".join(final_data)


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))
