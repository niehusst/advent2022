#part 1

def priority(item):
    if item.isupper():
        return ord(item) - 38
    return ord(item) - 96

def findCommonItem(rucksack):
    pivot = len(rucksack) // 2
    comp1 = set(list(rucksack[:pivot]))
    comp2 = set(list(rucksack[pivot:]))
    return comp1.intersection(comp2).pop()

with open('input.txt') as f:
    pscore = sum([priority(findCommonItem(line.strip())) for line in f])
    print(f"priority sum: {pscore}") 

# part2

with open('input.txt') as f:
    groupScoreSum = 0
    counter = 0
    group = []
    for line in f:
        rucksack = line.strip()
        group.append(set(list(rucksack)))
        counter += 1
        if counter > 2:
            badge = group[0].intersection(group[1]).intersection(group[2]).pop()
            groupScoreSum += priority(badge)
            counter = 0
            group = []

    print(f"group sum: {groupScoreSum}")
