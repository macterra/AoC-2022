import re
from shortest import shortest_path_lengths

data="""Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

class Valve:
    def __init__(self, id, rate, exits):
        self.id = id
        self.rate = rate
        self.exits = exits

    def __repr__(self) -> str:
        return "valve {} rate={} {}".format(self.id, self.rate, self.exits)

def parse(lines):
    valves = {}
    for line in lines:
        match = re.search("Valve ([A-Z]+) has flow rate=(\d+); tunnel[s]? lead[s]? to valve[s]? ([A-Z ,]+)", line)
        if match:
            id = match.group(1)
            rate = int(match.group(2))
            exits = match.group(3).split(', ')
            valves[id] = Valve(id, rate, exits)
        else:
            print('fail', line)
    return valves

data = open('data', 'r').read()
lines = data.split('\n')
valves = parse(lines)

graph = {}
for id in valves:
    graph[id] = valves[id].exits
    print(valves[id])
print(graph)

shortest = shortest_path_lengths(graph)
print(shortest)

for id in valves:
    valves[id].shortest = shortest[id]
    print(shortest[id])

voi = [id for id in valves if valves[id].rate > 0]

print(voi)

def solve(t, loc, valves, voi):
    if t < 1:
        return 0

    max = 0
    for id in voi:
        rest = list(voi)
        rest.remove(id)
        dis = valves[loc].shortest[id]
        score = solve(t-dis-1, id, valves, rest)
        if score > max:
            max = score

    release = valves[loc].rate * t
    print("solve {} {} {} {} {}".format(t, loc, voi, release, max))

    return release + max

def solve2(t1, mloc, t2, eloc, valves, voi):
    if t1 < 1:
        return solve(t2, eloc, valves, voi)

    if t2 < 1:
        return solve(t1, mloc, valves, voi)

    max = 0
    for id1 in voi:
        rest = list(voi)
        rest.remove(id1)

        for id2 in rest:
            rest2 = list(rest)
            rest2.remove(id2)

            dis1 = valves[mloc].shortest[id1]
            dis2 = valves[eloc].shortest[id2]

            score = solve2(t1-dis1-1, id1, t2-dis2-1, id2, valves, rest2)
            if score > max:
                max = score
                
            dis1 = valves[mloc].shortest[id2]
            dis2 = valves[eloc].shortest[id1]

            score = solve2(t1-dis1-1, id2, t2-dis2-1, id1, valves, rest2)
            if score > max:
                max = score

    release = 0

    if t1 > 0:
        release += valves[mloc].rate * t1 
    if t2 > 0:
        release += valves[eloc].rate * t2

    print("solve2 {} {} {} {} {} {} {}".format(t1, mloc, t2, eloc, voi, release, max))

    return release + max

score = solve2(26, 'AA', 26, 'AA', valves, voi)
print(score)
