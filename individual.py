import math
import random


class Individual:

    #cities = list of lists where first index is x coordinate and second index is y coordinate
    #solution = list of cities in order of visits (reference by indices)
    def __init__(self, cities):
        self.cities = cities
        self.size = len(cities)
        self.solution = [i for i in range(self.size)]
        random.shuffle(self.solution)
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        total_distance = 0
        for i in range(self.size-1):
            total_distance += self.compute_distance(self.cities[self.solution[i]], self.cities[self.solution[i+1]])
        self.fitness = total_distance
        return total_distance

    def compute_distance(self, a, b):
        return math.dist(a, b)

