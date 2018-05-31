import random

def create_array():
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