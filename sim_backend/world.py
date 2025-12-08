from agent import Agent
import random

foodEnergy = 2000   # MVP value, tweak later
targetFood = 20  # MVP value, tweak later

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
        self.spawnFood(20)

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

        newAgents = []
        for agent in self.agents:
            reproductionThreshold = 7000

            if agent.energy > reproductionThreshold:
                agent.energy /= 2  # parent keeps half

                # mutation helper
                def mutate(value, amount=0.1):
                    import random
                    return max(0.1, value + random.uniform(-amount, amount))

                child = Agent(
                    id=len(self.agents) + len(newAgents),
                    x=agent.x + random.uniform(-1, 1),
                    y=agent.y + random.uniform(-1, 1),
                    moveSpeed=mutate(agent.moveSpeed),
                    senseRange=mutate(agent.senseRange),
                    metabolism=mutate(agent.metabolism),
                    colour=agent.colour  # or mutate color later
                )

                child.energy = agent.energy  # child inherits the other half
                newAgents.append(child)

        # add children
        self.agents.extend(newAgents)


        # remove dead agents
        self.agents = [a for a in self.agents if a.energy > 0]

        #Spawn food if none exists
        if len(self.food)< targetFood:
            missing = targetFood - len(self.food)
            for _ in range(missing):
                self.food.append({
                    "id": len(self.food),
                    "x": random.uniform(0, self.width),
                    "y": random.uniform(0, self.height)
                })


    # convert world to JSON-friendly dict
    def to_dict(self):
        return {
            "agents": [
                {"id": a.id, "x": a.x, "y": a.y, "energy": a.energy, "colour": a.colour}
                for a in self.agents
            ],
            "food": self.food 
        }
