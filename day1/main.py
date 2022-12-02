# part1
mostCalories = 0

with open('input.txt') as f:
    currElfCals = 0

    for line in f.readlines():
        if line.strip().isnumeric():
            currElfCals += int(line)
        else:
            mostCalories = max(mostCalories, currElfCals)
            currElfCals = 0
    mostCalories = max(mostCalories, currElfCals)
    currElfCals = 0

print(f"fatest elf has {mostCalories}")

#part 2
import heapq

with open('input.txt') as f:
    currElfCals = 0
    elfHeap = []

    for line in f.readlines():
        if line.strip().isnumeric():
            currElfCals += int(line)
        else:
            heapq.heappush(elfHeap, currElfCals)
            currElfCals = 0
    heapq.heappush(elfHeap, currElfCals)
    currElfCals = 0

print(f"top elves are {sum(heapq.nlargest(3, elfHeap))}")
