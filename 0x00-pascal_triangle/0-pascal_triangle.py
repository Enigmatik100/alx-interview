#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    @args: n integer
    Return: list of integers representing the Pascal's triangle of n
    """
    res = list()
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(res[i - 1][j - 1] + res[i - 1][j])
            row.append(1)
        res.append(row)
    return res
