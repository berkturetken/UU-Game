import prints
import game
import main

'''

User input

'''


def askToPlayAgain():
    choice = input('       Play again? [yes/no]\n')
    if (choice == 'yes'):
        game.main()
    else:
        quit()

def askWhereToPlace(board):    
    choice = requestCoordinates(board)
    return choice

def askForPiece(pieces):
    choice = requestPiece(pieces)
    return choice

def requestPiece(pieces):
    acceptableInput = ['1', '2', '3', '4', '5', '6', '7', '8',
                       '9', '10', '11', '12', '13', '14', '15', '16']
    choice = input('Which piece?\n')


    while (True):
        if (choice == 'quit'):
            quit()
        if (choice in acceptableInput):
            if (len(pieces[int(choice) - 1]) == 0):
                prints.eprint('There are no morex pieces of that type!', prints.sf.WHITE, True, True)
                choice = input('Please pick a different piece: \n')
            else:
                break
        else:
            choice = input('Please enter a number between 1 and 16: \n')
        
    return pieces[int(choice) - 1].pop()

def makeInt(letter):
    if (letter == 'a' or letter == 'A'):
        return 0
    if (letter == 'b' or letter == 'B'):
        return 1
    if (letter == 'c' or letter == 'C'):
        return 2
    if (letter == 'd' or letter == 'D'):
        return 3

    return 0
    
def requestCoordinates(board):
    acceptableInput = ['a1', 'a2', 'a3', 'a4', 'A1', 'A2', 'A3', 'A4',
                       '1a', '2a', '3a', '4a', '1A', '2A', '3A', '4A',
                       'b1', 'b2', 'b3', 'b4', 'B1', 'B2', 'B3', 'B4',
                       '1b', '2b', '3b', '4b', '1B', '2B', '3B', '4B',
                       'c1', 'c2', 'c3', 'c4', 'C1', 'C2', 'C3', 'C4',
                       '1c', '2c', '3c', '4c', '1C', '2C', '3C', '4C',
                       'd1', 'd2', 'd3', 'd4', 'D1', 'D2', 'D3', 'D4'
                       '1d', '2d', '3d', '4d', '1D', '2D', '3D', '4D',
                       'q']

    numbers = ['1', '2', '3', '4']
    
    choice = input('Choose a location on the grid (example: 1A or a1):\n')
    while (True):
        if choice in acceptableInput:
            if (choice == 'q'):
                quit()
            else:
                first = choice[0]
                second = choice[1]

                if (first in numbers):
                    x = int(first)
                else:
                    x = int(second)

                if (isinstance(second, str)):
                    y = makeInt(second)
                else:
                    y = makeInt(first)

                if (board[y][x - 1] is not None):
                    print("That cell is occupied! Please pick another one.")
                    (x, y) = requestCoordinates(board)
                    return (int(x), int(y))
                else:
                    return (int(x) - 1, int(y))
        else:
            choice = input('Please enter a valid location (example: 1A or a1):\n')
                       

def menuInput():

    choice = input('')
    acceptableInput = ['1', '2', '3', 'q']

    while (True):
        if choice in acceptableInput:
            if (choice == 'q'):
                quit()
            if (int(choice) == 3):
                quit()
            elif (int(choice) == 2):
                #game.playOnlineVersus(True)
                prints.printOnlineMenu()
                onlineMenuInput()
            elif (int(choice) == 1):
                print('\033c', end='')
                prints.printLocalMenu()
                localMenuInput()
        else:
            choice = input('Please enter a number between 1-3\n')
    return

def localMenuInput():
    choice = input('')
    acceptableInput = ['1', '2', '3', '4', 'q']

    while (True):
        if choice in acceptableInput:
            if (choice == 'q'):
                quit()
            if (int(choice) == 4):
                game.main()
            elif (int(choice) == 2):
                print('\033c', end='')
                prints.printDifficultySettings()
                difficultySettings('Player', 'UU-BOT')
            elif (int(choice) == 1):
                player1, player2 = namePlayers()
                game.playVersusHuman(player1, player2)
            elif (int(choice) == 3):
                #play tournament
                #game.playLocalTournament()
                prints.printHowManyPlayers()
                humans = tournamentHowManyPlayers()
                playerList, humanDict = tournamentNamePlayers(humans)
                prints.printHowManyAI()
                ais = tournamentHowManyAI()
                playerList, humanDict = tournamentAddAI(playerList, humanDict, ais)
                game.playLocalTournament(playerList, humanDict)
                game.main()
        else:
            choice = input('Please enter a number between 1-4\n')
        
        
    return
    
def difficultySettings(player1, player2):
    choice = input('')
    acceptableInput = ['1', '2', '3', '4', 'q']
    while (True):
        if choice in acceptableInput:
            if (choice == 'q'):
                quit()
            if (int(choice) == 1):
                difficulty = game.Difficulty.EASY
                break
            elif (int(choice) == 2):
                difficulty = game.Difficulty.MEDIUM
                break
            elif (int(choice) == 3):
                difficulty = game.Difficulty.HARD
                break
            else:
                print('\033c', end='')
                prints.printLocalMenu()
                localMenuInput()
        else:
            choice = input('Please enter a number between 1-4\n')
    game.playVersusAI(difficulty, player1, player2)
        
def onlineMenuInput():
    choice = input('')
    acceptableInput = ['1', '2', '3']

    while (True):
        if choice == 'q':
            quit()
        if choice in acceptableInput:
            if (int(choice) == 3):
                game.main()
            elif (int(choice) == 2):
                print('\033c', end='')
                main.online_tour_play()

            elif (int(choice) == 1):
                print('\033c', end='')
                prints.printOnlineHostingMenu()
                onlineMenuHostOrClientInput()
        else:
            choice = input('Please enter a number between 1-3\n')
        return

def onlineMenuHostOrClientInput():
    choice = input('')
    acceptableInput = ['1', '2', '3']

    while (True):
        if (choice == 'q'):
            quit()
        if choice in acceptableInput:
            if (int(choice) == 3):
                prints.printOnlineMenu()
                onlineMenuInput()
            elif (int(choice) == 2):
                #game.playOnlineVersus(True)
                game.playOnlineVersus(False, "Player 2", "Player 1")
            elif (int(choice) == 1):
                print('\033c', end='')
                game.playOnlineVersus(True, "Player 1", "Player 2")
        else:
            choice = input('Please enter a number between 1-3\n')
        return

def namePlayers():
    player1 = input('Enter the name of player 1: ')
    player2 = input('Enter the name of player 2: ')
    return player1, player2

#Tournament stuff
def tournamentHowManyPlayers():
    choice = input('')
    acceptableInput = ['3', '4', '5', '6', '7', '8']

    while (True):
        if choice == 'q':
            quit()
        if choice in acceptableInput:
            return int(choice)
        else:
            choice = input('Please enter a number between 3-8\n')
        return

def tournamentNamePlayers(amount):
    playerList = []
    humanDict = {}  # Booleans. Key = player. True = Human, False = NPC
    for i in range(amount):
        name = input('Enter the name of player #' + str(i + 1) + ": ")
        playerList.append(name)
        humanDict[name] = True
    return playerList, humanDict
        

def tournamentHowManyAI():
    choice = input('')
    acceptableInput = ['0', '1', '2', '3']

    while (True):
        if choice in acceptableInput:
            return int(choice)
        else:
            choice = input('Please enter a number between 0-3\n')
        return

def tournamentAddAI(playerList, humanDict, amount):
    if (amount == 0):
        return playerList, humanDict
    namePool = ['AM', 'R2D2', 'UU-BOT']

    for i in range(amount):
        name = namePool.pop()
        playerList.append(name)
        humanDict[name] = False

    return playerList, humanDict
