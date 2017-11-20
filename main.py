from greedy import greedy
from generator import generate
from load_data import load_data
from copy import deepcopy
from genetic import GeneticAlghoritm
from proc_class import *

generate()
data = load_data()
out=greedy(deepcopy(data))
print(return_proc(out,rev=True).time)
a,b,c=data
c=sorted(c,reverse=True)
out = greedy([a,b,c])
print(return_proc(out,rev=True).time)
genetic = GeneticAlghoritm(
    data = data,
    population_size = 50,
    time_limit = 60*5

)
genetic.start()