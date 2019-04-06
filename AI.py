import random
import game


'''
Places a given piece on a given board, where board is a 4x4 list of lists

'''
def placePiece(board, piece, difficulty):

    # Easy
    if (difficulty == game.Difficulty.EASY):
        (x, y) = getRandomCoords(board)
        board[y][x] = piece

    # Medium
    elif (difficulty == game.Difficulty.MEDIUM):
        coinFlip = random.uniform(0,1)
        if (coinFlip < 0.5):
            (x, y) = getRandomCoords(board)
            board[y][x] = piece
        else:
            coords = findBestBlock(board, piece)
            if (coords == None):
                coords = findBestSpot(board, piece)
                if (coords == None):
                    
                    (x, y) = getRandomCoords(board)
                
                else:
                    (x, y) = (coords[0], coords[1])
            else:
                (x, y) = (coords[0], coords[1])
        board[y][x] = piece


    # Hard
    else:
        coords = findBestBlock(board, piece)
        if (coords == None):
            coords = findBestSpot(board, piece)
            if (coords == None):
                
                (x, y) = getRandomCoords(board)
                
            else:
                (x, y) = (coords[0], coords[1])
        else:
            (x, y) = (coords[0], coords[1])
        board[y][x] = piece
    return piece

'''
Picks a piece out of a given pool of pieces

'''
def pickPiece(board, pieces, difficulty):

    # Easy
    if (difficulty == game.Difficulty.EASY):
        piece = getRandomPiece(pieces)

    # Medium
    elif (difficulty == game.Difficulty.MEDIUM):
        coinFlip = random.uniform(0,1)
        if (coinFlip < 0.5):
            piece = getRandomPiece(pieces)
        else:
            piece = findWorstPiece(board, pieces)

    # Hard
    else:
        piece = findWorstPiece(board, pieces)
    return piece

     
'''
Generates a random set of coordinates for an empty slot in a 4x4 list of lists

'''
def getRandomCoords(board):
    x = random.randint(0, 3)
    y = random.randint(0, 3)

    while (board[y][x] != None):
        x = random.randint(0, 3)
        y = random.randint(0, 3)

        

    return (x, y)

'''
Generates a random piece out of a pool of pieces

'''
def getRandomPiece(pieces):
    x = random.randint(0,15)
    while (len(pieces[x]) == 0):
        x = random.randint(0,15)

    return pieces[x].pop()

'''
Finds the worst piece on a given board, defined as either a random piece or one that isn't an optimal piece

'''
def findWorstPiece(board, pieces):
    for x in range(16):
        if (len(pieces[x]) > 0):
            if (findBestSpot(board, pieces[x][0]) == None):
                #possibly = pieces[x]
                return pieces[x].pop()

    return getRandomPiece(pieces)

'''
Picks a piece which has 3 of the same type placed in a row on the board with the 4th slot free

'''
def findBestSpot(board, piece):
    countPieces = 0
    countFreeSpots = 0
    possibleBestSpot = None

    piece0 = None
    piece1 = None
    piece3 = None
    
    # Count rows
    for x in range(4):
        for y in range(4):
            if (board[y][x] != None):                
                if (board[y][x].equal(piece)):
                    countPieces += 1
                else:
                    possibleBestSpot = None
            else:
                countFreeSpots += 1
                possibleBestSpot = (x, y)

        if (countPieces == 3 and countFreeSpots == 1):        
            return possibleBestSpot
        countPieces = 0
        countFreeSpots = 0
        possibleBestSpot = None

    # Count columns
    for y in range(4):
        for x in range(4):
            if (board[y][x] != None):                
                if (board[y][x].equal(piece)):
                    countPieces += 1
                else:
                    possibleBestSpot = None
            else:
                countFreeSpots += 1
                possibleBestSpot = (x, y)

        if (countPieces == 3 and countFreeSpots == 1):
            return possibleBestSpot
        countPieces = 0
        countFreeSpots = 0
        possibleBestSpot = None

    # Count diagonals
    x = 0
    for y in range(4):

        if (board[y][x] != None):
            if (board[y][x].equal(piece)):
                countPieces += 1
            else:
                possibleBestSpot = None
        else:
            countFreeSpots += 1
            possibleBestSpot = (x, y)
        x += 1
    if (countPieces == 3 and countFreeSpots == 1):
        return possibleBestSpot
    
    countPieces = 0
    countFreeSpots = 0
    possibleBestSpot = None

    # Count diagonals
    y = 3
    for x in range(4):
        if (board[y][x] != None):
            if (board[y][x].equal(piece)):
                countPieces += 1
            else:
                possibleBestSpot = None
        else:
            countFreeSpots += 1
            possibleBestSpot = (x, y)
        y -= 1
    if (countPieces == 3 and countFreeSpots == 1):
        return possibleBestSpot
    
    countPieces = 0
    countFreeSpots = 0
    possibleBestSpot = None

    

    return possibleBestSpot


def findBestBlock(board, piece):
    countPieces = 0
    countFreeSpots = 0
    possibleBestSpot = None

    # Count rows
    for x in range(4):
        for y in range(4):
            if (board[y][x] != None):                
                if (not board[y][x].equal(piece)):
                    countPieces += 1
                else:
                    possibleBestSpot = None
            else:
                countFreeSpots += 1
                possibleBestSpot = (x, y)

        if (countPieces == 3 and countFreeSpots == 1):        
            return possibleBestSpot
        countPieces = 0
        countFreeSpots = 0
        possibleBestSpot = None

    # Count columns
    for y in range(4):
        for x in range(4):
            if (board[y][x] != None):                
                if (not board[y][x].equal(piece)):
                    countPieces += 1
                else:
                    possibleBestSpot = None
            else:
                countFreeSpots += 1
                possibleBestSpot = (x, y)

        if (countPieces == 3 and countFreeSpots == 1):
            return possibleBestSpot
        countPieces = 0
        countFreeSpots = 0
        possibleBestSpot = None

    # Count diagonals
    x = 0
    for y in range(4):

        if (board[y][x] != None):
            if (not board[y][x].equal(piece)):
                countPieces += 1
            else:
                possibleBestSpot = None
        else:
            countFreeSpots += 1
            possibleBestSpot = (x, y)
        x += 1
    if (countPieces == 3 and countFreeSpots == 1):
        return possibleBestSpot
    
    countPieces = 0
    countFreeSpots = 0
    possibleBestSpot = None

    # Count diagonals
    y = 3
    for x in range(4):
        if (board[y][x] != None):
            if (not board[y][x].equal(piece)):
                countPieces += 1
            else:
                possibleBestSpot = None
        else:
            countFreeSpots += 1
            possibleBestSpot = (x, y)
        y -= 1
    if (countPieces == 3 and countFreeSpots == 1):
        return possibleBestSpot
    
    countPieces = 0
    countFreeSpots = 0
    possibleBestSpot = None

    

    return possibleBestSpot


def findSecondBestSpot(board, piece):
    countPieces = 0
    countFreeSpots = 0
    possibleBestSpot = None

    # Count rows
    for x in range(4):
        for y in range(4):
            if (board[y][x] != None):                
                if (board[y][x].equal(piece)):
                    countPieces += 1
                else:
                    possibleBestSpot = None
            else:
                countFreeSpots += 1
                possibleBestSpot = (x, y)

        if (countPieces == 2 and countFreeSpots == 2):
            return possibleBestSpot
        countPieces = 0
        countFreeSpots = 0
        possibleBestSpot = None

    # Count columns
    for y in range(4):
        for x in range(4):
            if (board[y][x] != None):                
                if (board[y][x].equal(piece)):
                    countPieces += 1
                else:
                    possibleBestSpot = None
            else:
                countFreeSpots += 1
                possibleBestSpot = (x, y)

        if (countPieces == 2 and countFreeSpots == 2):
            return possibleBestSpot
        countPieces = 0
        countFreeSpots = 0
        possibleBestSpot = None

    # Count diagonals
    x = 0
    for y in range(4):

        if (board[y][x] != None):
            if (board[y][x].equal(piece)):
                countPieces += 1
            else:
                possibleBestSpot = None
        else:
            countFreeSpots += 1
            possibleBestSpot = (x, y)
        x += 1
    if (countPieces == 2 and countFreeSpots == 2):
        return possibleBestSpot
    
    countPieces = 0
    countFreeSpots = 0
    possibleBestSpot = None

    # Count diagonals
    y = 3
    for x in range(4):
        if (board[y][x] != None):
            if (board[y][x].equal(piece)):
                countPieces += 1
            else:
                possibleBestSpot = None
        else:
            countFreeSpots += 1
            possibleBestSpot = (x, y)
        y -= 1
    if (countPieces == 2 and countFreeSpots == 2):
        return possibleBestSpot
    
    countPieces = 0
    countFreeSpots = 0
    possibleBestSpot = None

    

    return possibleBestSpot
