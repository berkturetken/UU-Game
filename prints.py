#from termcolor import colored, cprint

from game import Turn

class sf:
    
    BOLD = '\033[01m'
    RED = '\033[31m'
    CYAN = '\033[36m'
    YELLOW = '\033[93m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    WHITE = '\033[00m'
    

def eprint(string, color, bold, linebreak):
    if (bold):
        formatedString = color+sf.BOLD+str(string)
    else:
        formatedString = color+str(string)

    if (linebreak):
        print(formatedString)
    else:
        print(formatedString, end='')

    
    

def printTitleScreen():
    print('\033c', end='')
    eprint(' _____ _____           _____               ', sf.RED, True, True)
    eprint('|  |  |  |  |   ___   |   __|___ _____ ___ ', sf.RED, True, True)
    eprint('|  |  |  |  |  |___|  |  |  | .\'|     | -_|', sf.RED, True, True)
    eprint('|_____|_____|         |_____|__,|_|_|_|___|', sf.RED, True, True)
    print('')
    eprint('         [1] Play Local Game', sf.WHITE, True, True)
    eprint('         [2] Play Online Game', sf.WHITE, True, True)
    print('')
    eprint('         [3] Exit\n', sf.WHITE, True, True)
    eprint('  Type \'q\' at any point to exit the game.', sf.WHITE, True, True)

def printLocalMenu():
    print('\033c', end='')
    eprint(' _____ _____           _____               ', sf.RED, True, True)
    eprint('|  |  |  |  |   ___   |   __|___ _____ ___ ', sf.RED, True, True)
    eprint('|  |  |  |  |  |___|  |  |  | .\'|     | -_|', sf.RED, True, True)
    eprint('|_____|_____|         |_____|__,|_|_|_|___|', sf.RED, True, True)
    print('')
    eprint('         [1] Play VS Human', sf.WHITE, True, True)
    eprint('         [2] Play VS Computer', sf.WHITE, True, True)
    eprint('         [3] Play Tournament', sf.WHITE, True, True)
    print('')
    eprint('         [4] Back', sf.WHITE, True, True)

def printOnlineMenu():
    print('\033c', end='')
    eprint(' _____ _____           _____               ', sf.RED, True, True)
    eprint('|  |  |  |  |   ___   |   __|___ _____ ___ ', sf.RED, True, True)
    eprint('|  |  |  |  |  |___|  |  |  | .\'|     | -_|', sf.RED, True, True)
    eprint('|_____|_____|         |_____|__,|_|_|_|___|', sf.RED, True, True)
    print('')
    eprint('         [1] Play Versus', sf.WHITE, True, True)
    eprint('         [2] Play Tournament', sf.WHITE, True, True)
    print('')
    eprint('         [3] Back', sf.WHITE, True, True)

def printOnlineHostingMenu():
    print('\033c', end='')
    eprint(' _____ _____           _____               ', sf.RED, True, True)
    eprint('|  |  |  |  |   ___   |   __|___ _____ ___ ', sf.RED, True, True)
    eprint('|  |  |  |  |  |___|  |  |  | .\'|     | -_|', sf.RED, True, True)
    eprint('|_____|_____|         |_____|__,|_|_|_|___|', sf.RED, True, True)
    print('')
    eprint('         [1] Host', sf.WHITE, True, True)
    eprint('         [2] Join', sf.WHITE, True, True)
    print('')
    eprint('         [3] Back', sf.WHITE, True, True)
    
def printFancyBoard(board, turn, player, opponent):

    print('\033c', end='')
    
    if (turn == Turn.PLAYER):
        eprint('      ', sf.GREEN, True, False)
        eprint(player, sf.GREEN, True, False)
        eprint('\'s turn.', sf.WHITE, True, True) 
    else:
        eprint('      ', sf.RED, True, False)
        eprint(opponent, sf.RED, True, False)
        eprint('\'s turn.', sf.WHITE, True, True) 
        
    eprint(' _________________________', sf.CYAN, True, True)
    for i in range(4):
        eprint(' |     |     |     |     |', sf.CYAN, True, True)
        
        

        for j in range(4):
            
            if (j == 0):
                letter = ''
                if (i == 0):
                    letter = 'A'
                elif (i == 1):
                    letter = 'B'
                elif (i == 2):
                    letter = 'C'
                else:
                    letter = 'D'
                eprint(letter, sf.WHITE, True, False)
                eprint('| ', sf.CYAN, True, False)
            else:
                print('', end='')

            if (board[i][j] == None):
                print('   ', end='')
            else:
                #eprint(board[i][j], sf.RED, end='')
                board[i][j].printSelf()
                #print(board[i][j])
            if (j == 3):
                eprint(' | ', sf.CYAN, True, True)
            else:
                eprint(' | ', sf.CYAN, True, False)
        if (i == 3):
            eprint(' |_____|_____|_____|_____|', sf.CYAN, True, True)
            eprint('    1     2     3     4 \n', sf.WHITE, True, True)
        else:
            eprint(' |_____|_____|_____|_____|', sf.CYAN, True, True)

def printWhatToDo():
    eprint(' What would you like to do?', sf.WHITE, True, True)
    eprint('     [1] Make a move', sf.WHITE, True, True)
    eprint('     [2] Send message', sf.WHITE, True, True)
    eprint('     [3] Quit', sf.WHITE, True, True)

def printPieces(pieces):
    eprint('  Current pool of pieces: ', sf.WHITE, True, True)

    for x in range(8):
        print(' ', end='')
        if (len(pieces[x]) > 0):
            pieces[x][0].printSelf()
        else:
            print('   ', end='')
    print('')
    eprint('  1   2   3   4   5   6   7   8 ', sf.WHITE, True, True)
    print('')
    for x in range(8, 16):
        print(' ', end='')
        if (len(pieces[x]) > 0):
            pieces[x][0].printSelf()
        else:
            print('   ', end='')

    print('')
    eprint('  9  10  11  12  13  14  15  16 ', sf.WHITE, True, True)
    print('')

def printPieceToPlace(piece, turn):
    eprint('You were handed the piece ', sf.WHITE, True, False)
    piece.printSelf()
    eprint('\nWhere do you want to place it?\n', sf.WHITE, True, False)

def printPieceToGive(pieces):
    eprint('Select a piece to give to the opponent:\n', sf.WHITE, True, True)


def printDifficultySettings():
    print('\033c', end='')
    eprint(' _____ _____           _____               ', sf.RED, True, True)
    eprint('|  |  |  |  |   ___   |   __|___ _____ ___ ', sf.RED, True, True)
    eprint('|  |  |  |  |  |___|  |  |  | .\'|     | -_|', sf.RED, True, True)
    eprint('|_____|_____|         |_____|__,|_|_|_|___|', sf.RED, True, True)
    print('')
    eprint('         Select difficulty:\n', sf.WHITE, True, True)
    eprint('            [1] Easy', sf.WHITE, True, True)
    eprint('            [2] Medium', sf.WHITE, True, True)
    eprint('            [3] Hard', sf.WHITE, True, True)
    print('')
    eprint('            [4] Back', sf.WHITE, True, True)


# Tournament stuff

def printHowManyPlayers():
    print('\033c', end='')
    eprint(' _____ _____           _____               ', sf.RED, True, True)
    eprint('|  |  |  |  |   ___   |   __|___ _____ ___ ', sf.RED, True, True)
    eprint('|  |  |  |  |  |___|  |  |  | .\'|     | -_|', sf.RED, True, True)
    eprint('|_____|_____|         |_____|__,|_|_|_|___|', sf.RED, True, True)
    print('')
    eprint('      How many players? (3-8 players)\n', sf.WHITE, True, True)

def printHowManyAI():
    print('\033c', end='')
    eprint(' _____ _____           _____               ', sf.RED, True, True)
    eprint('|  |  |  |  |   ___   |   __|___ _____ ___ ', sf.RED, True, True)
    eprint('|  |  |  |  |  |___|  |  |  | .\'|     | -_|', sf.RED, True, True)
    eprint('|_____|_____|         |_____|__,|_|_|_|___|', sf.RED, True, True)
    print('')    
    eprint('        How many AI units? (0-3 AI)\n', sf.WHITE, True, True)
