#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()    
    for i in range(len(new_matrix)):
        row = []
        for j in range(len(new_matrix[i])):
            row.append(new_matrix[i][j]**2)
        new_matrix[i] = row
    return new_matrix
