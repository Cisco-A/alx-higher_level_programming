#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in range(len(matrix)):
        solve = list(map(lambda x: x ** 2, matrix[row]))
        new_matrix.append(solve)
    return new_matrix
