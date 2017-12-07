from copy import deepcopy
import math
import sys

from greedy import Greedy
from generator import Generator
from data import Data
from genetic import GeneticAlghoritm

def select_input_data():
    data_array = ['data.txt','m25.txt','m50.txt','m50n200.txt','m50n1000.txt']
    try:
        index = int(sys.argv[1])
        return data_array[index]
    except:
        return data_array[0]


generator = Generator()
#generator.generate()

data = Data()
data_path = select_input_data()
data.load_data(data_path)
print("Wykonuje: ",data_path)
print("Oczekiwane optimum: ",math.ceil(sum(data.array_exs)/data.proc))

greedy = Greedy()
greedy.start(data)
print("Greedy: ", greedy.output_time())

data.array_exs = sorted(data.array_exs, reverse=True)

greedy.start(data)
print("Greedy z posorotowanym inputem: ",greedy.output_time())

for i in range(20,101,1):
    genetic = GeneticAlghoritm(
        data = deepcopy(data),
        population_size = i,
        time_limit = 60,

    )
    genetic.start()