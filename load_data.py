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
