from mesa import Model
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
import random
from code.agents import Sheep, Wolf, GrassPatch
from code.schedule import RandomActivationByBreed


class WolfSheepPredation(Model):
    verbose = False  
    def __init__(self, height=20, width=20,
                 initial_wolves=40, wolf_reproduce=0.05, wolf_gain_from_food=20,
                 initial_sheep=100, sheep_reproduce=0.04, sheep_gain_from_food=4,
                 grass=True, grass_regrowth_time=30 ):

        self.height = height
        self.width = width
        self.initial_wolves = initial_wolves
        self.wolf_reproduce = wolf_reproduce
        self.wolf_gain_from_food = wolf_gain_from_food
        self.initial_sheep = initial_sheep
        self.sheep_gain_from_food = sheep_gain_from_food
        self.sheep_reproduce = sheep_reproduce
        self.grass = grass
        self.grass_regrowth_time = grass_regrowth_time
        self.schedule = RandomActivationByBreed(self)
        self.grid = MultiGrid(self.height, self.width, torus=True)
        self.datacollector = DataCollector({"Predator": lambda m: m.schedule.get_breed_count(Wolf), "Prey": lambda m: m.schedule.get_breed_count(Sheep)})

        # Wolves
        for i in range(self.initial_wolves):
            x = random.randrange(self.width)
            y = random.randrange(self.height)
            energy = random.randrange(2 * self.wolf_gain_from_food)
            wolf = Wolf((x, y), self, True, energy)
            self.grid.place_agent(wolf, (x, y))
            self.schedule.add(wolf)

        # Sheeps:
        for i in range(self.initial_sheep):
            x = random.randrange(self.width)
            y = random.randrange(self.height)
            energy = random.randrange(2 * self.sheep_gain_from_food)
            sheep = Sheep((x, y), self, True, energy)
            self.grid.place_agent(sheep, (x, y))
            self.schedule.add(sheep)

        # CGreate grass patches
        if self.grass:
            for agent, x, y in self.grid.coord_iter():
                fully_grown = random.choice([True, False])
                if fully_grown:
                    countdown = self.grass_regrowth_time
                else:
                    countdown = random.randrange(self.grass_regrowth_time)
                patch = GrassPatch((x, y), self, fully_grown, countdown)
                self.grid.place_agent(patch, (x, y))
                self.schedule.add(patch)
        self.running = True

    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)
        if self.verbose:
            print([self.schedule.time, self.schedule.get_breed_count(Wolf), self.schedule.get_breed_count(Sheep)])

    def run_model(self, step_count=200):

        if self.verbose:
            print('Initial number of wolves: ', self.schedule.get_breed_count(Wolf))
            print('Initial number of sheeps: ', self.schedule.get_breed_count(Sheep))
        for i in range(step_count):
            self.step()
        if self.verbose:
            print('')
            print('Final number of wolves: ', self.schedule.get_breed_count(Wolf))
            print('Final number of sheep: ', self.schedule.get_breed_count(Sheep))
