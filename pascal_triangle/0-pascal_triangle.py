#!/usr/bin/python3
""" This module provides a function for generating
 Pascal's triangle up to a given number of rows."""
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = prev_row[j-1] + prev_row[j]
        triangle.append(row)

    return triangle
