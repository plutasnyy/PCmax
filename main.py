from greedy import greedy
from generator import generate
from load_data import load_data
from copy import deepcopy
from genetic import GeneticAlghoritm

generate()
data = load_data()
#greedy_output = greedy(deepcopy(data))
genetic = GeneticAlghoritm(
    data = [3,10,[1,2,2,2,2,2,2,8,9,10]],
    population_size = 2,
    time_limit = 5

)
genetic.start()