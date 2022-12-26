import re
import heapq
from collections import defaultdict

data = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""

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
    costs = defaultdict(int)

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
    geoclaCost, geoobsCost = bp.geode
    maxore = max(oreoreCost, claoreCost, obsoreCost)
    maxcla = max(obsclaCost, geoclaCost)
    maxobs = geoobsCost

    pqueue = [(0, state)]
    heapq.heapify(pqueue)
    visited = set()

    while len(pqueue) > 0:
        cost, state = heapq.heappop(pqueue)
        
        print(cost, state, len(pqueue), maxgeo)

        if (state) in visited:
            continue

        visited.add(state)

        oreBots, claBots, obsBots, geoBots, ore, cla, obs, geo = state

        ore += oreBots
        cla += claBots
        obs += obsBots
        geo += geoBots

        if geo > maxgeo:
            maxgeo = geo
            maxgeostate = state

        if cost == 4:
            continue

        timeleft = 24-cost

        if (geo + timeleft) < maxgeo:
            continue

        heapq.heappush(pqueue, (cost+1, (oreBots, claBots, obsBots, geoBots, ore, cla, obs, geo)))

        if oreoreCost < ore and oreBots < maxore:
            heapq.heappush(pqueue, (cost+1, (oreBots+1, claBots, obsBots, geoBots, ore-oreoreCost, cla, obs, geo)))

        if claoreCost < ore and claBots < maxcla:
            heapq.heappush(pqueue, (cost+1, (oreBots, claBots+1, obsBots, geoBots, ore-claoreCost, cla, obs, geo)))

        if obsoreCost < ore and obsclaCost < cla and obsBots < maxobs:
            heapq.heappush(pqueue, (cost+1, (oreBots, claBots, obsBots+1, geoBots, ore-obsoreCost, cla-obsclaCost, obs, geo)))

        if geoclaCost < cla and geoobsCost < obs:
            heapq.heappush(pqueue, (cost+1, (oreBots, claBots, obsBots, geoBots+1, ore, cla-geoclaCost, obs-geoobsCost, geo)))
        
    print(maxgeo, maxgeostate)
    return maxgeo

#data = open('data', 'r').read()
lines = data.split('\n')

blueprints = [ Blueprint(line) for line in lines ]

print(blueprints)

print(solve(blueprints[0]))
