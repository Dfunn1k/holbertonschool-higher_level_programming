#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = sys.argv

    if len(arguments) == 1:
        print("0 arguments:")

    elif len(arguments) == 2:
        print("{:d} argument:".format(len(arguments) - 1))
        print("{:d}: {}".format(1, arguments[1]))

    else:
        print("{:d} arguments:".format(len(arguments) - 1))
        for i in range(1, len(arguments)):
            print("{:d}: {}".format(i, arguments[i]))
