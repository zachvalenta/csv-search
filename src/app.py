import csv
import re

from loguru import logger


def get_tokens():
    with open('queries.txt', mode='r') as f:
        tokens = list()
        queries = f.read().splitlines()
        for x in queries:
            tokens.append(x.split())
        return tokens


def create_query_container():
    tokens = get_tokens()
    containers = list()
    for token in tokens:
        containers.append(dict(
            count=0,
            tokens=token,
        ))
    return containers


def read_products():
    queries = create_query_container()
    with open('search_dataset.csv', mode='r') as f:
        reader = csv.DictReader(f, fieldnames=('id', 'name', 'brand'))
        for row in reader:
            for query in queries:
                for token in query['tokens']:
                    regex = re.compile(r'^{}'.format(token), re.IGNORECASE)
                    if re.search(regex, row['name']):
                        query['count'] += 1
    logger.debug(queries)
