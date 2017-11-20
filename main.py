from greedy import greedy
from generator import generate
from load_data import load_data
from copy import deepcopy
from genetic import GeneticAlghoritm

#generate()
data = load_data()
#greedy_output = greedy(deepcopy(data))
genetic = GeneticAlghoritm(
    data = [1,2,3,4,5],
    population_size = 20,
    time_limit = 5

)
genetic.start()