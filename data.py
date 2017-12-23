import sys
import math
from generator import Generator
from random import shuffle
from config import *

class DataManager(object):
    def __init__(self):
        self.generator = Generator()
        self.initial_vector = None

    def load_data(self):
        print("Wykonuje: ", self.data_path)

        with open('data/{0}.txt'.format(self.data_path), 'r') as open_file:
            file = open_file.read().split('\n')
            self.proc, self.ex, file = int(file[0]), int(file[1]), file[2:]
            self.array_exs = list()
            for line in file:
                try:
                    time = int(line)
                    if time > 0:
                        self.array_exs.append(time)
                    else:
                        print("wtf", time)
                        raise AttributeError

                except:
                    print("Bad input line:", line)

        print("Oczekiwane optimum: ", math.ceil(sum(self.array_exs) / self.proc))

    def set_array_exs(self, new_array):
        self.array_exs = new_array

    def select_input_data(self):
        self.data_array = ['data', 'm25', 'm50', 'm50n200', 'm50n1000']
        try:
            index = int(sys.argv[1])
            self.data_path = self.data_array[index]
            if index == 0:
                self.random()
        except:
            self.data_path = self.data_array[0]

    def random(self):
        self.generator.generate()

    def return_initial_vector(self):
        if self.initial_vector is None:
            shuffle(self.array_exs)
            return self.array_exs
        return self.initial_vector

    def load_best_vector(self):
        if INITIAL_VECTOR == "RANDOM":
            pass
        elif INITIAL_VECTOR == "GREEDY":
            self.initial_vector = sorted(self.array_exs, reverse=True)
        elif INITIAL_VECTOR == "LAST_BEST":
            output, self.initial_vector = self._load_vector_file()
            if output is None:
                self.initial_vector = sorted(self.array_exs, reverse=True)
            else:
                print("Time to improve: {}".format(output))

    def save_best(self, value, new_vector):
        if self.data_path != "data":
            output, vector = self._load_vector_file()
            with open('data/{0}_last_best.txt'.format(self.data_path), 'w+') as open_file:
                if output is None or value < output:
                    open_file.write("{}\n{}".format(value, new_vector))
                else:
                    open_file.write('{}\n{}'.format(output, vector))

    def _load_vector_file(self):
        with open('data/{0}_last_best.txt'.format(self.data_path), 'r') as open_file:
            file = open_file.read().split('\n')
            try:
                output, initial_data = int(file[0]), file[1]
                initial_vector = [int(x) for x in initial_data[1:-1].split(",")]
                return output, initial_vector
            except:
                return None, None


