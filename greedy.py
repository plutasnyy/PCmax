def load_data():
    with open('data.txt', 'r') as file:
        data = list()
        for line in file.read().split('\n'):
            try:
                data.append(int(line))
            except:
                pass
        return data


class Proc(object):

    def __init__(self,id):
        self.time = 0
        self.id = id
        self.ex = list()

    def add_ex(self,ex):
        self.ex.append(ex)
        self.time += ex

    def print_proc(self):
        print("ID: {0}, Time: {1}, Ex: {2}".format(self.id, self.time, ' '.join(map(str, self.ex))))


def return_proc(proc_array, rev = False):
    return sorted(proc_array, key = lambda x: x.time, reverse = rev)[0]


def greedy():
    proc_array = [Proc(0), Proc(1), Proc(2)]

    for i in load_data():
        return_proc(proc_array).add_ex(i)

    #print(return_proc(proc_array, rev = True ).time())

    for i in proc_array:
        i.print_proc()
