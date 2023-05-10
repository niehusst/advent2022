# part 1

def moveScore(move):
    if move == 'X':
        return 1
    elif move == 'Y':
        return 2
    else:
        return 3

def outcomeScore(enemyMove, myMove):
    if enemyMove == 'A' and myMove == 'X' or \
        enemyMove == 'B' and myMove == 'Y' or \
        enemyMove == 'C' and myMove == 'Z':
        return 3
    elif enemyMove == 'A' and myMove == 'Y' or \
        enemyMove == 'B' and myMove == 'Z' or \
        enemyMove == 'C' and myMove == 'X':
        return 6
    else:
        return 0

def calcScore(enemyMove, myMove):
    return moveScore(myMove) + outcomeScore(enemyMove, myMove)

with open('input.txt') as f:
    score = 0
    
    for line in f:
        enemyMove, myMove = line.strip().split(' ')
        if myMove == None:
            continue
        score += calcScore(enemyMove, myMove)

    print(f"final score: {score}")

# part 2

def getMyMove(enemyMove, outcome):
    if outcome == 'X' and enemyMove == 'A' or \
        outcome == 'Z' and enemyMove == 'B' or \
        outcome == 'Y' and enemyMove == 'C':
        return 'C'
    elif outcome == 'X' and enemyMove == 'B' or \
        outcome == 'Z' and enemyMove == 'C' or \
        outcome == 'Y' and enemyMove == 'A':
        return 'A'
    else:
        return 'B'

def nmoveScore(move):
    if move == 'A':
        return 1
    elif move == 'B':
        return 2
    else:
        return 3

def noutcomeScore(outcome):
    if outcome == 'X':
        return 0
    elif outcome == 'Y':
        return 3
    else:
        return 6

def ncalcScore(enemyMove, outcome):
    myMove = getMyMove(enemyMove, outcome)
    return nmoveScore(myMove) + noutcomeScore(outcome)

with open('input.txt') as f:
    score = 0
    
    for line in f:
        enemyMove, outcome = line.strip().split(' ')
        if myMove == None:
            continue
        score += ncalcScore(enemyMove, outcome)

    print(f"final score: {score}")

# part 3

# calculate ELO rating of the game
game_result = calc_game_results()

def get_elo(score1, score2):
    if score1 > score2:
        return '1400'
    elif score1 < score2:
        return '1203'
    else:
        return 'not a valid elo score'

with open('input.txt') as f:
    for line in f:
        if get_elo(line.split()) == '1400':
            game_result -= 1
    print(f"final elo score is {game_result}")
