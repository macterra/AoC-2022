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
    maxoreBots = max(oreoreCost, claoreCost, obsoreCost, geooreCost)
    maxclaBots = obsclaCost
    maxobsBots = geoobsCost
    
    state = (1, 0, 0, 0, 0, 0, 0, 0)
    pqueue = deque([(0, state)])
    visited = set()

    maxt = 24

    while len(pqueue) > 0:
        minutes, state = pqueue.popleft()

        if minutes > maxt:
            continue
        
        #print(minutes, state, len(pqueue), maxgeo)

        if state in visited:
            continue

        visited.add(state)

        oreBots, claBots, obsBots, geoBots, ore, cla, obs, geo = state

        if geo > maxgeo:
            maxgeo = geo
            maxgeostate = state
            print(minutes, maxgeo, maxgeostate)

        if claBots == 0 and (obsclaCost + geoobsCost + minutes + 3) > maxt:
            continue

        if obsBots == 0 and (geoobsCost + minutes + 2) > maxt:
            continue

        if geoBots == 0 and (maxgeo + minutes + 1) > maxt:
            continue

        if obsBots > 0:
            needore = geooreCost - ore
            needobs = geoobsCost - obs
            t = 1 + max(0, int(needore/oreBots + 0.5), int(needobs/obsBots + 0.5))
            pqueue.append((minutes+t, (
                oreBots, claBots, obsBots, geoBots+1, 
                ore + t*oreBots - geooreCost, 
                cla + t*claBots, 
                obs + t*obsBots - geoobsCost, 
                geo + t*geoBots)))

        if claBots > 0 and obsBots < maxobsBots:
            needore = obsoreCost - ore
            needcla = obsclaCost - cla
            t = 1 + max(0, int(needore/oreBots + 0.5), int(needcla/claBots + 0.5))
            pqueue.append((minutes+t, (
                oreBots, claBots, obsBots+1, geoBots, 
                ore + t*oreBots - obsoreCost, 
                cla + t*claBots - obsclaCost, 
                obs + t*obsBots, 
                geo + t*geoBots)))

        if claBots < maxclaBots:
            needore = claoreCost - ore
            t = 1 + max(0, int(needore/oreBots + 0.5))
            pqueue.append((minutes+t, (
                oreBots, claBots+1, obsBots, geoBots, 
                ore + t*oreBots - claoreCost, 
                cla + t*claBots, 
                obs + t*obsBots, 
                geo + t*geoBots)))

        if oreBots < maxoreBots:
            needore = oreoreCost - ore
            t = 1 + max(0, int(needore/oreBots + 0.5))
            pqueue.append((minutes+t, (
                oreBots+1, claBots, obsBots, geoBots, 
                ore + t*oreBots - oreoreCost, 
                cla + t*claBots, 
                obs + t*obsBots, 
                geo + t*geoBots)))

        if geoBots > 0:
            pqueue.append((minutes+1, (
                oreBots, claBots, obsBots, geoBots, 
                ore + oreBots, 
                cla + claBots, 
                obs + obsBots, 
                geo + geoBots)))

    print(maxgeostate, maxgeo)
    print(len(visited), (1,4,2,2,6,41,8,9) in visited)
    return maxgeo

#data = open('data', 'r').read()
lines = data.split('\n')
blueprints = [ Blueprint(line) for line in lines ]

print(solve(blueprints[0].costs))
