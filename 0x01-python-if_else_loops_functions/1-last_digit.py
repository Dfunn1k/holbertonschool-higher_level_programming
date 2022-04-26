#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    ld = ((number * -1) % 10) * -1
else:
    ld = number % 10
if ld == 0:
    print("Last digit of {} is {} and is 0".format(number, ld))
elif ld > 5:
    print("Last digit of {} is {} and is greater that 5".format(number, ld))
elif ld < 6:
    print(f"Last digit of {number} is {ld} and is less than 6 and not 0")
