#!/usr/bin/python3
"""
This is a function that calculates the minimum number
of operations needed to result in exactly n 'H' characters in a text file.
"""


def minOperations(n):
    """ return 0 if n is less than or equal to 0"""
    if n <= 0:
        return 0
    operations = 0
    i = 2
    """ iterate through all possible divisors of n"""
    while i <= n:
        """add the divisor to operations count and divide n by it
         until n is no longer divisible by it"""
        while n % i == 0:
            operations += i
            n = n // i
        i += 1
    """ return the total number of operations"""
    return operations
