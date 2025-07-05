

class Sanctuary():
    number_of_sanctuaries = 0
    def __init__(self, name, tagline=None):
        self.creatures = []
        self.name = name
        self.tagline = tagline 
        self.caretakers = []
        Sanctuary.number_of_sanctuaries += 1

    @classmethod
    def get_number_of_sanctuaries(cls):
        return cls.number_of_sanctuaries

    def add_caretaker(self, keeper):
        self.caretakers.append(keeper)

    def add_creature(self, creature):
        self.creatures.append(creature)
        print(f"{creature.name} the {creature.__class__.__name__} has been added to the sanctuary.")

    def feed_all(self, food):
        for c in self.creatures:
            print(c.feed(food))

    def rest_all(self):
        for c in self.creatures:
            print(c.rest())

    def play_all(self):
        for c in self.creatures:
            print(c.play())

    def show_status(self):
        for c in self.creatures:
            print(c)

    def run_day(self):
        print(f"🌞 A new day at {self.name}")
        for c in self.creatures:
            print("→", c.decide_action())
            c.daily_update()
        print()     

