#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = lambda a, b: a if a == b else None
    return (list(map(common, set_1, set_2)))
