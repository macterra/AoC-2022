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

rocks = []
rocks.append(makeRock(4,1,"####"))
rocks.append(makeRock(3,3,".#.###.#."))
rocks.append(makeRock(3,3,"..#..#####"))
rocks.append(makeRock(1,4,"####"))
rocks.append(makeRock(2,2,"####"))
#print(rocks)

chamber = np.full((3,7), 0)
top = 0
t = 0

def addRock(rock, top, chamber, rocks):
    print(rock)
    h, w = rock.shape
    ht, _ = chamber.shape

    print(w, h, ht, top)
    if ht <= top + h + 3:
        chamber = np.vstack((np.full((h,7),0), chamber))
    
    return chamber

# rock = np.copy(rocks[0])
# chamber = addRock(rock, top, chamber, rocks)
# print(chamber)

# for rock in rocks:
#     chamber = np.vstack((rock, chamber))

print(chamber)
print()
print(rocks[1])
print()
print(chamber[6:9,])
print()
test = rocks[1] + chamber[6:9,] == 2
print(test, np.any(test))

def shift(rock, left):
    if left:
        if np.all(rock[:,0] == 0):
            rock = np.roll(rock, -1, axis=1)
    else:
        if np.all(rock[:,-1] == 0):
            rock = np.roll(rock, 1, axis=1)
    return rock

