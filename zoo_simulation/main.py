from zoo import Zoo
from animals import Moose, Wolf, Pig
from people import Visitor

# moose = Moose('Helge', 12)
# print(moose)
# moose.make_sound()
# moose.sleep()
# moose.eat()
# moose.special_action()

# wolf = Wolf('Zeke', 5)
# print(wolf)
# wolf.make_sound()
# wolf.sleep()
# wolf.eat()
# wolf.special_action()

# pig = Pig('Piglet', 2)
# print(pig)
# pig.make_sound()
# pig.sleep()
# pig.eat()
# pig.special_action()

# visitor = Visitor('Sara')
# visitor.feed(pig)


animals = [
    Moose("Helge", 12),
    Wolf("Zeke", 5),
    Wolf("Leke", 3),
    Pig("Nasse", 3),
    Pig("Roffe", 1),
    Pig("Nöffe", 1),
]

visitors = [
    Visitor("Sara"),
    Visitor("Elin")
]

zoo = Zoo(animals, visitors)
days = int(input("How many days should the zoo run for? "))
zoo.simulate(days=days)
zoo.print_statistics()


def main():
    animals = [
        Moose("Helge", 12),
        Wolf("Zeke", 5),
        Wolf("Leke", 3),
        Pig("Nasse", 3),
        Pig("Roffe", 1),
        Pig("Nöffe", 1),
    ]

    visitors = [
        Visitor("Sara"),
        Visitor("Elin")
    ]

    zoo = Zoo(animals, visitors)
    days = int(input("How many days should the zoo run for? "))
    zoo.simulate(days=days)
    zoo.print_statistics()


if __name__ == "__main__":
    main()
