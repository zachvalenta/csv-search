import csv

from loguru import logger


def get_queries():
    with open('queries.txt', mode='r') as f:
        return f.read().splitlines()


def create_query_container():
    queries = get_queries()
    containers = list()
    for q in queries:
        containers.append(dict(
            query=q,
            count=0,
            results=list()
        ))
    return containers


def read_products():
    with open('search_dataset.csv', mode='r') as f:
        reader = csv.DictReader(f, fieldnames=('id', 'name', 'brand'))
        for row in reader:
            logger.debug('id {} name {} brand {}'.format(row['id'], row['name'], row['brand']))
