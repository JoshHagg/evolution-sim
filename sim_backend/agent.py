# agent data
class Agent:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.energy = 50  # temporary MVP energy

    # update logic (random movement for MVP)
    def update(self):
        import random

        # move randomly by -1, 0, or +1
        self.x += random.choice([-1, 0, 1])
        self.y += random.choice([-1, 0, 1])

        # energy drain
        self.energy -= 1
