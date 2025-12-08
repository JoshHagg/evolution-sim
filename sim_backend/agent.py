# agent data
class Agent:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.energy = 5000  # temporary MVP energy

    # update logic (random movement for MVP)
    def update(self):
        import random

        dx = random.uniform(-1, 1)
        dy = random.uniform(-1, 1)

        self.x += dx
        self.y += dy


        self.x = max(0, min(self.x, 99))
        self.y = max(0, min(self.y, 99))

        # energy drain
        moveCost = (abs(dx) + abs(dy)) * 0.2
        self.energy -= (1 + moveCost)

