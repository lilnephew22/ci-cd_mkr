def read_file(filename):
    with open(filename, 'r') as file:
        return set(file.readlines())

