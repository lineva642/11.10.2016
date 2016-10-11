__author__ = 'student'
import random
import numpy as np
n=int(input())
def get_percentile(values, n):
    stepp = 100/n
    result = []
    act = 0
    for o in range (n):
         result.append(np.percentile(values, act))
         act += stepp
    result[0] = 0.0
    return result
def get_percentile_number(value, percentiles):
    i = 0
    while percentiles[i] <= value:
        index = i
        if i <len(percentiles)-1:
            i+=1
        else:
            break
    return index
values = [3.0, 4.0, 1.0, 2.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
percentiles = get_percentile(values, 4)
print(get_percentile_number(2.5,percentiles))