import numpy as np
import time
import sys

def creat_diagnal_matrix(number):
    matrix = np.zeros((number, number), dtype=float)
    for i in range(number):
        matrix[i][i] = 1
    return matrix


def my_inverse_matrix(matrix):
    dimension = matrix.shape[0]
    diagnoal = creat_diagnal_matrix(dimension)
    "This loop control every diagnal number must be dived as 1"
    for d in range(dimension):
        "temp store the information which every row of numbers should be devided"
        temp = matrix[d][d]
        for c in range(dimension):
            matrix[d][c] = matrix[d][c] / temp
            diagnoal[d][c] = diagnoal[d][c] / temp
        # print 'process matrix:\n',matrix
        # print 'process diagnoal:\n',diagnoal
        "This loop control every row should mutiply a number(mu) and add to another row"
        for r in range(dimension):
            mu = -matrix[r][d]
            "But one row which we dived as 1 at the first time should be escaped"
            if (r != d):
                for c in range(dimension):
                    matrix[r][c] = matrix[d][c] * mu + matrix[r][c]
                    diagnoal[r][c] = diagnoal[d][c] * mu + diagnoal[r][c]
                    # print mu
                    # print 'procee\n',matrix
    return diagnoal

if __name__ =='__main__':
    matrix = np.array([[2, 3, 4],
                   [5, 6, 7],
                   [2, 9, 10]], dtype=float)

    print ("Original matrix is:\n", matrix)
    t1 = time.time()
    print ("\nInverse matrix using python function is:\n", np.linalg.inv(matrix))
    t2 = time.time()
    my_inverse = my_inverse_matrix(matrix)
    t3 = time.time()
    print ("\nInverse matrix using my function is:\n", my_inverse)

    print ("\nPython function cost(s):", t2 - t1, "\nMy function cost(s):", t3 - t2)