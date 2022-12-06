fname = 'input.txt'

#part1

#start of packet
sopLen = 4

sop = None

with open('input.txt') as f:
    data = f.read().strip()

    for i in range(len(data)-sopLen):
        if len(set(data[i:i+sopLen])) == sopLen:
            sop = i + sopLen
            print(f"SOP ends at {sop}")
            break

# part2

somLen = 14
som = None

with open('input.txt') as f:
    data = f.read().strip()

    for i in range(len(data)-somLen):
        if len(set(data[i:i+somLen])) == somLen:
            som = i + somLen
            print(f"SOM ends at {som}")
            break

