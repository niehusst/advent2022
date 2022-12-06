from collections import defaultdict

fname = 'input.txt'

# part 1

def getStacks(crates):
    stacks = defaultdict(lambda: [])
    # skip last row of column numbers
    for row in crates.split("\n")[:-1]:
        for i, ch in enumerate(row):
            if ch.isupper():
                pos = (i // 4) + 1
                stacks[pos].insert(0, ch)
    return stacks

def printStacks(stacks):
    for k in sorted(stacks.keys()):
        print(f"{k} >", stacks[k])
    print()

def part1():
    f = open(fname, 'r')
    rawInput = f.read()
    f.close()
    cratesInit, commands = rawInput.split("\n\n")
    stacks = getStacks(cratesInit)
    
    printStacks(stacks)
    
    for cmd in commands.strip().split("\n"):
        quant, locs = cmd.split(' from ')
        quant = int(quant[5:])
        frm, to = map(lambda x: int(x), locs.split(' to '))
    
        for _ in range(quant):
            stacks[to].append(stacks[frm].pop(-1))
    
    print(''.join([stacks[k][-1] for k in sorted(stacks.keys())]))


# part2

def part2():
    f = open(fname, 'r')
    rawInput = f.read()
    f.close()
    cratesInit, commands = rawInput.split("\n\n")
    stacks = getStacks(cratesInit)
    
    for cmd in commands.strip().split("\n"):
        quant, locs = cmd.split(' from ')
        quant = int(quant[5:])
        frm, to = map(lambda x: int(x), locs.split(' to '))
    
        stacks[to] += stacks[frm][-quant:]
        stacks[frm] = stacks[frm][:-quant]
    
    print(''.join([stacks[k][-1] for k in sorted(stacks.keys())]))

part2()
