import csv


def read_csv():
    with open('search_dataset.csv', mode='r') as f:
        reader = csv.DictReader(f, fieldnames=('id', 'name', 'brand'))
        return reader
