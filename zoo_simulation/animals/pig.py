import random
from .herbivore import Herbivore


class Pig(Herbivore):
    PLAY_ENERGY_COST = 5
    PLAY_CHANCE = 0.5

    def make_sound(self):
        super().make_sound('"Oink!"')

    def eat(self):
        """
        Pig eat method: pigs dig in the soil for roots.
        """
        super().eat()
        print(f"{self.name} digs in the soil for roots.")

    def roll_in_mud(self):
        """
        Roll in mud method: checks if self has enough energy to play. Reduces energy levels accordingly.
        """
        if self._energy_level < self.PLAY_ENERGY_COST:
            print(f"{self.name} is too tired to roll in the mud.")
            return

        self._change_energy(-self.PLAY_ENERGY_COST)
        print(
            f"{self.name} rolls in the mud! Energy level is now {self._energy_level}")

    def select_playmate(self, animals):
        """
        Selects a random playmate from the list of animals.
        """
        possible_mates = []

        for animal in animals:
            if animal is self:
                continue

            if not isinstance(animal, Pig):
                continue

            if not animal.is_alive:
                continue

            if animal._energy_level < self.PLAY_ENERGY_COST:
                continue

            possible_mates.append(animal)

        if not possible_mates:
            return None

        return random.choice(possible_mates)

    def play(self, play_mate):
        """
        Play method: checks if self and play_mate have enough energy to play. Reduces energy levels accordingly.
        """
        if self._energy_level < self.PLAY_ENERGY_COST:
            print(f"{self.name} is too tired to play.")
            return

        self._change_energy(-self.PLAY_ENERGY_COST)
        play_mate._change_energy(-self.PLAY_ENERGY_COST)

        print(
            f"{self.name} plays with {play_mate.name}! Both pigs' energy levels decrease by {self.PLAY_ENERGY_COST}.")

    def special_action(self, animals):
        """
        Pig special action: randomly plays, otherwise performs species special action (roll_in_mud()).
        """
        if random.random() < self.PLAY_CHANCE:
            play_mate = self.select_playmate(animals)

            if not play_mate:
                print(f"No playmate available for {self.name} to play.")
            else:
                self.play(play_mate)
                return

        self.roll_in_mud()
