class Caretaker:
    def __init__(self, name, specialty=None):
        self.name = name
        self.specialty = specialty
        self.energy = 100
        self.assigned = []

    def assign(self, creature):
        self.assigned.append(creature)
        print(f"{self.name} now cares for {creature.name}")

    def care(self):
        for c in self.assigned:
            action = c.play()  # or feed/rest based on your logic
            self.energy -= 10
            print(f"{self.name} plays with {c.name}: {action}")
