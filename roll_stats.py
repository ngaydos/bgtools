import random

def create_array():
    '''creates an array of D&D stats by rolling 4 six sided dice, dropping the lowest
    and repeating 6 times to create 6 numbers
    inputs = None
    outputs = list of numbers between 3 and 18
    '''
    array = []
    for value in range(6):
        rolls = []
        for value in range(4):
            rolls.append(random.randint(1, 6))
        rolls.remove(min(rolls))
        array.append(sum(rolls))
    return array

if __name__ == '__main__':
    print(create_array())