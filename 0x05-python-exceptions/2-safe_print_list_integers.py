#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(0, x):
            print("{:d}".format(my_list[i]), end='')
            count += 1
        print("")
    except ValueError:
        pass
    finally:
        if x > count:
            return count
        else:
            return x

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))