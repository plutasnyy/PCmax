import sys
import math
from generator import Generator


class Data(object):
    def __init__(self):
        self.generator = Generator()

    def load_data(self):
        print("Wykonuje: ", self.data_path)

        with open('data/{0}'.format(self.data_path), 'r') as open_file:
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
        self.data_array = ['data.txt', 'm25.txt', 'm50.txt', 'm50n200.txt', 'm50n1000.txt']
        try:
            index = int(sys.argv[1])
            self.data_path = self.data_array[index]
        except:
            self.data_path = self.data_array[0]

    def random(self):
        self.generator.generate()
