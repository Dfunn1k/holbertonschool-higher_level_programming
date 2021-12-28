#!/usr/bin/python3
from calculator_1 import add, sub, div, mul
from sys import argv, exit


if __name__ == "__main__":

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        num1 = int(argv[1])
        num2 = int(argv[3])

        match argv[2]:
            case '+':
                print("{:d} {:s} {:d} = {:d}".format(num1, argv[2], num2, add(num1, num2)))
            case '-':
                print("{:d} {:s} {:d} = {:d}".format(num1, argv[2], num2, sub(num1, num2)))
            case '*':
                print("{:d} {:s} {:d} = {:d}".format(num1, argv[2], num2, mul(num1, num2)))
            case '/':
                print("{:d} {:s} {:d} = {:d}".format(num1, argv[2], num2, div(num1, num2)))
            case _:
                print("Unknown operator. Available operators: +, -, * and /")
                exit(1)
