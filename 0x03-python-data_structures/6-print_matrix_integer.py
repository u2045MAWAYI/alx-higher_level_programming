#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for num in range(len(matrix)):
        for j in range(len(matrix[num])):
            if j != 0:
                print(" ", end='')
            print("{:d}".format(matrix[num][j]), end='')
        print()
