import csv

from src.app import read_csv


def test_my_function():
    assert isinstance(read_csv(), csv.DictReader)
