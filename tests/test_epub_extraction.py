import pytest
from text_extractor import extractor

def test_read_text_from_epub():
    file_path = "tests/test_files/epub_test.epub"
    expected_output = "This is test"
    assert extractor.extract_text(file_path) == expected_output
