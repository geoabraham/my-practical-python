# pcost.py
#
# Exercise 1.27
total = 0.0

with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        split_line = line.split(',')
        total += int(split_line[1]) * float(split_line[2])

print(f'Total cost {round(total, 2)}')
