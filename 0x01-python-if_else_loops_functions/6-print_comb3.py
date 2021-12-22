#!/usr/bin/python3
for num1 in range(0, 10):
    for num2 in range(0, 10):
        if num2 <= num1:
            pass
        else:
            if (num1 == 8 and num2 == 9):
                print("{}{}".format(num1, num2))
                break
            print("{}{}".format(num1, num2), end=", ")
