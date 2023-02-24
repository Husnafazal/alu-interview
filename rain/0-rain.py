#!/usr/bin/python3
"""
This is a function that calculate how many square units 
of water will be retained after it rains
"""

def rain(walls):
    """
    This is a function that calculate how many square units 
    of water will be retained after it rains
    """
    n = len(walls)
    if n == 0:
        return 0

    left_max = [0] * n
    right_max = [0] * n

    # Compute the maximum height of walls to the left of each wall.
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], walls[i])

    # Compute the maximum height of walls to the right of each wall.
    right_max[n-1] = walls[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], walls[i])

    # Compute the amount of water retained by each wall.
    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - walls[i]

    return water