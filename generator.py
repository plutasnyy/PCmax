from config import *
from random import randint
from proc_class import *

def add_ex_to_proc(proc_array, ex_range, proc_number):
    for i in range(ex_range):
        proc = randint(0, proc_number - 1)
        ex_time = randint(MIN_EX_TIME, MAX_EX_TIME)
        proc_array[proc].add_ex(ex_time)

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

def create_instance(proc_array, proc_number, ex_number):
    instance = str()
    instance += str(proc_number) + "\n"
    instance += str(ex_number) + "\n"

    for proc in proc_array:
        for ex in proc.ex:
            instance += str(ex) + "\n"

    return instance

def save_instance(instance):
    with open('data.txt', 'w') as open_file:
        open_file.write(instance)

def generate():
    proc_number = PROCESSORS
    ex_number = EXERCIESES

    if RAND_PROC:
        proc_number = randint(MIN_PROC, MAX_PROC)

    if RAND_EX:
        ex_number = randint(MIN_EX, MAX_EX)


    proc_array = list()
    for i in range(proc_number):
        proc_array.append(Proc(i))

    if OPTIMAL:
        add_ex_to_proc(proc_array, ex_number - proc_number, proc_number)
        max_proc, pc_max = add_ex_to_longest(proc_array)
        fill(proc_array, max_proc, pc_max)
        instance = create_instance(proc_array, proc_number, ex_number)

        print("PCMAX: {}".format(pc_max))
        #print(instance)

    else:
        add_ex_to_proc(proc_array, ex_number, proc_number)
        instance = create_instance(proc_array, proc_number, ex_number)
        #print(instance)

    save_instance(instance)