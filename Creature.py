class Creature():
    number_of_creatures = 0

    def __init__(self,name,age=None):
        self.name = name
        self.health = 85
        self.happiness = 75
        self.hunger = 20
        self.energy = 80
        self.age = age
        Creature.number_of_creatures += 1

    def feed(self, food):
        food_value = food_dictionary.get(food, 0)
        self.hunger = max(self.hunger - food_value, 0)
        return f"{self.name} has been fed {food}. Hunger level is now {self.hunger}."
    def rest(self, hours=3):
        self.energy = min(self.energy + hours*7, 100)
        return f"{self.name} has rested. Energy level is now {self.energy}."
    def play(self, duration=1):
        self.happiness = min(self.happiness + duration*10, 100)
        self.energy = max(self.energy - duration*5, 0)
        return f"{self.name} has played for {duration} hour(s). Happiness is now {self.happiness}, energy is {self.energy}."
    def __str__(self):
        return f"Creature(name={self.name}, age={self.age}, health={self.health}, happiness={self.happiness}, hunger={self.hunger}, energy={self.energy})"
    def speak(self):
        return f"{self.name} says: Hello!"
    def daily_update(self):
        self.hunger = min(self.hunger + 20, 100)
        self.energy = max(self.energy - 20, 0)
        self.happiness = max(self.happiness - 15, 0)


class Dragon(Creature):
    def breathe_fire(self):
        return f"{self.name} breathes fire!"

class Unicorn(Creature):
    def rainbow(self):
        return f"{self.name} creates a rainbow!"

class Phoenix(Creature):
    def rise_from_ashes(self):
        return f"{self.name} rises from the ashes!"

class Griffin(Creature):
    def fly(self):
        return f"{self.name} flies majestically!"

class Mermaid(Creature):
    def swim(self):
        return f"{self.name} swims gracefully!"

class Centaur(Creature):
    def gallop(self):
        return f"{self.name} gallops through the forest!"

class Werewolf(Creature):
    def howl(self):
        return f"{self.name} howls at the moon!"
    
class Hydra(Creature):
    def regenerate(self):
        return f"{self.name} regenerates its heads!"

food_dictionary = {
    "meat": 30, "fish": 20, "vegetables": 10, "fruits": 5, "grains": 2
}

Rob = Dragon("Rob", 5)
Fiona = Unicorn("Fiona", 3)
Charlie = Phoenix("Charlie", 2)
Gryphon = Griffin("Gryphon", 4)
Merlin = Mermaid("Merlin", 6)
print(Fiona.__str__())
print(Rob.play(2))
print(Charlie.rise_from_ashes())
print(Charlie.__str__())
print(Fiona.feed("fruits"))
print(Rob.breathe_fire())
print(Fiona.__str__())