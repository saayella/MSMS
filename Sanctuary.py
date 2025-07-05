

class Sanctuary():
    def __init__(self, name, tagline=None):
        self.creatures = []
        self.name = name
        self.tagline = tagline 

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
