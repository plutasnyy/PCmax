from time import time
from random import shuffle, sample, uniform
from copy import deepcopy
from greedy import greedy
from proc_class import *

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
        fitness = 1/fitness
        return (chromosome,fitness)

    def two_random_numbers_from_interval(self, interval):
        start_section, end_section = sample(interval, 2)
        if start_section > end_section:
            start_section, end_section = end_section, start_section
        return start_section, end_section

    def crossover(self, parent_one, parent_two):
        #print(parent_one)
        #print(parent_two)

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

        #print(start_section, " : ",end_section)
       # print(child)
        return child

    def mutation(self, chromosome):
        a,b = self.two_random_numbers_from_interval(range(len(chromosome)))
        chromosome[a], chromosome[b] = chromosome[b], chromosome[a]

    def select_with_probability(self,population):
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

        population = self.generate_random_population()
        x=sorted(self.data,reverse=True)
        for i in range(len(population)):
            population[i]=x
        new_population = list()

        while time() - start_time < self.time_limit:
            for i in range(len(population)):
                chromosome = population[i]
                population[i] = self.fitness(chromosome)

            for i in range(int(len(population)/2)):
                parent_one = self.select_with_probability(population)
                parent_two = self.select_with_probability(population)

                child_one = self.crossover(parent_one,parent_two)
                child_two = self.crossover(parent_two,parent_one)

                self.mutation(child_one)
                self.mutation(child_two)

                new_population.append(child_one)
                new_population.append(child_two)

            population = deepcopy(new_population)
            ##print(population)
           # print("")
            #print("")
            new_population.clear()
        #print(population[0])
       # best_chromosome = sorted(population, key = lambda x: 1/self.fitness(x)[1])[0]
        temp = list()
        for i in population:
            x = return_proc(greedy([self.number_of_processors,self.number_of_processors,population[0]]), rev=True).time
            temp.append(x)
        print(min(temp))
