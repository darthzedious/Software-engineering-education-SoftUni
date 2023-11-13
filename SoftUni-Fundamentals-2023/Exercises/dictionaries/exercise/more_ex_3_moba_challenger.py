player_info = {}
while True:
    info = input()
    if info == "Season end":
        break
    if "->" in info:
        player, position, skill = info.split(" -> ")
        skill = int(skill)
        if player not in player_info.keys():
            player_info[player] = {position: skill}
        elif position not in player_info[player].keys():
            player_info[player][position] = skill
        elif skill > player_info[player][position]:
            player_info[player][position] = skill
    elif "vs" in info:
        player_one, player_two = info.split(" vs ")
        if player_one in player_info.keys() and player_two in player_info.keys():
            for position in player_info[player_one].keys():
                for pos in player_info[player_two].keys():
                    if position == pos:
                        total_skill_points_player_one = sum(player_info[player_one].values())
                        total_skill_points_player_two = sum(player_info[player_two].values())
                        if total_skill_points_player_one > total_skill_points_player_two:
                            player_info.pop(player_two)
                        elif total_skill_points_player_one < total_skill_points_player_two:
                            player_info.pop(player_one)

sorted_skills = dict(sorted(player_info.items(), key=lambda x: (-sum(x[1].values()), x[0])))

for player, info in sorted_skills.items():
    print(f"{player}: {sum(info.values())} skill")
    sorted_names = dict(sorted(info.items(), key=lambda x: (-x[1], x[0])))
    for position, skill in sorted_names.items():
        print(f"- {position} <::> {skill}")
