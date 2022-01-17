#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        print(''.join(map(str, my_list[0:x])))
        for i in my_list:
            count += 1
    except ValueError:
        pass
    finally:
        if x > count:
            return count
        else:
            return x
