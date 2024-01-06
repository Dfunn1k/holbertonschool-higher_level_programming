#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv, exit
    from calculator_1 import add, sub, div, mul

    operator = argv[2]
    num1 = int(argv[1])
    num2 = int(argv[3])

    operations = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }

    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    if operator not in operations.keys():
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    print(f"{num1} {operator} {num2} = {operations[operator](num1, num2)}")
