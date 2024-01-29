def team_lineup(*args):
    country_data = {}
    final_data = []

    for info in args:
        player, country = info

        if country not in country_data.keys():
            country_data[country] = []
        country_data[country].append(player)

    sorted_country_data = dict(sorted(country_data.items(), key=lambda x: (-len(x[1]), x[0])))

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

print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))

