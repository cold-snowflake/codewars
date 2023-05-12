#Given a non-empty array of integers, return the
#result of multiplying the values together in order.

def grow(arr):
    n = 1
    for i in arr:
        n *= i
    return n
