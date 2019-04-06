

'''

User input

'''


def askToPlayAgain():
    choice = input('Play again?\n')
    if (choice == 'yes'):
        playVersusAI()
    else:
        quit()

def askWhereToPlace():
    choice = requestCoordinates()
    return choice

def askForPiece(pieces):
    choice = requestPiece(pieces)
    return choice

def askWhatToDo(board, pieces):
    choice = input('')

    if (int(choice) == 1):
        choice = askForMove(pieces)
        updateBoard(board, pieces[int(choice[0]) - 1].pop(), int(choice[1][0]), int(choice[1][1])) 
        return

    if (int(choice) == 2):
        #sendMessage():
        return

    if (int(choice) == 3):
        quit()


        
    return

def askForMove(pieces):
    piece = requestPiece(pieces)
    coords = requestCoordinates()
    return (piece, coords)
    

def requestPiece(pieces):
    if (len(pieces[0]) > 0 or len(pieces[1]) > 0):
        choice = input('Which piece?\n')
        # TODO: add more safeguards for input
        while (len(pieces[int(choice) - 1]) == 0):
            cprint('There are no morex pieces of that type!', 'white', attrs=['bold'])
            choice = input('Please pick a different piece: \n')
        return pieces[int(choice) - 1].pop()
    return None


def requestCoordinates():
    badX = True
    badY = True
    
    while(badX):
        x = input("X: ")
        if (int(x) > 0 and int(x) <= 4):
            badX = False
            
    while (badY):
        y = input("Y: ")
        if (int(y) > 0 and int(y) <= 4):
            badY = False
        
    return (int(x) - 1, int(y) - 1)

def menuInput():
    cprint('      What would you like to do?', 'white', attrs=['bold'])
    choice = input('')
    
    if (int(choice) == 3):
        quit()
    elif (int(choice) == 2):
        cprint('\033c', end='')
        playVersusAI()
    else:
        cprint('\033c', end='')
        playVersusHuman()
        return
