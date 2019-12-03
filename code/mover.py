from mesa import Agent
import random

class Mover(Agent):
    x = None
    y = None
    grid = None
    diagonal = True

    def __init__(self, pos, model, diagonal=True):
        super().__init__(pos, model)
        self.pos = pos
        self.diagonal = diagonal

    def random_move(self):
        next_moves = self.model.grid.get_neighborhood(self.pos, self.diagonal, True)
        next_move = random.choice(next_moves)
        self.model.grid.move_agent(self, next_move)
