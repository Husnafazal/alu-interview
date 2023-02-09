#!/usr/bin/python3
"""
Calculates the minimum number of Copy and Paste operations needed to get n H characters in a text file
"""


def minOperations(n):
    """If n is less than or equal to 1, return 0"""
    if n <= 1:
        return 0
    
    """Initialize operations count"""
    operations = 0
    
    """Starting with 2, as 1 is not a factor"""
    i = 2
    
    """Loop until i*i is greater than n"""
    while i * i <= n:
        """Keep dividing n by i until n % i is not 0"""
        while n % i == 0:
            """Increase the operations count by 2 for each division by i"""
            operations += 2
            n = n // i
        i += 1
    
    if n > 1:
        operations += 1
    
    return operations
