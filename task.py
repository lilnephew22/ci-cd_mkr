def read_file(filename):
    with open(filename, 'r') as file:
        return set(file.readlines())

def write_to_file(filename, lines):
    with open(filename, 'w') as file:
        file.writelines(lines)