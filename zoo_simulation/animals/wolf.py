import random
from .carnivore import Carnivore


class Wolf(Carnivore):
    HUNT_CHANCE = 0.4

    def make_sound(self):
        super().make_sound('"Howl!"')

    def eat(self):
        super().eat()
        print(f"{self.name} hunts in a pack.")

    def howl(self):
        self._change_energy(-10)
        print(f"{self.name} howls at the moon!")

    def special_action(self, animals):
        """
        Wolf special action: randomly hunts, otherwise performs species special action (howls).
        """
        if random.random() < self.HUNT_CHANCE:
            prey = self.select_prey(animals)
            if prey and self.hunt(prey):
                return

        self.howl()
