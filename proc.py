class Proc(object):

    def __init__(self, id):
        self.time = 0
        self.id = id
        self.ex = list()

    def add_ex(self, ex):
        self.ex.append(ex)
        self.time += ex

    def print_proc(self):
        print("ID: {0}, Time: {1}, Ex: {2}".format(self.id, self.time, ' '.join(map(str, self.ex))))


