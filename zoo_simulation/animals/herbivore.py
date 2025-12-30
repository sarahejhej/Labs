from .animal import Animal


class Herbivore(Animal):
    category = 'Herbivore'

    PLANT_ENERGY_GAIN = 15

    def eat(self, amount=PLANT_ENERGY_GAIN):
        super().eat(amount)
        print(f"{self.name} is a {self.category.lower()} and eats plants. Energy level is now {self._energy_level}")

    def __str__(self):
        base_string = super().__str__()
        return f'{base_string} and eats plants'
