#!/usr/bin/python3
def uniq_add(my_list=[]):
    #Adds all unique integers in a list
    uniq_set = set(my_list)
    sum = 0
    for item in uniq_set:
        sum =+ item
    return sum
