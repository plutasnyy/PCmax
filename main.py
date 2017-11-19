from greedy import greedy
from generator import generate
from load_data import load_data
from copy import deepcopy
from genetic import GeneticAlghoritm

#generate()
data = load_data()
greedy_output = greedy(deepcopy(data))
genetic = GeneticAlghoritm(
    initial=greedy_output,
    population_size = 5000,

)