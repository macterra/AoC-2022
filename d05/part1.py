data = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

def parseStacks(lines):
    lines.reverse()
    print(lines)
    rows = len(lines)
    n = len(lines[0].split('   '))
    stacks = [[] * n]
    print(stacks)
    print(n)
    for line in lines[1:]:
        print(line)

def parseMoves(lines):
    print(lines)

def parse(lines):
    i = 0
    while lines[i]:
        i += 1
    print(i)
    print(len(lines))
    parseStacks(lines[:i])
    parseMoves(lines[i+1:])

lines = data.split('\n')
parse(lines)
