#!/usr/bin/python3
"""Minimum operations"""


def minOperations(n):
    """Minimum operations"""
    op_count = 0
    for i in range(2, n):
        while n % i == 0:
            op_count += i
            n = int(n / i)
    return op_count
