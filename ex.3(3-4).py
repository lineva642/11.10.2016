import random
import numpy as np
import matplotlib.pyplot as plt
n=int(input())
def get_percentile(values, n):
    kol = 100/n
    res = []
    ch = 0
    for _ in range (n):
         res.append(np.percentile(values, ch))
         ch += kol
    res[0] = 0.0
    return res
values = [3, 4, 1, 2, 5, 6, 7, 8, 9, 10]
a=get_percentile(values, 4)
print(a)

def get_percentile_number(value, percentiles):
    i = 0
    while percentiles[i] <= value:
        index = i
        if i <len(percentiles)-1:
            i+=1
        else:
            break
    return index
if __name__=='__main__':
    values = [3.0, 4.0, 1.0, 2.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
    percentiles = get_percentile(values, 4)
    print(percentiles)
    print(get_percentile_number(2.5, percentiles))

def value_equalization(value, percentiles, add_random = False):
    idx = get_percentile_number(value, percentiles)
    step = 1/len(percentiles)
    new_value = idx*step
    if add_random == True:
        new_value = idx*step + random.uniform(0, step)
    return new_value
percentiles = get_percentile(values, 5)
print(value_equalization(5.5, percentiles))
