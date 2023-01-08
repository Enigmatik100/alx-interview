#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    @args: n integer
    Return: list of integers representing the Pascal's triangle of n
    """
    if n <= 0:
        return []

    res = [[1]]
    for i in range(1, n):
        line = [1]
        for k in range(1, i):
            line.append(comb(i - 1, k - 1) + comb(i - 1, k))
        line.append(1)
        res.append(line)
    return res


def fact(n):
    if n <= 0:
        return 1
    return n * fact(n - 1)


def comb(n, p):
    return int(fact(n) / (fact(p) * fact(n - p)))
