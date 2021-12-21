#!/usr/bin/python3
for num in range(0, 100):
    if num == 99:
        print("{: 03d}".format(num))
        break
    print("{: 03d}".format(num), end=", ")
