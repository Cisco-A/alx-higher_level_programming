#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divisibles = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            divisibles[i] = True
        else:
            divisibles[i] = False
    return divisibles
