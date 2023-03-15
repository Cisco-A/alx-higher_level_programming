#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == len(tuple_b) == 2:
        return(tuple_a + tuple_b)
    elif len(tuple_a) > 2:
        return(tuple_a[:1] + tuple_b)
    elif len(tuple_b) > 2:
        return(tuple_a + tuple_b[:1])
    elif len(tuple_a) < 2:
        tuple_1 = list(tuple_a)
        if len(tuple_a) == 0:
            tuple_1.append(0)
            tuple_1.append(0)
        else:
            tuple_1.append(0)
        tuple_a = tuple(tuple_1)
        return(tuple_a + tuple_b)
    elif len(tuple_b) < 2:
        tuple_2 = list(tuple_b)
        if len(tuple_b) == 0:
            tuple_2.append(0)
            tuple_2.append(0)
        else:
            tuple_2.append(0)
        tuple_b = tuple(tuple_2)
        return(tuple_a + tuple_b)
