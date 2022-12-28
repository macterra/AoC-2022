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

    maxt = 24

    while len(pqueue) > 0:
        minutes, state = pqueue.popleft()

        if minutes > maxt:
            continue
        
        #print(minutes, state, len(pqueue), maxgeo)

        if (state) in visited:
            continue

        visited.add(state)

        oreBots, claBots, obsBots, geoBots, ore, cla, obs, geo = state

        if geo > maxgeo:
            maxgeo = geo
            maxgeostate = state
            print(minutes, maxgeo, maxgeostate)

        if claBots == 0 and (obsclaCost + geoobsCost + minutes) > maxt:
            continue

        if obsBots == 0 and (geoobsCost + minutes) > maxt:
            continue

        if geoBots == 0 and (maxgeo + minutes) > maxt:
            continue

        if oreBots < maxore:
            needore = oreoreCost - ore
            t = max(0, int(needore/oreBots + 0.5)) + 1
            nore = ore + t*oreBots - oreoreCost
            ncla = cla + t*claBots
            nobs = obs + t*obsBots
            ngeo = geo + t*geoBots
            pqueue.append((minutes+t, (oreBots+1, claBots, obsBots, geoBots, nore, ncla, nobs, ngeo)))

        if claBots < maxcla:
            needore = claoreCost - ore
            t = max(0, int(needore/oreBots + 0.5)) + 1
            nore = ore + t*oreBots - claoreCost
            ncla = cla + t*claBots
            nobs = obs + t*obsBots
            ngeo = geo + t*geoBots
            pqueue.append((minutes+t, (oreBots, claBots+1, obsBots, geoBots, nore, ncla, nobs, ngeo)))

        if claBots > 0 and obsBots < maxobs:
            needore = obsoreCost - ore
            needcla = obsclaCost - cla
            t = max(0, int(needore/oreBots + 0.5), int(needcla/claBots + 0.5)) + 1
            nore = ore + t*oreBots - obsoreCost
            ncla = cla + t*claBots - obsclaCost
            nobs = obs + t*obsBots
            ngeo = geo + t*geoBots
            pqueue.append((minutes+t, (oreBots, claBots, obsBots+1, geoBots, nore, ncla, nobs, ngeo)))

        if obsBots > 0:
            needore = geooreCost - ore
            needobs = geoobsCost - obs
            t = max(0, int(needore/oreBots + 0.5), int(needobs/obsBots + 0.5)) + 1
            nore = ore + t*oreBots - geooreCost
            ncla = cla + t*claBots
            nobs = obs + t*obsBots - geoobsCost
            ngeo = geo + t*geoBots
            pqueue.append((minutes+t, (oreBots, claBots, obsBots, geoBots+1, nore, ncla, nobs, ngeo)))

        if geoBots > 0:
            nore = ore + oreBots
            ncla = cla + claBots
            nobs = obs + obsBots
            ngeo = geo + geoBots
            pqueue.append((minutes+1, (oreBots, claBots, obsBots, geoBots, nore, ncla, nobs, ngeo)))

    print(maxgeostate, maxgeo)
    return maxgeo

#data = open('data', 'r').read()
lines = data.split('\n')
blueprints = [ Blueprint(line) for line in lines ]

print(solve(blueprints[0].costs))
