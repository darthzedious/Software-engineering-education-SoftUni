class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}  # represent skill and its mp cost
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills.keys():
            return f"Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        skills_info = "\n".join(f"==={skill} - {mana}" for skill, mana in self.skills.items())
        return f"Name: {self.name}\n"\
               f"Guild: {self.guild}\n"\
               f"HP: {self.hp}\n"\
               f"MP: {self.mp}\n"\
               f"{skills_info}"
