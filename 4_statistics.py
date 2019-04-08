""" this contains simple commands for calculating statistics"""

import numpy as np
from scipy import stats


# mean/median/mode
data1 = [23, 34, 56, 12, 43, 23, 43]
mean = np.mean(data1)
median = np.median(data1)
mode = stats.mode(data1)   # the most frequent item (or the smallest item if multi-modal)

# weighted mean
data2 = data1
weight = '1 2 3 4 5'

w = list(map(int, weight.strip().split()))  # map: use function for each element in a list
weighted_mean = sum([a*b for a, b in zip(data2, w)]) / sum(w)   # formula
print(format(weighted_mean, '.1f'))         # output with 1 decimal
