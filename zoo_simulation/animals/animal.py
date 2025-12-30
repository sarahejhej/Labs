class Animal:
    category = 'Animal'
    DEFAULT_ENERGY = 100
    MAX_ENERGY = 100
    MIN_ENERGY = 20

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._energy_level = self.DEFAULT_ENERGY
        self.is_alive = True

    def _change_energy(self, amount):
        if not self.is_alive:
            return

        self._energy_level = max(
            0, min(self.MAX_ENERGY, self._energy_level + amount))

        if self._energy_level <= 0:
            self.is_alive = False
            print(f"{self.name} has no energy left and is now dead.")

    def eat(self, amount):
        if self.is_alive:
            self._change_energy(amount)

    def sleep(self):
        if not self.is_alive:
            return

        self._energy_level = self.DEFAULT_ENERGY
        print(
            f'{self.name} sleeps and fully recovers. Energy level is now {self._energy_level}')

    def make_sound(self, sound='...'):
        if not self.is_alive:
            return

        print(f'{self.name} says {sound}')

    def special_action(self):
        raise NotImplementedError(
            "Subclasses must implement special_action() method.")

    def act(self, all_animals=None):
        if not self.is_alive:
            return

        if self._energy_level < self.MIN_ENERGY:
            self.sleep()
        else:
            self.special_action(all_animals)

    def __str__(self):
        species = self.__class__.__name__
        return f'{self.name} the {species} is a {self.category.lower()}'
