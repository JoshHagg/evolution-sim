# agent data
class Agent:
    def __init__(self, id, x, y, moveSpeed = None, senseRange = None, metabolism = None, colour = None):
        import random
        self.id = id
        self.x = float(x)
        self.y = float(y)
        self.direction = random.uniform(0, 6.28)   # radians

        self.moveSpeed = moveSpeed if moveSpeed is not None else 0.2 + random.uniform(-0.05, 0.05)
        self.senseRange = senseRange if senseRange is not None else 2.0 + random.uniform(-0.1, 0.1)
        self.metabolism = metabolism if metabolism is not None else 1.0 + random.uniform(-0.1, 0.1)

        self.colour = colour if colour is not None else random.randint(0x00AA00, 0x00FF00)

        self.energy = 2000  

    # update logic (random movement for MVP)
    def update(self):
        import random
        import math 

        # slight steering noise instead of full randomness
        turnAmount = random.uniform(-0.2, 0.2)   # how sharply they can turn
        self.direction += turnAmount

        # movement is based on direction
        dx = math.cos(self.direction) * self.moveSpeed
        dy = math.sin(self.direction) * self.moveSpeed

        self.x += dx
        self.y += dy


        self.x = max(0, min(self.x, 99))
        self.y = max(0, min(self.y, 99))

        # energy drain
        moveCost = (abs(dx) + abs(dy)) * self.metabolism
        self.energy -= (1 + moveCost)

