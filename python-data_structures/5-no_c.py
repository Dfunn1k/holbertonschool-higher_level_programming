#!/usr/bin/python3
def no_c(my_string):
    msg = [char for char in my_string]
    if 'c' in msg:
        msg.remove('c')
    if 'C' in msg:
        msg.remove('C')
    return ''.join(msg)
