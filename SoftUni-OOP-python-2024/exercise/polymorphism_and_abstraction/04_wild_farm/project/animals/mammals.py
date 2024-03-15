from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit


class Mouse(Mammal):

    def make_sound(self):
        return "Squeak"

    @property
    def proper_food(self):
        return [Vegetable, Fruit]

    @property
    def gained_weight(self) -> float:
        return 0.10


class Dog(Mammal):

    def make_sound(self):
        return "Woof!"

    @property
    def proper_food(self):
        return [Meat]

    @property
    def gained_weight(self) -> float:
        return 0.40


class Cat(Mammal):

    def make_sound(self):
        return "Meow"

    @property
    def proper_food(self):
        return [Vegetable, Meat]

    @property
    def gained_weight(self) -> float:
        return 0.30


class Tiger(Mammal):

    def make_sound(self):
        return "ROAR!!!"

    @property
    def proper_food(self):
        return [Meat]

    @property
    def gained_weight(self) -> float:
        return 1.00
