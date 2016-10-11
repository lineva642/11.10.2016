__author__ = 'student'
import random
import numpy as np

n=int(input())
def   get_percentile(values, n):
    perl=100/n
    result = []
    act = 0
    for o in range (n):
        result.append(np.percentile(values,act))
        act +=perl
    result[0]=0.0
    return result
values = [3, 4, 1, 2, 5, 6, 7, 8, 9, 10]
print(get_percentile(values, 4))



