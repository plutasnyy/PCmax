class Moderator(object):
    def return_proc(self, array_proc, rev=False):
        return sorted(array_proc, key=lambda x: x.time, reverse=rev)[0]
