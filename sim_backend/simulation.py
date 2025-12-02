from world import World

# simulation control
class Simulation:
    def __init__(self):
        self.world = World()

    # one tick of the sim
    def tick(self):
        self.world.update()
        return self.world.to_dict()
