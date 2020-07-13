# report.py
#
# Exercise 2.4
import csv
import sys
import os


def read_portfolio(file_name):
    """
    Computes the total cost (shares*price) of a portfolio file
    :param file_name:
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
                portfolio.append((row[0], int(row[1]), float(row[2])))
            except ValueError:
                print("Couldn't parse", row)
        return portfolio


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

print(read_portfolio('Data/portfolio.csv'))
