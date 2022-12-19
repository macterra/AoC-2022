import re

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

data = open('data', 'r').read()
lines = data.split('\n')

blueprints = [ Blueprint(line) for line in lines ]

print(blueprints)