import math

fname = 'test2.txt'

# part1

def moveTail(head, tail, hprev):
    if int(math.sqrt((head[0]-tail[0])**2 + (head[1]-tail[1])**2)) > 1:
        return hprev
    return tail

def walk(f):
    hx = hy = 0
    tpos = (0,0)
    positions = set([tpos])

    for move in f:
        dr, spaces = move.strip().split(" ")
        spaces = int(spaces)

        # could maybe optimze to skipt this when spaces > 3?? but calculating positions of tail...
        for _ in range(spaces):
            hprev = (hx, hy)
            if dr == 'R':
                hx += 1
            elif dr == 'L':
                hx -= 1
            elif dr == 'U':
                hy += 1
            else:
                hy -= 1
    
            # compute tail move
            tpos = moveTail((hx,hy), tpos, hprev)

            positions.add(tpos)
    return positions

with open(fname) as f:
    allTailSpots = walk(f)
    print(f"positions seen by tail: {len(allTailSpots)}")

# part 2

def moveKnotN(head, tail, hprev):
    if int(math.sqrt((head[0]-tail[0])**2 + (head[1]-tail[1])**2)) > 1:
        # TODO: need to move
        newPos = 'TODO'
        return newPos, tail
    return tail, tail

def walkN(f, n):
    hx = hy = 0
    tposN = [(0,0)]*(n-1) # -1 since head included in n
    positions = set([tposN[0]])

    for move in f:
        dr, spaces = move.strip().split(" ")
        spaces = int(spaces)

        #move head
        for _ in range(spaces):
            hprev = (hx, hy)
            if dr == 'R':
                hx += 1
            elif dr == 'L':
                hx -= 1
            elif dr == 'U':
                hy += 1
            else:
                hy -= 1
    
            # compute tail moves
            knotPrev = hprev
            for i in range(n-1):
                leader = tposN[i-1] if i-1 >= 0 else (hx, hy)
                newPos, knotPrev = moveKnotN(leader, tposN[i], knotPrev)
                if tposN[i] != newPos:
                    tposN[i] = newPos
                else:
                    break # other tails wont move either

            positions.add(tposN[-1]) # add nth knot to positions list
    return positions

def printpos(pos):
    minx = min(map(lambda x: x[0], pos))
    miny = min(map(lambda x: x[1], pos))
    maxx = max(map(lambda x: x[0], pos))
    maxy = max(map(lambda x: x[1], pos))

    xshift = 0 - minx
    yshift = 0 - miny
    coords = list(map(lambda x: (x[0] + xshift, x[1] + yshift), pos))

    grid = [['.' for _ in range(maxx + xshift + 1)] for _ in range(maxy + yshift + 1)]
    for x,y in coords:
        grid[y][x] = '#'

    for row in grid:
        print(''.join(row))

with open(fname) as f:
    longTailSpots = walkN(f, 10)
    printpos(longTailSpots)
    print(f"seen by tail len 10: {len(longTailSpots)}")
