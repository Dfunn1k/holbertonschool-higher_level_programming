#!/usr/bin/python3
from calculator_1 import add, div, mul, sub
from sys import argv

if __name__ == "__main__":
    i = argv
    if len(i) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        operator = i[2]
        num1 = int(i[1])
        num2 = int(i[3])

        if operator == '+':
            print(f"{num1} {operator} {num2} = {add(num1, num2)}")
        elif operator == '-':
            print(f"{num1} {operator} {num2} = {sub(num1, num2)}")
        elif operator == '*':
            print(f"{num1} {operator} {num2} = {mul(num1, num2)}")
        elif operator == '/':
            print(f"{num1} {operator} {num2} = {div(num1, num2)}")
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
