from config import *
from random import randint
from proc_class import *

def add_ex_to_proc(proc_array, ex_range):
    for i in range(ex_range):
        proc_number = randint(0, PROCESSORS - 1)
        ex_time = randint(MIN_EX_TIME, MAX_EX_TIME)
        proc_array[proc_number].add_ex(ex_time)

def add_ex_to_longest(proc_array):
    ex_time = randint(MIN_EX_TIME, MAX_EX_TIME)
    max_proc = return_proc(proc_array, rev=True)
    max_proc.add_ex(ex_time)
    return max_proc, max_proc.time

def fill(proc_array, max_proc, pc_max):
    for i in proc_array:
        if i != max_proc:
            time_to_pcmax = pc_max - i.time
            i.add_ex(time_to_pcmax)

def create_instance(proc_array):
    instance = str()
    instance += str(PROCESSORS) + "\n"
    instance += str(EXERCIESES) + "\n"

    for proc in proc_array:
        for ex in proc.ex:
            instance += str(ex) + "\n"

    return instance

def save_instance(instance):
    with open('data.txt', 'w') as open_file:
        open_file.write(instance)

def generate():

    proc_array = list()
    for i in range(PROCESSORS):
        proc_array.append(Proc(i))

    if OPTIMAL:
        add_ex_to_proc(proc_array, EXERCIESES - PROCESSORS)
        max_proc, pc_max = add_ex_to_longest(proc_array)
        fill(proc_array, max_proc, pc_max)
        instance = create_instance(proc_array)

        print("PCMAX: {}".format(pc_max))
        print(instance)

    else:
        add_ex_to_proc(proc_array, EXERCIESES)
        instance = create_instance(proc_array)
        print(instance)

    save_instance(instance)