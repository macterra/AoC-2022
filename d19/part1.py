import re
from collections import deque

data = """\
Blueprint 1: Each ore robot minutess 4 ore. Each clay robot minutess 2 ore. Each obsidian robot minutess 3 ore and 14 clay. Each geode robot minutess 2 ore and 7 obsidian.
Blueprint 2: Each ore robot minutess 2 ore. Each clay robot minutess 3 ore. Each obsidian robot minutess 3 ore and 8 clay. Each geode robot minutess 3 ore and 12 obsidian."""

class Blueprint:
    def __init__(self, line):
        nums = [int(x) for x in re.findall(r'(\d+)', line)]
        self.id = nums.pop(0)
        self.costs = nums

def solve(costs):
    maxgeo = 0
    maxgeostate = ()
    oreoreCost, claoreCost, obsoreCost, obsclaCost, geooreCost, geoobsCost = costs
    maxore = max(oreoreCost, claoreCost, obsoreCost, geooreCost)
    maxcla = obsclaCost
    maxobs = geoobsCost
    
    state = (1, 0, 0, 0, 0, 0, 0, 0)
    pqueue = deque([(0, state)])
    visited = set()

    while len(pqueue) > 0:
        minutes, state = pqueue.popleft()
        
        #print(minutes, state, len(pqueue), maxgeo)

        if (state) in visited:
            continue

        visited.add(state)

        oreBots, claBots, obsBots, geoBots, ore, cla, obs, geo = state

        if geo > maxgeo:
            maxgeo = geo
            maxgeostate = state
            print(minutes, maxgeo, maxgeostate)

        if minutes == 24:
            continue

        timeleft = 24-minutes

        if (geo + timeleft * geoBots) < maxgeo:
            continue

        ore += oreBots
        cla += claBots
        obs += obsBots
        geo += geoBots

        pqueue.append((minutes+1, (oreBots, claBots, obsBots, geoBots, ore, cla, obs, geo)))

        if oreoreCost < ore and oreBots < maxore:
            pqueue.append((minutes+1, (oreBots+1, claBots, obsBots, geoBots, ore-oreoreCost, cla, obs, geo)))

        if claoreCost < ore and claBots < maxcla:
            pqueue.append((minutes+1, (oreBots, claBots+1, obsBots, geoBots, ore-claoreCost, cla, obs, geo)))

        if obsoreCost < ore and obsclaCost < cla and obsBots < maxobs:
            pqueue.append((minutes+1, (oreBots, claBots, obsBots+1, geoBots, ore-obsoreCost, cla-obsclaCost, obs, geo)))

        if geooreCost < ore and geoobsCost < obs:
            pqueue.append((minutes+1, (oreBots, claBots, obsBots, geoBots+1, ore-geooreCost, cla, obs-geoobsCost, geo)))
        
    print(maxgeostate, maxgeo)
    print((1,4,2,2,6,41,8,9) in visited)
    return maxgeo

#data = open('data', 'r').read()
lines = data.split('\n')

blueprints = [ Blueprint(line) for line in lines ]

print(blueprints)

print(solve(blueprints[0].costs))
