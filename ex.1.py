__author__ = 'student'
import random
import matplotlib.pyplot as plt

random.seed(0)
plt.subplot(221)
n = 100
values = [random.normalvariate(0, 1) for i in range(n)]
plt.hist(values, bins=100)

random.seed(0)
plt.subplot(222)
n = 1000
values = [random.normalvariate(0, 1) for i in range(n)]
plt.hist(values, bins=100)

random.seed(0)
plt.subplot(223)
n = 10000
values = [random.normalvariate(0, 1) for i in range(n)]
plt.hist(values, bins=100)

random.seed(0)
plt.subplot(224)
n = 100000
values = [random.normalvariate(0, 1) for i in range(n)]
plt.hist(values, bins=100)

plt.show()