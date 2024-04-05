import pytest

# Функция для сравнения содержимого двух файлов
def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        content1 = f1.readlines()
        content2 = f2.readlines()
        return content1 == content2

# Тест для проверки содержимого двух файлов
def test_compare_files():
    assert compare_files('file1.txt', 'file2.txt') == False

# Фикстура для чтения содержимого файла
@pytest.fixture
def read_file_content(file):
    with open(file, 'r') as f:
        return f.readlines()

# Параметризованный тест для проверки содержимого файлов
@pytest.mark.parametrize("file", ['file1.txt', 'file2.txt'])
def test_read_file_content(read_file_content, file):
    content = read_file_content
    assert len(content) == 10  # Проверяем, что файл содержит 10 строк

