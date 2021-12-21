#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
tmp = number
if number < 0:
    tmp *= -1
    l_digit = ((tmp % 10)*-1)
if number >= 0:
    l_digit = number % 10

if l_digit > 5:
    print(f"Last digit of {number} is {l_digit} and is greater than 5")
elif l_digit == 0:
    print(f"Last digit of {number} is {l_digit} and is 0")
elif l_digit < 5:
    print(f"Last digit of {number} is {l_digit} and is less than 6 and not 0")
