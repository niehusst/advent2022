fname = 'input.txt'

# part1

def readForest(f):
    forest = []
    for line in f:
        forest.append(list(map(int, list(line.strip()))))
    return forest

def buildStack(trees):
    stack = []
    for tree in trees[::-1]:
        prevMax = stack[-1] if stack else 0
        stack.append(max(tree, prevMax))
    return stack

def addMaxStack(stack, tree):
    stack.append(max(stackPeek(stack), tree))

def stackPeek(stack):
    return stack[-1] if stack else 0

def visibilityByPosition(forest):
    rows = len(forest)
    cols = len(forest[0])
    rowVis = [[(0,0) for _ in range(rows)] for _ in range(cols)]

    for row in range(rows):
        rstack = buildStack(forest[row])
        lstack = []
        for col in range(cols):
            # drain rstack, in case next largest is curr tree
            rstack.pop()

            rowVis[row][col] = (stackPeek(lstack), stackPeek(rstack))
            addMaxStack(lstack, forest[row][col])


    colVis = [[(0,0) for _ in range(rows)] for _ in range(cols)]

    for col in range(cols):
        dstack = buildStack([forest[r][col] for r in range(rows)])
        ustack = []
        for row in range(rows):
            # drain down stack
            dstack.pop()

            colVis[row][col] = (stackPeek(ustack), stackPeek(dstack))
            addMaxStack(ustack, forest[row][col])

    return [list(zip(rowVis[i], colVis[i])) for i in range(rows)]

def hiddenTrees(forest):
    vis = visibilityByPosition(forest)
#    for i in range(len(vis)):
#        for j in range(len(vis[0])):
#            v = vis[i][j]
#            print(f"pos {i},{j} as vis <^>v {v[0][0]},{v[1][0]},{v[0][1]},{v[1][1]}")
    hidden = 0
    for row in range(1, len(forest)-1):
        for col in range(1, len(forest[0])-1):
            tree = forest[row][col]
            horzVis, vertVis = vis[row][col]
            if tree <= horzVis[0] and tree <= horzVis[1] and tree <= vertVis[0] and tree <= vertVis[1]:
#                print(f"{row},{col} is hidden")
                hidden += 1
    return hidden

with open(fname) as f:
    forest = readForest(f)
    totalTrees = len(forest) * len(forest[0])
    hidden = hiddenTrees(forest)
    print(f"num visible trees: {totalTrees - hidden}")


# part 2

class Tree:
    def __init__(self, height, up=0, down=0, left=0, right=0):
        self.height = height
        self.up = up
        self.down = down
        self.left = left
        self.right = right

def addMaxDistStack(stack, tree, r, c):
    if stack and stack[-1][0] >= tree:
        stack.append(stack[-1])
    else:
        stack.append((tree, r, c))

def buildDistStackRow(trees, row):
    stack = []
    for i,tree in enumerate(trees[::-1]):
        prevMax = stack[-1] if stack else [0]
        m = prevMax
        if tree >= prevMax[0]:
            m = (tree, row, i)
        stack.append(m)
    return stack

def buildDistStackCol(trees, col):
    stack = []
    for i,tree in enumerate(trees[::-1]):
        prevMax = stack[-1] if stack else [0]
        m = prevMax
        if tree >= prevMax[0]:
            m = (tree, i, col)
        stack.append(m)
    return stack

def dstackPeek(stack):
    if not stack:
        return [0]*3
    return stack[-1]

def visibilityWithDist(forest):
    rows = len(forest)
    cols = len(forest[0])
    vis = [[Tree(forest[r][c]) for c in range(cols)] for r in range(rows)]
    for r in range(1, rows-1):
        for c in range(1, cols-1):
            tree = vis[r][c]
            # up
            for rowup in range(r-1, -1, -1):
                tree.up += 1
                if vis[rowup][c].height >= tree.height:
                    break

            # down
            for rowdown in range(r+1, rows):
                tree.down += 1
                if vis[rowdown][c].height >= tree.height:
                    break

            # left
            for colleft in range(c-1, -1, -1):
                tree.left += 1
                if vis[r][colleft].height >= tree.height:
                    break

            # right
            for colright in range(c+1, cols):
                tree.right += 1
                if vis[r][colright].height >= tree.height:
                    break
    return vis


#    treeVis = [[Tree(forest[r][c]) for c in range(cols)] for r in range(rows)]
#
#    for row in range(rows):
#        rstack = buildDistStackRow(forest[row], row)
#        lstack = []
#        for col in range(cols):
#            # drain rstack, in case next largest is curr tree
#            rstack.pop()
#
#            treeVis[row][col].left = abs(row - dstackPeek(lstack)[2])
#            treeVis[row][col].right = abs(row - dstackPeek(rstack)[2])
#            addMaxDistStack(lstack, forest[row][col], row, col)
#
#    for col in range(cols):
#        dstack = buildDistStackCol([forest[r][col] for r in range(rows)], col)
#        ustack = []
#        for row in range(rows):
#            # drain down stack
#            dstack.pop()
#
#            treeVis[row][col].up = abs(col - dstackPeek(ustack)[1])
#            treeVis[row][col].down = abs(col - dstackPeek(dstack)[1])
#            addMaxDistStack(ustack, forest[row][col], row, col)
#
#    return treeVis

def getScore(tree):
    return tree.right * tree.left * tree.up * tree.down

def getMostScenicTreeScore(forest):
    vis = visibilityWithDist(forest)

    maxScore = 0

    for row in range(1, len(vis)-1):
        for col in range(1, len(vis[0])-1):
#            if maxScore < getScore(vis[row][col]):
#                t = vis[row][col]
#                print(f"new max {getScore(vis[row][col])} at {row},{col} with <>^v {t.left},{t.right},{t.up},{t.down}")
            maxScore = max(maxScore, getScore(vis[row][col]))
          
    return maxScore

with open(fname) as f:
    forest = readForest(f)
    score = getMostScenicTreeScore(forest)
    print(f"most scenic: {score}")
