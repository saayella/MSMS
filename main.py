from Sanctuary import Sanctuary
from Creature import *
from Caretaker import Caretaker

# 1. Create sanctuary
s = Sanctuary("Wilson Sanctuary", "Magic lives here")

# 2. Add creatures
rob   = Dragon("Rob", age=5)
fiona = Unicorn("Fiona", age=3)
s.add_creature(rob)
s.add_creature(fiona)

# 3. Add a caretaker
alice = Caretaker("Alice", specialty="Unicorn")
s.add_caretaker(alice)
alice.assign(fiona)

# 4. Run a few days
for day in range(1, 4):
    s.run_day()
    s.show_status()
