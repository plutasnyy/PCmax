from proc import Proc
from moderator import Moderator

class Greedy(Moderator):
    def start(self, data):
        self.array_proc = list()

        for i in range(data.proc):
            self.array_proc.append(Proc(i))

        for i in data.array_exs:
            self.return_proc(self.array_proc).add_ex(i)

        return self.array_proc

    def output_time(self):
        return self.return_proc(self.array_proc,rev=True).time
