
class Visitor:
    def __init__(self, name):
        self.name = name

    def feed(self, animal):
        if not animal.is_alive:
            return

        print(f"{self.name} feeds {animal.name}.")
        animal.eat()
