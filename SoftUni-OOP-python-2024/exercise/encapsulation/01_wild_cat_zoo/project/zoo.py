from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals: list[Animal] = []
        self.workers: list[Worker] = []

    def add_animal(self, animal: Animal, price):
        if self.__budget >= price and len(self.animals) < self.__animal_capacity:
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__animal_capacity > len(self.animals) and self.__budget < price:
            return f"Not enough budget"
        return f"Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return f"Not enough space for worker"

    def fire_worker(self, worker_name: Worker):
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        workers_salary = sum(w.salary for w in self.workers)
        if self.__budget >= workers_salary:
            self.__budget -= workers_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animal_money = sum(a.money_for_care for a in self.animals)
        if self.__budget >= animal_money:
            self.__budget -= animal_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        amount_of_lions = len(lions)
        result += f"----- {amount_of_lions} Lions:\n"
        for lion in lions:
            result += f'{lion}\n'

        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        amount_of_tigers = len(tigers)
        result += f"----- {amount_of_tigers} Tigers:\n"
        for tiger in tigers:
            result += f"{tiger}\n"

        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]
        amount_of_cheetahs = len(cheetahs)
        result += f"----- {amount_of_cheetahs} Cheetahs:\n"
        for cheetah in cheetahs:
            result += f"{cheetah}\n"

        return result.strip()

    def workers_status(self):
        result = []

        result.append(f"You have {len(self.workers)} workers")
        keepers = [k for k in self.workers if k.__class__.__name__ == "Keeper"]
        amount_of_keepers = len(keepers)
        result.append(f"----- {amount_of_keepers} Keepers:")
        for keeper in keepers:
            result.append(keeper)

        caretakers = [c for c in self.workers if c.__class__.__name__ == "Caretaker"]
        amount_of_caretakers = len(caretakers)
        result.append(f"----- {amount_of_caretakers} Caretakers:")
        for caretaker in caretakers:
            result.append(caretaker)

        vets = [v for v in self.workers if v.__class__.__name__ == "Vet"]
        amount_of_vetes = len(vets)
        result.append(f"----- {amount_of_vetes} Vets:")
        for vet in vets:
            result.append(vet)

        return "\n".join(str(x) for x in result)

