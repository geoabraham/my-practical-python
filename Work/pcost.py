# pcost.py
#
# Exercise 1.27
import csv
import sys


def portfolio_cost(file_name):
    f = open(file_name, 'rt')
    rows = csv.reader(f)
    f.close()

    total = 0.0
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
