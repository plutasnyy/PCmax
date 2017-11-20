from time import time
from random import shuffle
from copy import deepcopy
from greedy import greedy


class GeneticAlghoritm(object):
    def __init__(self, data, population_size, time_limit):
        self.number_of_processors, self.number_of_exercises, self.data = data
        self.population_size = population_size
        self.time_limit = time_limit
        self.optimum = sum(self.data)/self.number_of_processors

    def generate_random_population(self):
        population = []
        copy_data = deepcopy(self.data)
        for i in range(self.population_size):
            shuffle(copy_data)
            population.append(deepcopy(copy_data))
        return population

    def fitness(self, genotype):
        proc_array = greedy([self.number_of_processors,self.number_of_exercises,genotype])
        fitness = 0
        max_time = 0
        for proc in proc_array:
            if proc.time > max_time:
                max_time = proc.time
            fitness += abs(self.optimum - proc.time)

        if max_time < self.optimum:
            raise ValueError

        fitness += max_time - self.optimum
        return (genotype,round(fitness,2))

    def start(self):
        start_time = time()

        population = self.generate_random_population()
        while time() - start_time < self.time_limit:
            for i in range(len(population)):
                genotype = population[i]
                population[i] = self.fitness(genotype)
                print(population[i])
            print(self.fitness(sorted(self.data,reverse=True)))
            break