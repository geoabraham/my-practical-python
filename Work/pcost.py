# pcost.py
#
# Exercise 1.27
import csv
import sys
import os


def portfolio_cost(file_name):
    if not os.path.exists(file_name):
        print(f'ERROR :: Can\'t find {file_name}')
        sys.exit()

    total = 0.0

    with open(file_name, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            try:
                total += int(row[1]) * float(row[2])
            except ValueError:
                print("Couldn't parse", row)
        return total


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

total_cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost {round(total_cost, 2)}')
