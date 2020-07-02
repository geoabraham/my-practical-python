# pcost.py
#
# Exercise 1.27


def portfolio_cost(filename):
    total = 0.0
    with open(filename, 'rt') as f:
        headers = next(f)
        for line in f:
            split_line = line.split(',')
            total += int(split_line[1]) * float(split_line[2])
    return total


total_cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost {round(total_cost, 2)}')
