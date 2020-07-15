# report.py
#
# Exercise 2.4
import csv
import os
import sys


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


def make_report(portfolio, prices):
    """
    takes a list of stocks and dictionary of prices as input
    and returns a list of tuples.
    :param portfolio:
    :param prices:
    :return:
    """
    data = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        diff = current_price - stock['price']
        data.append((stock['name'], stock['shares'], current_price, round(diff, 2)))
    return data


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

print('Gain', round(total_value - total_cost, 2))

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))

report = make_report(portfolio, prices)
for row in report:
    price_formatted = '${:.2f}'.format(row[2])
    print('{0[0]:>10s} {0[1]:10d} {1:>10s} {0[3]:10.2f}'.format(row, price_formatted))
