from zoo import Zoo
from animals import Moose, Wolf, Pig
from people import Visitor

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
