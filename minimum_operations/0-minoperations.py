#!/usr/bin/python3
"""
Calculates the minimum number of Copy and Paste operations needed to get n H characters in a text file
"""


def minOperations(n):
    """ If n is less than or equal to 1, then it is already achieved, so return 0 operations"""
    if n <= 1:
        return 0
    
    operations = 0
    i = 2
    """Loop until i squared is greater than n"""
    while i * i <= n:
        """If n is divisible by i, increase operations by 2 and divide n by i"""
        while n % i == 0:
            operations += 2
            n = n // i
        i += 1
    
    """If n is still greater than 1, increment operations by 1"""
    if n > 1:
        operations += 1
    
    """Return the total number of operations"""
    return operations

