#!/usr/bin/python3
def no_c(my_string):
    '''
    new_list = []
    # convert string into list
    for char in my_string:
        new_list.append(char)
    # remove instances of "C" or "c"
    for i in range(len(new_list)):
        if new_list[i] == "c" or new_list[i] == "C":
            new_list.pop(i)
    new_string = ""
    return (new_string.join(new_list))
    '''
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
