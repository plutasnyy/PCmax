from time import time
from random import shuffle, sample
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

    def fitness(self, chromosome):
        proc_array = greedy([self.number_of_processors,self.number_of_exercises,chromosome])
        fitness = 0
        max_time = 0
        for proc in proc_array:
            if proc.time > max_time:
                max_time = proc.time
            fitness += abs(self.optimum - proc.time)

        if max_time < self.optimum:
            raise ValueError

        fitness += max_time - self.optimum
        return (chromosome,round(fitness,2))

    def two_random_numbers_from_interval(self, interval):
        start_section, end_section = sample(interval, 2)
        if start_section > end_section:
            start_section, end_section = end_section, start_section
        return start_section, end_section

    def crossover(self, parent_one, parent_two):
        print(parent_one)
        print(parent_two)

        child = list()
        if len(parent_one) != len(parent_two):
            raise AssertionError

        for i in range(len(parent_one)):
            child.append(-1)

        start_section, end_section = self.two_random_numbers_from_interval(range(len(parent_one)))

        interval = parent_one[start_section:end_section]
        second_interval = parent_two[start_section:end_section]
        rest_of_second_parent = parent_two[:start_section] + parent_two[end_section:]

        for i in interval:
            if i in rest_of_second_parent:
                rest_of_second_parent.remove(i)
            elif i in second_interval:
                #print(second_interval)
                second_interval.remove(i)

        child[start_section:end_section] = interval
        indexes_to_fill = [x for x in range(len(parent_one)) if x < start_section or x >= end_section]
        #print(indexes_to_fill)
        for i in indexes_to_fill:
            if len(second_interval) > 0:
                child[i] = second_interval.pop(0)
            else:
                child[i] = rest_of_second_parent.pop(0)

        if len(rest_of_second_parent) > 0:
            raise ValueError

        if -1 in child:
            raise ValueError

        print(start_section, " : ",end_section)
        print(child)
        return child


    def start(self):
        start_time = time()

        population = self.generate_random_population()
        while time() - start_time < self.time_limit:
            for i in range(len(population)):
                chromosome = population[i]
                population[i] = self.fitness(chromosome)
            #print(self.fitness(sorted(self.data,reverse=True)))

            self.crossover(population[0][0], population[1][0])
            break