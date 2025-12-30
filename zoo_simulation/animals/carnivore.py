import random
from .animal import Animal


class Carnivore(Animal):
    category = 'Carnivore'

    MEAT_ENERGY_GAIN = 30
    HUNT_ENERGY_COST = 10
    MIN_ENERGY_TO_HUNT = 20
    HUNT_SUCCESS_CHANCE = 0.6
    MIN_PREY_COUNT = 2
    PREY_ENERGY_LOSS = 85

    def eat(self, amount=MEAT_ENERGY_GAIN):
        super().eat(amount)
        print(
            f"{self.name} is a {self.category.lower()} and eats meat. Energy level is now {self._energy_level}")

    def select_prey(self, animals):
        possible_prey = []

        for animal in animals:
            if animal is self:
                continue

            if animal.category != 'Herbivore':
                continue

            if not animal.is_alive:
                continue

            possible_prey.append(animal)

        if len(possible_prey) < self.MIN_PREY_COUNT:
            print(f"Not enough prey available for {self.name} to hunt.")
            return None

        if not possible_prey:
            print(f"No prey available for {self.name} to hunt.")
            return None

        return random.choice(possible_prey)

    def hunt(self, prey):
        if self._energy_level < self.MIN_ENERGY_TO_HUNT:
            print(f"{self.name} is too tired to hunt.")
            return False

        if not prey.is_alive:
            print(f"{prey.name} is already dead.")
            return

        self._change_energy(-self.HUNT_ENERGY_COST)

        if random.random() > self.HUNT_SUCCESS_CHANCE:
            print(f"{self.name} failed to catch {prey.__class__.__name__.lower()}.")
            return False

        print(f"{self.name} successfully hunts {prey.__class__.__name__.lower()}.")

        prey._change_energy(-self.PREY_ENERGY_LOSS)

        if not prey.is_alive:
            print(f"{prey.name} has died from the hunt!")

        self.eat()

        return True

    def __str__(self):
        base_string = super().__str__()
        return f'{base_string} and eats meat'
