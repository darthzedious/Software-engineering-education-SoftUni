from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):
    def make_sound(self):
        return "Hoot Hoot"

    @property
    def proper_food(self):
        return [Meat]

    @property
    def gained_weight(self) -> float:
        return 0.25


class Hen(Bird):

    def make_sound(self):
        return "Cluck"

    @property
    def proper_food(self):
        return [Meat, Fruit, Vegetable, Seed]

    @property
    def gained_weight(self) -> float:
        return 0.35
    