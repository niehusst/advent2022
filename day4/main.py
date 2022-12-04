fname = 'input.txt'

#part1 

def contains(r1, r2):
    return r1[0] <= r2[0] and r1[1] >= r2[1]

with open(fname) as f:
    dupedWork = 0
    for line in f:
        r1, r2 = [tuple(map(int, r.split('-'))) for r in line.strip().split(',')]
        if contains(r1, r2) or contains(r2, r1):
            dupedWork += 1
    print(f"dupped: {dupedWork}")

# part 2

def overlap(r1, r2):
    return r2[0] <= r1[0] <= r2[1] or r2[0] <= r1[1] <= r2[1]

with open(fname) as f:
    overlapWork = 0
    for line in f:
        r1, r2 = [tuple(map(int, r.split('-'))) for r in line.strip().split(',')]
        if overlap(r1, r2) or overlap(r2, r1):
            overlapWork += 1
    print(f"overlapping: {overlapWork}")
