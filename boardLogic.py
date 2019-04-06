from gamePiece import Color, Shape, Piece, OuterColor, OuterShape
import userInput
import prints
import game

'''

Board logic

'''

def checkEquality(piece1, piece2, piece3, piece4):
    return (piece1.equals(piece2, piece3, piece4) and
            piece2.equals(piece1, piece3, piece4) and
            piece3.equals(piece1, piece2, piece4) and
            piece4.equals(piece1, piece2, piece3))


'''
Checks if 4 aligned pieces are the same on the board. Returns True if game is won, False otherwise.

'''
def determineState(board, piece):

    for x in range(4):
        if (board[0][x] != None and
            board[1][x] != None and
            board[2][x] != None and
            board[3][x] != None):
            return checkEquality(board[0][x], board[1][x], board[2][x], board[3][x])
                                

        if (board[x][0] != None and
            board[x][1] != None and
            board[x][2] != None and
            board[x][3] != None):
            return checkEquality(board[x][0], board[x][1], board[x][2], board[x][3])

    if (board[0][0] != None and
        board[1][1] != None and
        board[2][2] != None and
        board[3][3] != None):
        return checkEquality(board[0][0], board[1][1], board[2][2], board[3][3])

    if (board[0][3] != None and
        board[1][2] != None and
        board[2][1] != None and
        board[3][0] != None):

        return checkEquality(board[0][3], board[1][2], board[2][1], board[3][0])
        
    return False


'''
Updates the board at coordinates (x, y) with a given piece

'''
def updateBoard(board, piece, x, y):
    board[y][x] = piece;

'''
Generates an empty board. Empty slots are defined as None

'''
def createBoard():
    board = [[None for x in range(4)] for y in range(4)]
    return board

'''
Generates a pool of pieces from which moves can be made

'''
def createPieces():
    
    #crosses = [Piece(0, 0, 0, 0) for x in range(8)]
    #circles = [Piece(1, 1, 1, 1) for x in range(8)]


    pieces = [[Piece(0, 0, 0, 0)],
              [Piece(0, 0, 0, 1)],
              [Piece(0, 0, 1, 0)],
              [Piece(0, 0, 1, 1)],
              [Piece(0, 1, 0, 0)],
              [Piece(0, 1, 0, 1)],
              [Piece(0, 1, 1, 0)],
              [Piece(0, 1, 1, 1)],
              [Piece(1, 0, 0, 0)],
              [Piece(1, 0, 0, 1)],
              [Piece(1, 0, 1, 0)],
              [Piece(1, 0, 1, 1)],
              [Piece(1, 1, 0, 0)],
              [Piece(1, 1, 0, 1)],
              [Piece(1, 1, 1, 0)],
              [Piece(1, 1, 1, 1)]]
              
              
    
   # pieces = [crosses, circles]
    
    return pieces

'''
Checks if board is empty

'''
def isEmpty(board):
    for x in range(4):
        for y in range(4):
            if (board[y][x] != None):
                return False
    return True

'''
Determines who has won the game

'''
def endGame(board, piece, turn, player, opponent):
    choice = False
    
    win = determineState(board, piece)
    if (win and turn == game.Turn.PLAYER):        
        prints.printFancyBoard(board, turn, player, opponent)
        print('      ', end='')
        prints.eprint(player, prints.sf.GREEN, True, False)
        prints.eprint(' won!', prints.sf.WHITE, True, True)
        choice = userInput.askToPlayAgain()
        
    elif (win and turn == game.Turn.OPPONENT):
        prints.printFancyBoard(board, turn, player, opponent)
        print('      ', end='')
        prints.eprint(opponent, prints.sf.RED, True, False)
        prints.eprint(' won!', prints.sf.WHITE, True, True)
        choice = userInput.askToPlayAgain()

        
    elif (not win and not movesRemaining(board)):
        prints.printFancyBoard(board, turn, player, opponent)
        prints.eprint('It\'s a tie!', prints.sf.YELLOW, True, True)
        choice = userInput.askToPlayAgain()
    return choice


def endGameNoReplay(board, piece, turn, player, opponent):
    choice = False
    
    win = determineState(board, piece)
    if (win and turn == game.Turn.PLAYER):        
        prints.printFancyBoard(board, turn, player, opponent)
        print('      ', end='')
        prints.eprint(player, prints.sf.GREEN, True, False)
        prints.eprint(' won!', prints.sf.WHITE, True, True)
        return player
        
    elif (win and turn == game.Turn.OPPONENT):
        prints.printFancyBoard(board, turn, player, opponent)
        print('      ', end='')
        prints.eprint(opponent, prints.sf.RED, True, False)
        prints.eprint(' won!', prints.sf.WHITE, True, True)
        return opponent

        
    elif (not win and not movesRemaining(board)):
        prints.printFancyBoard(board, turn, player, opponent)
        prints.eprint('It\'s a tie!', prints.sf.YELLOW, True, True)
        return 'DRAW'
    return 'NONE'

'''
Returns True if there are possible moves remaining. False if board is full

'''
def movesRemaining(board):
    for x in range(4):
        for y in range(4):
            if (board[y][x] == None):
                return True
    return False
