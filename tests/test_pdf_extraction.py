import pytest
from text_extractor import extractor

def test_read_text_from_pdf():
    file_path = "tests/test_files/pdf_test.pdf"
    expected_output = "This is test"
    assert extractor.extract_text(file_path) == expected_output
