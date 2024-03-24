import pytest
from text_extractor import extractor

def test_read_text_from_txt():
    file_path = "tests/test_files/txt_test.txt"
    expected_output = "This is test"
    assert extractor.extract_text(file_path) == expected_output
