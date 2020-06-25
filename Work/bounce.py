# bounce.py
#
# Exercise 1.5
height = 100
bounce = 0

while bounce < 10:
    height = height * 60 / 100
    bounce += 1
    print(f"{bounce} {round(height, 4)}")
