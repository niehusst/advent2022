fname = 'input.txt'

#part1


def checkFreq(cycle, rX, offset, period, freq):
    if (cycle - offset) % period == 0:
        freq.append(rX * cycle)


with open(fname) as f:
    cycleOffset = 20
    cyclePeriod = 40
    rX = 1 #init register value
    cycle = 1
    frequencies = []
    for cmd in f:
        cmd = cmd.strip()
        if cmd == 'noop':
            cycle += 1
            checkFreq(cycle, rX, cycleOffset, cyclePeriod, frequencies)
            continue
        # we know op is addx
        _, value = cmd.split(' ')
        cycle += 1
        checkFreq(cycle, rX, cycleOffset, cyclePeriod, frequencies)
        cycle += 1
        rX += int(value)
        checkFreq(cycle, rX, cycleOffset, cyclePeriod, frequencies)
    print(f"signal strength sum: {sum(frequencies)}")

# part 2

def drawCrt(crt, rX, cycle, period):
    row = cycle // period
    col = cycle % period
    if col >= rX - 1 and col <= rX + 1:
        crt[row][col] = '#'
    # no else because position is already marked dark

def printCrt(crt):
    for row in crt:
        print(''.join(row))

def debug(crt, cycle, cmd, rx):
    return
    p = 40
    r = cycle // p
    c = cycle % p
    sprite = ['#' if i >= rx-1 and i <= rx+1 else '.' for i in range(p)]
    print(f"sprite at: {''.join(sprite)}")
    print(f"executing {cmd} ...")
    print(f"c: {cycle}, r: {rx}")
    print(f"curr crt:  {''.join(crt[r][:c+1])}")
    print()

with open(fname) as f:
    cyclePeriod = 40
    rX = 1 #init register value
    cycle = 0
    crtH = 6
    crtW = 40
    crt = [['.' for _ in range(crtW)] for _ in range(crtH)]

    for cmd in f:
        cmd = cmd.strip()
        if cmd == 'noop':
            drawCrt(crt, rX, cycle, cyclePeriod)
            cycle += 1
            debug(crt, cycle, cmd, rX)
            continue
        # we know op is addx
        _, value = cmd.split(' ')
        drawCrt(crt, rX, cycle, cyclePeriod)
        cycle += 1
        debug(crt, cycle, cmd, rX)

        drawCrt(crt, rX, cycle, cyclePeriod)
        cycle += 1
        rX += int(value)
        debug(crt, cycle, cmd, rX)
    printCrt(crt)
