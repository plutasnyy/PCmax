from proc_class import*
from load_data import load_data

def greedy(input_data):
    proc_array = list()
    [proc, ex, data] = input_data

    for i in range(proc):
        proc_array.append(Proc(i))

    for i in data:
        return_proc(proc_array).add_ex(i)

    #print(return_proc(proc_array, rev=True).time)

    #for i in proc_array:
    #    i.print_proc()

    return proc_array
