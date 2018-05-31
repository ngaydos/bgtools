rolls = []
from roll_stats import *
import matplotlib.pyplot as plt

def count_to_16():
    '''counts how many rolls required to roll a D&D character stat array with 2 stats 16 or higher
    input = None
    output = list'''
    acc = 0
    rolls = []
    rollnumber = 0
    while acc < 2:
        rollnumber += 1
        acc = 0
        rolls = create_array()
        for number in rolls:
            if number >= 16:
                acc += 1
    return rollnumber

counts = []
for i in range(10000):
    counts.append(count_to_16())
plt.hist(counts)
plt.show()