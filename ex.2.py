__author__ = 'student'
import random
def f(x):
    if x < -2 or x > 2:
        res=0
    else:
        res=-x**2+4
    return res
values=[random.random()*6-3 for i in range(100000)]
results=[f(x) for x in values]
int=(6/100000)*sum(results)
print(int)