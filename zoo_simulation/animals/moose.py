from .herbivore import Herbivore


class Moose(Herbivore):
    SWIM_ENERGY_COST = 5

    def make_sound(self):
        super().make_sound('"Mooo!"')

    def eat(self):
        super().eat()
        print(f"{self.name} eats leaves and twigs from trees.")

    def special_action(self, all_animals):
        self._change_energy(-self.SWIM_ENERGY_COST)
        print(
            f"{self.name} swims across the river!. Energy level is now {self._energy_level}")
