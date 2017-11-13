from proc_class import*

def load_data():
    with open('data.txt', 'r') as open_file:
        data = list()
        file = open_file.read().split('\n')
        proc, ex, file = int(file[0]), int(file [1]), file[2:]
        for line in file:
            try:
                time = int(line)
                if time > 0:
                    data.append(time)

                else:
                    raise AttributeError

            except:
                pass
        return proc, ex, sorted(data, reverse=True)

def greedy():
    proc_array = list()
    proc, ex, data = load_data()

    for i in range(proc):
        proc_array.append(Proc(i))

    for i in data:
        return_proc(proc_array).add_ex(i)

    print(return_proc(proc_array, rev=True).time)

    for i in proc_array:
        i.print_proc()
