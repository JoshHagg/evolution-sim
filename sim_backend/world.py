from agent import Agent
import random

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

    # one simulation tick
    def update(self):
        for agent in self.agents:
            agent.update()

        # remove dead agents
        self.agents = [a for a in self.agents if a.energy > 0]

    # convert world to JSON-friendly dict
    def to_dict(self):
        return {
            "agents": [
                {"id": a.id, "x": a.x, "y": a.y, "energy": a.energy}
                for a in self.agents
            ]
        }
