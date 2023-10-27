class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
            self.__animals += 1
        elif species == "fish":
            self.fishes.append(name)
            self.__animals += 1
        elif species == "bird":
            self.birds.append(name)
            self.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\nTotal animals: {self.__animals}"
        elif species == "fish":
            return f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\nTotal animals: {self.__animals}"
        elif species == "bird":
            return f"Birds in {self.zoo_name}: {', '.join(self.birds)}\nTotal animals: {self.__animals}"


name_of_the_zoo = input()
n = int(input())
zoo = Zoo(name_of_the_zoo)
for animals in range(n):
    animal = input()
    species, name = animal.split()
    zoo.add_animal(species, name)
info_for_current_species = input()
print(zoo.get_info(info_for_current_species))
