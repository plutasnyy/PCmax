from time import time
from random import shuffle
from copy import deepcopy
from greedy import greedy
class GeneticAlghoritm(object):
    def __init__(self, data, population_size, time_limit):
        self.data = data
        self.population_size = population_size
        self.time_limit = time_limit

    def generate_random_population(self):
        population = []
        copy_data = deepcopy(self.data)
        for i in range(self.population_size):
            shuffle(copy_data)
            population.append(deepcopy(copy_data))
        return population


    def fitness(self):
        

    def start(self):
        start_time = time()

        population = self.generate_random_population()

        while time() - start_time < self.time_limit:
            for i in range(len(population)):
                genotype = population[i]
                population[i] = self.fitness(genotype)