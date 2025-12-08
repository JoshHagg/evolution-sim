from agent import Agent
import random

foodEnergy = 30   # MVP value, tweak later

# world data + simulation management
class World:
    def __init__(self, width=100, height=100, agent_count=10):
        self.width = width
        self.height = height

        # create initial agents
        self.agents = [
            Agent(id=i, x=random.randint(0, width), y=random.randint(0, height))
            for i in range(agent_count)
        ]
        self.food = []

    def spawnFood(self, amount=20):
        self.food = [
            {"id": i,
             "x": random.uniform(0, self.width),
             "y": random.uniform(0, self.height)}
             for i in range(amount)
    ]
    # one simulation tick
    def update(self):
        for agent in self.agents:
            agent.update()

           # ---- EATING LOGIC ----
        eatRange = 2.0
        remainingFood = []

        for food in self.food:
            eaten = False
            fx, fy = food["x"], food["y"]

            for agent in self.agents:
                dx = agent.x - fx
                dy = agent.y - fy

                if dx*dx + dy*dy <= eatRange * eatRange:
                    # Agent eats this food
                    agent.energy += foodEnergy
                    eaten = True
                    break

            if not eaten:
                remainingFood.append(food)

        # update food list
        self.food = remainingFood


        # remove dead agents
        self.agents = [a for a in self.agents if a.energy > 0]

        #Spawn food if none exists
        if len(self.food) == 0:
            self.spawnFood()


    # convert world to JSON-friendly dict
    def to_dict(self):
        return {
            "agents": [
                {"id": a.id, "x": a.x, "y": a.y, "energy": a.energy}
                for a in self.agents
            ],
            "food": self.food 
        }
