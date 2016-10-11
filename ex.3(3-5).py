import numpy as np
import random
import matplotlib.pyplot as plt
import pylab

n=int(input())
def get_percentile(values, n):
    p = 100/n
    res = []
    count = 0
    res.append(0.0)
    count += p
    while count < 100:
        res.append(np.percentile(values, count))
        count += p
    return res

def get_percentile_number(value, percentiles):
    i = 0
    while percentiles[i] <= value:
        i += 1
        if i >= len(percentiles):
            i -= 1
            return i
    return i-1

def value_equalization(value, percentiles, addRandom=False, add_random=False):
    if add_random: addRandom = True
    if not addRandom:
        idx = get_percentile_number(value, percentiles)
        step = 1 / len(percentiles)
        value = idx*step
        return value
    else:
        idx = get_percentile_number(value, percentiles)
        step = 1 / len(percentiles)
        random_noise = random.uniform(0, step)
        value = idx*step + random_noise
        return value

def values_equalization(values, percentiles, addRandom=False, add_random=False):
    if add_random: addRandom = True
    res = []
    for i in values:
        res.append(value_equalization(i, percentiles, addRandom))
    return res
if __name__=='__main__':
    v = [3, 4, 1, 2, 5, 6, 7, 8, 9, 10]
    p = (get_percentile(v, 4))
    print(values_equalization(v, p, addRandom=True))
