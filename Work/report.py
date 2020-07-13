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

    p = []
    with open(file_name, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            try:
                p.append({
                    'name': row[0],
                    'shares': int(row[1]),
                    'price': float(row[2]),
                })
            except ValueError:
                print("Couldn't parse", row)

    return p


def read_prices(file_name):
    """
    Reads prices from a file name.
    :param file_name:
    :return:
    """
    if not os.path.exists(file_name):
        print(f'ERROR :: Can\'t find {file_name}')
        sys.exit()

    p = {}
    with open(file_name, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                p[row[0]] = float(row[1])
            except ValueError:
                print('Could\'t parse', row)
            except IndexError:
                print('There\'s an empty line')

        return p


def print_report(portfolio, prices):
    """
    compute the current value of the portfolio along with the gain/loss
    :param portfolio:
    :param prices:
    :return:
    """
    total = 0.0
    current_value = []
    for s in portfolio:
        total += s['shares'] * s['price']
        value = {
            'name': s['name'],
            'shares': s['shares'],
            'cost': s['price'],
            'value': prices[s['name']],
            'gain': round(s['shares'] * prices[s['name']] - s['shares'] * s['price'], 2),
            'gain(%)': round((s['shares'] * prices[s['name']]) / (s['shares'] * s['price']) * 100 - 100, 2),
        }
        current_value.append(value)

    return current_value


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

total_cost = 0.0
for share in portfolio:
    total_cost += share['shares'] * share['price']

print('Total cost', total_cost)

total_value = 0.0
for share in portfolio:
    total_value += share['shares'] * prices[share['name']]

print('Current value', total_value)
print('Gain', total_value - total_cost)
pprint(print_report(portfolio, prices))
