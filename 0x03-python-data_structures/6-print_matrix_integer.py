#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for column in rows:
            if column != rows[0]:
                print(" ", end='')
            print("{:d}".format(column), end='')
        print()
