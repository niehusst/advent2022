fname = 'test.txt'

# part 1

# takes file stream, returns a monkey if there are any left in stream
def parseMonkey(f):
    monkey = None
    for line in f:
        line = line.strip()
        if not line:
            return monkey

        components = line.split(' ')
        if components[0] == 'Monkey':
            monkey = Monkey(int(components[1][:-1]))
        elif components[0] == 'Starting':
            items = list(map(Item, map(int, line.split(':')[1].split(','))))
            monkey.items = items
        elif components[0] == 'Operation:':
            str_op = line.split(' = ')[1]
            monkey.worryOp = lambda worry: eval(str_op.replace('old', str(worry)))
        elif components[0] == 'Test:':
            testDivisor = int(line.split('by ')[1])
            trueMonkeyTarget = int(next(f).split(' ')[-1])
            falseMonkeyTarget = int(next(f).split(' ')[-1])
            monkey.test = lambda worry: falseMonkeyTarget if worry % testDivisor else trueMonkeyTarget
    return monkey


class Item:
    def __init__(self, worry):
        self.worry = worry

    def __repr__(self):
        return f"Item(worry: {self.worry})"

class Monkey:
    items = []
    inspections = 0
    test = None
    worryOp = None

    def __init__(self, index):
        self.index = index
    
    def __repr__(self):
        return f"Monkey(items: {self.items}, inspections: {self.inspections})"

    def take_turn(self, monkeys, isRelieved=True):
        """
        monkeys is a dict of all monkeys available
        """
        self.inspections += len(self.items)
        for item in self.items:
            # update worry based on how monkey handles
            item.worry = self.worryOp(item.worry)

            # then divide by 3 if relieved 
            if isRelieved:
                item.worry = item.worry // 3

            # monkey tests item and throws to other monkey
            monkeyReciever = self.test(item.worry)
            monkeys[monkeyReciever].items.append(item)
        
        # monkey threw away all its items
        self.items = []

with open(fname) as f:
    monkeys = {}
    monkey = parseMonkey(f)
    while monkey:
        monkeys[monkey.index] = monkey
        monkey = parseMonkey(f)

    # monkeys have been parsed. now throw items
    rounds = 20
    for _ in range(rounds):
        # all monkeys throw each round
        for mon_key in monkeys.keys(): # get it? mon_key? monkey key??
            monkeys[mon_key].take_turn(monkeys)

    # get top 2 monkeys who did most inspections
    sortedMonkeys = sorted(monkeys.values(), key=lambda monkey: monkey.inspections)
    print(f"monkey buisness: {sortedMonkeys[-1].inspections * sortedMonkeys[-2].inspections}")

# part 2

# we need big int...
#import sys
#sys.set_int_max_str_digits(199000)

# big int not helping.
# use the values that the monkey tests on to keep the worry values low enough to use? (worry = worry % testValue) or something

with open(fname) as f:
    monkeys = {}
    monkey = parseMonkey(f)
    while monkey:
        monkeys[monkey.index] = monkey
        monkey = parseMonkey(f)

    # monkeys have been parsed. now throw items
    rounds = 10000
    for _ in range(rounds):
        # all monkeys throw each round
        for mon_key in monkeys.keys(): # get it? mon_key? monkey key??
            monkeys[mon_key].take_turn(monkeys, False)

    # get top 2 monkeys who did most inspections
    sortedMonkeys = sorted(monkeys.values(), key=lambda monkey: monkey.inspections)
    print(f"monkey buisness: {sortedMonkeys[-1].inspections * sortedMonkeys[-2].inspections}")
