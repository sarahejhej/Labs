import random


class Zoo:
    def __init__(self, animals, visitors):
        self.animals = animals
        self.visitors = visitors
        self.current_hour = 8

        self.schedule = {
            9: self.morning_routine,
            12: self.lunchtime,
            15: self.interactions,
            18: self.evening_routine
        }

        self.statistics = {
            'days_simulated': 0,
            'animals_alive': [],
            'deaths': 0,
            'total_animals': len(animals),
            'total_visitors': len(visitors),
            'animal_energy_levels': []
        }

    def morning_routine(self):
        print("Morning routine: Animals are waking up and being fed.")
        for animal in self.animals:
            animal.make_sound()
            animal.eat()

    def lunchtime(self):
        print("Lunchtime: Visitors are feeding the animals.")
        for visitor in self.visitors:
            animal = random.choice(self.animals)
            if animal.is_alive:
                visitor.feed(animal)

    def interactions(self):
        print("Afternoon interactions: Visitors are interacting with animals.")
        for visitor in self.visitors:
            for animal in self.animals:
                print(
                    f"{visitor.name} is watching {animal.name}.")
                animal.act(self.animals)

    def evening_routine(self):
        print("Evening routine: Animals are settling down for the night.")
        for animal in self.animals:
            animal.sleep()

    def collect_statistics(self):
        alive = [animal for animal in self.animals if animal.is_alive]
        self.statistics['animals_alive'] = len(alive)
        self.statistics['deaths'] = self.statistics['total_animals'] - \
            len(alive)
        self.statistics['animal_energy_levels'] = {
            animal.name: animal._energy_level for animal in alive}
        self.statistics['days_simulated'] += 1

        print(f"Days Simulated: {self.statistics['days_simulated']}")

    def run_hour(self):
        action = self.schedule.get(self.current_hour)
        if action:
            action()

    def simulate_day(self):
        print(f"The zoo opens its gates. It's {self.current_hour} o'clock.")

        for hour in range(8, 20):
            self.current_hour = hour
            print(f"\nTime: {hour}:00")

            self.run_hour()

        self.collect_statistics()
        print("The zoo is closing for the day.")

    def simulate(self, days):
        for day in range(1, days + 1):
            print(f"--- Day {day} ---")
            self.simulate_day()

            self.statistics['days_simulated'] = day

    def print_statistics(self):
        print("\n--- Zoo Statistics ---")
        for key, value in self.statistics.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
