#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_integ = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > max_integ:
            max_integ = my_list[i]
    return max_integ
