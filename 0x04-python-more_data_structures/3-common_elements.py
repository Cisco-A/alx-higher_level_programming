#!/usr/bin/python3
def common_elements(set_1, set_2):
    return (list(map(lambda a, b: a if a == b else None, set_1, set_2)))
