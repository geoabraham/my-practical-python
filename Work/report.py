# report.py
#
# Exercise 2.4
import csv
import sys
import os
from pprint import pprint


def read_portfolio(file_name):
    """
    Reads a portfolio file
    :param file_name: portfolio file name.
    :return:
    """
    if not os.path.exists(file_name):
        print(f'ERROR :: Can\'t find {file_name}')
        sys.exit()

    portfolio = []

    with open(file_name, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            try:
                portfolio.append({
                    'name': row[0],
                    'shares': int(row[1]),
                    'price': float(row[2])
                })
            except ValueError:
                print("Couldn't parse", row)
        return portfolio


def read_prices(file_name):
    """
    Reads prices from a file name.
    :param file_name:
    :return:
    """
    if not os.path.exists(file_name):
        print(f'ERROR :: Can\'t find {file_name}')
        sys.exit()

    prices = {}
    with open(file_name, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = row[1]
            except ValueError:
                print('Couldn\'t parse', row)
            except IndexError:
                print('There\'s an empty line')

        return prices


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

pprint(read_portfolio('Data/portfolio.csv'))
pprint(read_prices('Data/prices.csv'))
