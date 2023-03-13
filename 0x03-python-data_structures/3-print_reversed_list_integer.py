#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list)):
        #current index in the loop is subtracted from length of list
        #to access last element on the list
        #1 is then subtracted from the result to stay in range of index
        print("{:d}".format(my_list[(len(my_list) - i) - 1]))
