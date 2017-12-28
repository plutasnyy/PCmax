from time import time
from random import shuffle, sample, uniform
from copy import deepcopy
import math

from greedy import Greedy


class GeneticAlghoritm(object):
    def __init__(self, data, population_size, time_limit):
        self.data = data
        self.population_size = population_size
        self.time_limit = time_limit
        self.optimum = math.ceil(sum(self.data.array_exs) / self.data.proc)
        self.greedy = Greedy()
        self.generation_best_time = 1
        self.best_time = None
        self.best_vector = None

    def generate_new_population(self):
        population = []
        for i in range(self.population_size):
            initial_vector = self.data.return_initial_vector()
            population.append(deepcopy(initial_vector))

        return population

    def fitness(self, chromosome):
        self.data.set_array_exs(chromosome)
        array_proc = self.greedy.start(self.data)
        fitness = 0

        for proc in array_proc:
            fitness += abs(self.optimum - proc.time)

        chromosome_time = self.greedy.output_time()
        fitness += chromosome_time - self.optimum

        if self.best_time == None:
            self.best_time = chromosome_time
            self.best_vector = deepcopy(chromosome)
        elif chromosome_time < self.best_time:
            self.best_time = chromosome_time
            self.generation_best_time = self.generation
            self.best_vector = deepcopy(chromosome)
        return fitness

    def two_random_numbers_from_interval(self, interval):
        interval = range(len(interval))
        start_section, end_section = sample(interval, 2)
        if start_section > end_section:
            start_section, end_section = end_section, start_section
        return start_section, end_section

    def crossover(self, parent_one, parent_two, start_section, end_section):

        child = [None] * len(parent_one)

        if len(parent_one) != len(parent_two):
            raise AssertionError

        interval = parent_one[start_section:end_section]
        second_interval = parent_two[start_section:end_section]
        rest_of_second_parent = parent_two[:start_section] + parent_two[end_section:]

        for i in interval:  # select data to fill
            if i in rest_of_second_parent:
                rest_of_second_parent.remove(i)
            elif i in second_interval:
                second_interval.remove(i)

        child[start_section:end_section] = interval
        indexes_to_fill = [x for x in range(len(parent_one)) if x < start_section or x >= end_section]

        for i in indexes_to_fill:
            if len(second_interval) > 0:
                child[i] = second_interval.pop(0)
            else:
                child[i] = rest_of_second_parent.pop(0)

        if len(rest_of_second_parent) > 0:
            raise ValueError

        if -1 in child:
            raise Exception

        return child

    def mutation(self, chromosome, a, b):
        chromosome[a], chromosome[b] = chromosome[b], chromosome[a]

    def select_with_probability(self, population):
        weight_sum = sum([x[1] for x in population])
        rand_value = uniform(0, weight_sum)
        for chromosome, fitness in population:
            if fitness > rand_value:
                return chromosome
            else:
                rand_value -= fitness
        return chromosome

    def start(self):
        start_time = time()
        self.data.load_best_vector()
        population = self.generate_new_population()
        weighted_population = [None] * self.population_size
        new_population = list()
        self.generation = 1

        while time() - start_time < self.time_limit:
            for i in range(len(population)):
                chromosome = population[i]

                fit_output = self.fitness(chromosome)
                chromosome_fitness = 1 if fit_output == 0 else fit_output
                weighted_population[i] = (chromosome, chromosome_fitness)

            for _ in range(int(len(population) / 2)):
                parent_one = self.select_with_probability(weighted_population)
                parent_two = self.select_with_probability(weighted_population)

                cros_start, cros_end = self.two_random_numbers_from_interval(chromosome)

                for _ in range(2):
                    child = self.crossover(parent_one, parent_two, cros_start, cros_end)
                    mut_start, mut_end = self.two_random_numbers_from_interval(chromosome)
                    self.mutation(child, mut_start, mut_end)
                    new_population.append(child)
                    parent_one, parent_two = parent_two, parent_one

            population = deepcopy(new_population)
            new_population.clear()
            self.generation += 1

        print("Genetic, population size: {} time: {}s generations: {} score: {} in generation: {}".format(
            self.population_size, self.time_limit, self.generation, self.best_time, self.generation_best_time))

        self.data.save_best(self.best_time, self.best_vector)
