import pytest
from readText import read_text_file

def test_read_text_file():
    # Предполагается, что у вас есть тестовый файл test.txt в tests/test_files/
    file_path = "/Users/kirillanosov/extractText/tests/test_files/txt_test.txt"
    expected_output = "Это тестовый файл."
    
    assert read_text_file(file_path) == expected_output
