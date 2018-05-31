import random

def game_setup(players):
    '''takes a list of players and returns a race
    selection for each player as well as a first speaker
    inputs: list of players
    outputs: dictionary containing a race for each player as well as a starting speaker'''
    races = ['l1z1x mindnet', 'federation of sol', 'yin brotherhood', 'naalu collective', 'embers of muaat', 'mentak coalition',
    'barony of letnev', 'xxcha kingdom', 'emirates of hacan', 'nekro virus', 'winnu', 'sardakk norr', 'ghosts of creuss', 'clan of saar'
    'universities of jol-nar', 'arborec', 'yssaril tribes'] 
    final = {'speaker': random.choice(players)}
    sampled_races = random.sample(races, len(players))
    for i, v in enumerate(players):
        final[players[i]] = sampled_races[i]
    return final

if __name__ == '__main__':
    playercount = input("How many players? ")
    i = list(range(int(playercount)))
    print(game_setup(i))