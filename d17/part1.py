import numpy as np

"""
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
## 
"""

def makeRock(w, h, pattern):
    rock = np.full((4,7), 0)
    for i in range(h):
        for j in range(w):
            if pattern[i*w+j] == '#':
                rock[i,j] = 1
    rock = np.roll(rock, 4-h, axis=0)
    rock = np.roll(rock, 2, axis=1)
    print(rock)
    return rock

data = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
data = open('data', 'r').read().strip()
jets = list(data)

rocks = []
rocks.append(makeRock(4,1,"####"))
rocks.append(makeRock(3,3,".#.###.#."))
rocks.append(makeRock(3,3,"..#..#####"))
rocks.append(makeRock(1,4,"####"))
rocks.append(makeRock(2,2,"####"))

def shift(rock, jet):
    if jet == '<':
        if np.all(rock[:,0] == 0):
            rock = np.roll(rock, -1, axis=1)
    elif jet == '>':
        if np.all(rock[:,-1] == 0):
            rock = np.roll(rock, 1, axis=1)
    else:
        print("bad jet")
        exit()

    return rock

template = np.full((20,7), 0)
chamber = np.copy(template)

def nextRock():
    rock = rocks.pop(0)
    rocks.append(rock)
    return np.copy(rock)

def nextJet():
    jet = jets.pop(0)
    jets.append(jet)
    return jet

def findTop(chamber):
    ht, _ = chamber.shape
    for row in range(ht):
        if np.any(chamber[row,:] == 1):
            break
    return row

def drop(chamber):
    top = findTop(chamber)
    
    if top < 20:
        chamber = np.vstack((template, chamber))
        top += 20

    ht, _ = chamber.shape
    alt = top - 3
    rock = nextRock()
    while alt < ht:
        jet = nextJet()
        shifted = shift(rock, jet)
        test = shifted * chamber[alt-4:alt,] == 1
        if not np.any(test):
            rock = shifted
        test = rock * chamber[alt-3:alt+1,] == 1
        if np.any(test):
            break
        alt += 1
        
    #print(ht-alt, rock)    
    chamber[alt-4:alt,] += rock
    #print(chamber)
    return chamber

for i in range(2022):
    chamber = drop(chamber)
    ht, _ = chamber.shape
    top = findTop(chamber)
    print(ht-top)
