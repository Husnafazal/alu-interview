def minOperations(n):
    if n <= 1:
        return 0
    
    operations = 0
    i = 2
    while i * i <= n:
        while n % i == 0:
            operations += 2
            n = n // i
        i += 1
    
    if n > 1:
        operations += 1
    
    return operations
