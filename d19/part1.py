import re
from collections import deque

data = """Blueprint 1: Each ore robot minutess 4 ore. Each clay robot minutess 2 ore. Each obsidian robot minutess 3 ore and 14 clay. Each geode robot minutess 2 ore and 7 obsidian.
Blueprint 2: Each ore robot minutess 2 ore. Each clay robot minutess 3 ore. Each obsidian robot minutess 3 ore and 8 clay. Each geode robot minutess 3 ore and 12 obsidian."""

class Blueprint:
    def __init__(self, line):
        nums = [int(x) for x in re.findall(r'(\d+)', line)]
        self.id = nums[0]
        self.ore = nums[1]
        self.clay = nums[2]
        self.obsidian = (nums[3], nums[4])
        self.geode = (nums[5], nums[6])

    def __repr__(self) -> str:
        return "Blueprint {}: {} {} {} {}".format(self.id, self.ore, self.clay, self.obsidian, self.geode)

def solve(bp):
    maxgeo = 0
    maxgeostate = ()

    oreBots = 1
    claBots = 0
    obsBots = 0
    geoBots = 0

    ore = 0
    cla = 0
    obs = 0
    geo = 0

    state = (oreBots, claBots, obsBots, geoBots, ore, cla, obs, geo)

    oreoreCost = bp.ore
    claoreCost = bp.clay
    obsoreCost, obsclaCost = bp.obsidian
    geooreCost, geoobsCost = bp.geode
    maxore = max(oreoreCost, claoreCost, obsoreCost, geooreCost)
    maxcla = obsclaCost
    maxobs = geoobsCost

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

print(solve(blueprints[0]))
