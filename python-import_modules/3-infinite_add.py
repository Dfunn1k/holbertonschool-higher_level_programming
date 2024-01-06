#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv

    args = argv[1:]
    sums = 0

    for arg in args:
        sums += int(arg)

    print(sums)
