rolls = []
from roll_stats import *

def roll_16_or_more():
    '''rolls a D&D character stat array with 2 stats guaranteed to be 16 or higher
    input = None
    output = list'''
    acc = 0
    rolls = []
    while acc < 2:
        acc = 0
        rolls = create_array()
        for number in rolls:
            if number >= 16:
                acc += 1
    return rolls

if __name__ == '__main__':
    print(roll_16_or_more())