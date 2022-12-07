fname = 'input.txt'

#part 1

class FSNode:
    def __init__(self, name, parent, size = None, children = []):
        self.name = name
        self.parent = parent
        self.size = size
        self.children = children

    def __repr__(self):
        return str(self.name)

def buildFileTree(f):
    root = None
    currNode = None
    for line in f:
        line = line.strip()
        if line[0] == '$':
            # interprrt command
            cmd = line[2:].split(' ')
            if cmd[0] == 'ls' and currNode:
                currNode.children = []
            else:
                prev = currNode
                if cmd[1] == '..':
                    currNode = currNode.parent
                else:
                    # cd into child dir
                    if prev == None:
                        currNode = FSNode(cmd[1], currNode)
                        root = currNode
                        continue
                    tmp = None
                    for n in currNode.children:
                        if n.name == cmd[1]:
                            tmp = n
                            break
                    if not tmp:
                        tmp = FSNode(cmd[1], currNode)
                        currNode.children.append(tmp)
                    currNode = tmp
        else:
            # reading ls command output, add children
            size, name = line.split(' ')
            if size == 'dir':
                size = None
            currNode.children.append(FSNode(name, currNode, size))
    return root

def ptree(t):
    print(f"{t.parent} > {t}: {t.size}")
    for child in t.children:
        ptree(child)

def sumDirsUnder(tree, dirs, maxSize = 100000):
    runSum = 0
    for n in tree.children:
        if n.size:
            runSum += int(n.size)
        else:
            runSum += sumDirsUnder(n, dirs, maxSize)
    if runSum <= maxSize:
        dirs.append((runSum, tree.name))
    return runSum

f = open(fname, 'r')
tree = buildFileTree(f)
f.close()

mediumBois = []
sumDirsUnder(tree, mediumBois)
print(f"sum of files under 100000: {sum(map(lambda x: x[0], mediumBois))}")

# part 2

def totalSum(t):
    runSum = 0
    for n in t.children:
        if n.size:
            runSum += int(n.size)
        else:
            runSum += totalSum(n)
    return runSum

diskSize = 70000000
requiredSpace = 30000000

currSpace = diskSize - totalSum(tree)
spaceToClear = requiredSpace - currSpace

allDirSizes = []
sumDirsUnder(tree, allDirSizes, float('inf'))
for size,dname in sorted(allDirSizes):
    if size >= spaceToClear:
        print(f"smallest dir to delete is {dname} with size {size} ({spaceToClear} required, bigger by {size - spaceToClear})")
        break

