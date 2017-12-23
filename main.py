from copy import deepcopy

from greedy import Greedy
from data import DataManager
from genetic import GeneticAlghoritm

data = DataManager()
data.select_input_data()
data.load_data()

greedy = Greedy()
greedy.start(data)
print("Greedy: ", greedy.output_time())

data.array_exs = sorted(data.array_exs, reverse=True)

greedy.start(data)
print("Greedy with sorted input: ",greedy.output_time())

for i in range(20,101,1):
    genetic = GeneticAlghoritm(
        data = data,
        population_size = i,
        time_limit = 60,

    )
    genetic.start()