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

#data = open('data', 'r').read()
lines = data.split('\n')
valves = parse(lines)

graph = {}
for id in valves:
    graph[id] = valves[id].exits

shortest = shortest_path_lengths(graph)

for id in valves:
    valves[id].shortest = shortest[id]

voi = [id for id in valves if valves[id].rate > 0]

print(voi)

def solve2(t1, loc1, t2, loc2, valves, voi):
    if t1 < 1:
        return 0

    max = 0
    for id in voi:
        rest = list(voi)
        rest.remove(id)

        dis = valves[loc1].shortest[id]
        score = solve2(t1-dis-1, id, t2, loc2, valves, rest)

        if score > max:
            max = score

        dis = valves[loc2].shortest[id]
        score = solve2(t2-dis-1, id, t1, loc1, valves, rest)

        if score > max:
            max = score

    release = valves[loc1].rate * t1 

    #print("solve2 {} {} {} {} {} {} {}".format(t1, loc1, t2, loc2, voi, release, max))

    return release + max

score = solve2(26, 'AA', 26, 'AA', valves, voi)
print(score)
