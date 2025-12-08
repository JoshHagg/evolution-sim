# agent data
class Agent:
    def __init__(self, id, x, y, moveSpeed = None, senseRange = None, metabolism = None, colour = None):
        import random
        self.id = id
        self.x = float(x)
        self.y = float(y)

        self.moveSpeed = moveSpeed if moveSpeed is not None else 1.0 + random.uniform(-0.1, 0.1)
        self.senseRange = senseRange if senseRange is not None else 2.0 + random.uniform(-0.1, 0.1)
        self.metabolism = metabolism if metabolism is not None else 1.0 + random.uniform(-0.1, 0.1)

        self.colour = colour if colour is not None else random.randint(0x00AA00, 0x00FF00)

        self.energy = 5000  

    # update logic (random movement for MVP)
    def update(self):
        import random

        dx = random.uniform(-1, 1) * self.moveSpeed
        dy = random.uniform(-1, 1) * self.moveSpeed

        self.x += dx
        self.y += dy


        self.x = max(0, min(self.x, 99))
        self.y = max(0, min(self.y, 99))

        # energy drain
        moveCost = (abs(dx) + abs(dy)) * self.metabolism
        self.energy -= (1 + moveCost)

