def read_file(filename):
    with open(filename, 'r') as file:
        return set(file.readlines())

def write_to_file(filename, lines):
    with open(filename, 'w') as file:
        file.writelines(lines)

def main():
    file1 = "file1.txt"
    file2 = "file2.txt"

    try:
        lines1 = read_file(file1)
        lines2 = read_file(file2)

        same_lines = lines1.intersection(lines2)
        diff_lines = lines1.symmetric_difference(lines2)

        write_to_file('same.txt', sorted(same_lines))
        write_to_file('diff.txt', sorted(diff_lines))
        
        print("The operation was completed successfully.")
    except FileNotFoundError:
        print("Error: one of the files was not found.")


if __name__ == "__main__":
    main()