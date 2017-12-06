from greedy import Greedy
from generator import Generator
from data import Data
from genetic import GeneticAlghoritm
from copy import deepcopy

generator = Generator()
#generator.generate()

data = Data()
data.load_data('data.txt')

greedy = Greedy()
greedy.start(data)
print("Greedy: ", greedy.output_time())

data.array_exs = sorted(data.array_exs, reverse=True)

greedy.start(data)
print("Greedy z posorotowanym inputem: ",greedy.output_time())


for i in range(10,101,5):
    genetic = GeneticAlghoritm(
        data = deepcopy(data),
        population_size = i,
        time_limit = 30,

    )
    genetic.start()