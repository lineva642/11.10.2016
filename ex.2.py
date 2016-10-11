__author__ = 'student'
import random
def f(x):
    if x < -2 or x > 2:
        res=0
    else:
        res=-x**2+4
    return res
n=int(input())
values=[random.random()*6-3 for i in range(n)]
results=[f(x) for x in values]
y=(6/n)*sum(results)

print(y)