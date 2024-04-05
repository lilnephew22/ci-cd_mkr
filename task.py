from typing import Set, List

# Функция для чтения строк из файла и возврата уникального множества строк
def read_file(filename: str) -> Set[str]:
    with open(filename, 'r') as file:
        return set(file.readlines())

# Функция для записи списка строк в файл
def write_to_file(filename: str, lines: List[str]) -> None:
    with open(filename, 'w') as file:
        file.writelines(lines)

# Главная функция программы
def main() -> None:
    file1: str = "file1.txt"
    file2: str = "file2.txt"

    try:
        # Чтение строк из двух файлов
        lines1: Set[str] = read_file(file1)
        lines2: Set[str] = read_file(file2)

        # Нахождение общих и различных строк
        same_lines: Set[str] = lines1.intersection(lines2)
        diff_lines: Set[str] = lines1.symmetric_difference(lines2)

        # Запись результатов в файлы
        write_to_file('same.txt', sorted(same_lines))
        write_to_file('diff.txt', sorted(diff_lines))

        print("The operation was completed successfully.")
    except FileNotFoundError:
        print("Error: one of the files was not found.")

# Запуск главной функции, если скрипт запущен напрямую
if __name__ == "__main__":
    main()
