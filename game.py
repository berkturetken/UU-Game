from enum import Enum
import tournament
import time
import prints
import userInput
import boardLogic
import AI
import peer


class Difficulty(Enum):
    EASY = 0
    MEDIUM = 1
    HARD = 2

class Turn(Enum):
    PLAYER = 0
    OPPONENT = 1

'''

Main loop

'''

def main():

    prints.printTitleScreen()
    userInput.menuInput()
    
    return

def playLocalTournament(playerList, humanDict):
    tour = tournament.Tournament(playerList)
    while (True):
        print(tour.get_scoreboard())
        end = tour.winner_state
        players = tour.opponents
        if end == 1:
            break
        else:
            print('Up next: ' + players[0] + ' VS ' + players[1])
            humans = [humanDict[players[0]], humanDict[players[1]]]
            input('Press ENTER to start playing!')
            while (True):
                if ((not humans[0] and humans[1]) or (humans[0] and not humans[1])):
                    winner = playVersusAINoReplay(Difficulty.HARD, players[0], players[1])                    
                elif (not humans[0] and not humans[1]):
                    winner = playAIvsAI(Difficulty.HARD, players[0], players[1])
                    #this is where we make ai vs ai
                else:
                    winner = playVersusHumanNoReplay(players[0], players[1])

                if winner != "DRAW":
                    break
                else:
                    print("Draw game! Replaying game.")
            tour.next_game(winner)
            print(winner + " has advanced to the next round!")
        #        input('')
    print(winner + " has won the tournament!")
    input('Press ENTER to go back to the menu')

    return True

def playOnlineVersus(host, player1, player2):
    running = True

    connection = peer.Peer(host)

    board = boardLogic.createBoard()
    pieces = boardLogic.createPieces()

    firstTurn = True
    if (host):
        turn = Turn.PLAYER
        connection.accept_client()

        # First turn (just handing a piece)
        prints.printFancyBoard(board, turn, player1, player2)
        prints.printPieces(pieces)
        prints.printPieceToGive(pieces)
        piece = userInput.askForPiece(pieces)
        turn = Turn.OPPONENT
        connection.send([piece, pieces, board])
        firstTurn = False

    else:
        turn = Turn.OPPONENT
        connection.connect_to_server()
        prints.printFancyBoard(board, turn, player1, player2)
        prints.printPieces(pieces)

    while (running):
        if (firstTurn):
            [piece, pieces, board] = connection.receive()
            turn = Turn.PLAYER
            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)
            #Show given piece and place it
            prints.printPieceToPlace(piece, turn)
            coords = userInput.askWhereToPlace(board)
            boardLogic.updateBoard(board, piece, int(coords[0]), int(coords[1]))
            connection.send([piece, pieces, board])
            # Pick a piece for opponent
            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)
            prints.printPieceToGive(pieces)
            piece = userInput.askForPiece(pieces)
            connection.send([piece, pieces, board])
            firstTurn = False
            turn = Turn.OPPONENT
        else:
            turn = Turn.OPPONENT
            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)
            [piece, pieces, board] = connection.receive()
            boardLogic.endGame(board, piece, turn, player1, player2)   

            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)
            [piece, pieces, board] = connection.receive()
            turn = Turn.PLAYER
            # Show given piece, place it
            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)
            prints.printPieceToPlace(piece, turn)
            coords = userInput.askWhereToPlace(board)
            boardLogic.updateBoard(board, piece, int(coords[0]), int(coords[1]))
            connection.send([piece, pieces, board])
            boardLogic.endGame(board, piece, turn, player1, player2)            
        
            # Pick a piece for opponent
            prints.printFancyBoard(board, turn,  player1, player2)
            prints.printPieces(pieces)
            prints.printPieceToGive(pieces)
            piece = userInput.askForPiece(pieces)
            turn = Turn.OPPONENT
            connection.send([piece, pieces, board])


def playOnlineVersusTournament(host, connection, player1, player2):
    running = True

#    connection = peer.Peer(host)

    board = boardLogic.createBoard()
    pieces = boardLogic.createPieces()

    firstTurn = True
    if (host):
        turn = Turn.PLAYER
 #       connection.accept_client()

        # First turn (just handing a piece)
        prints.printFancyBoard(board, turn, player1, player2)
        prints.printPieces(pieces)
        prints.printPieceToGive(pieces)
        piece = userInput.askForPiece(pieces)
        turn = Turn.OPPONENT
        connection.send([piece, pieces, board])
        firstTurn = False

    else:
        turn = Turn.OPPONENT
#        connection.connect_to_server()
        prints.printFancyBoard(board, turn, player1, player2)
        prints.printPieces(pieces)

    while (running):
        if (firstTurn):
            [piece, pieces, board] = connection.receive()
            turn = Turn.PLAYER
            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)
            #Show given piece and place it
            prints.printPieceToPlace(piece, turn)
            coords = userInput.askWhereToPlace(board)
            boardLogic.updateBoard(board, piece, int(coords[0]), int(coords[1]))
            connection.send([piece, pieces, board])
            # Pick a piece for opponent
            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)
            prints.printPieceToGive(pieces)
            piece = userInput.askForPiece(pieces)
            connection.send([piece, pieces, board])
            firstTurn = False
            turn = Turn.OPPONENT
        else:
            turn = Turn.OPPONENT
            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)
            [piece, pieces, board] = connection.receive()
            result = boardLogic.endGameNoReplay(board, piece, turn, player1, player2)
            if (result != 'NONE'):
              #  input('Press enter to advance')
                return result

            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)
            [piece, pieces, board] = connection.receive()
            turn = Turn.PLAYER
            # Show given piece, place it
            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)
            prints.printPieceToPlace(piece, turn)
            coords = userInput.askWhereToPlace(board)
            boardLogic.updateBoard(board, piece, int(coords[0]), int(coords[1]))
            connection.send([piece, pieces, board])
            result = boardLogic.endGameNoReplay(board, piece, turn, player1, player2)
            if (result != 'NONE'):
             #   input('Press enter to advance')
                return result
        
            # Pick a piece for opponent
            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)
            prints.printPieceToGive(pieces)
            piece = userInput.askForPiece(pieces)
            turn = Turn.OPPONENT
            connection.send([piece, pieces, board])

def playOnlineAI(host, connection, player1, player2):
    running = True

#    connection = peer.Peer(host)

    board = boardLogic.createBoard()
    pieces = boardLogic.createPieces()
    difficulty = Difficulty.HARD

    firstTurn = True
    if (host):
        turn = Turn.PLAYER
 #       connection.accept_client()

        # First turn (just handing a piece)
        prints.printFancyBoard(board, turn, player1, player2)
        prints.printPieces(pieces)
        prints.printPieceToGive(pieces)
        piece = AI.pickPiece(board, pieces, difficulty) 
        turn = Turn.OPPONENT
        time.sleep(0.05)
        connection.send([piece, pieces, board])
        firstTurn = False

    else:
        turn = Turn.OPPONENT
#        connection.connect_to_server()
        prints.printFancyBoard(board, turn, player1, player2)
        prints.printPieces(pieces)

    while (running):
        if (firstTurn):
            [piece, pieces, board] = connection.receive()
            turn = Turn.PLAYER
            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)
            #Show given piece and place it
            prints.printPieceToPlace(piece, turn)
            AI.placePiece(board, piece, difficulty) #add difficulty        
#            boardLogic.updateBoard(board, piece, int(coords[0]), int(coords[1]))
            time.sleep(0.05)
            connection.send([piece, pieces, board])
            # Pick a piece for opponent
            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)
            prints.printPieceToGive(pieces)
            piece = AI.pickPiece(board, pieces, difficulty) #add difficulty
            time.sleep(0.05)
            connection.send([piece, pieces, board])
            firstTurn = False
            turn = Turn.OPPONENT
        else:
            turn = Turn.OPPONENT
            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)
            [piece, pieces, board] = connection.receive()
            result = boardLogic.endGameNoReplay(board, piece, turn, player1, player2)
            if (result != 'NONE'):
            #    input('Press enter to advance')
                return result

            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)
            [piece, pieces, board] = connection.receive()
            turn = Turn.PLAYER
            # Show given piece, place it
            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)
            prints.printPieceToPlace(piece, turn)
            AI.placePiece(board, piece, difficulty) #add difficulty
#            boardLogic.updateBoard(board, piece, int(coords[0]), int(coords[1]))
            time.sleep(0.05)
            connection.send([piece, pieces, board])
            result = boardLogic.endGameNoReplay(board, piece, turn, player1, player2)
            if (result != 'NONE'):
           #     input('Press enter to advance')
                return result
        
            # Pick a piece for opponent
            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)
            prints.printPieceToGive(pieces)
            piece = AI.pickPiece(board, pieces, difficulty)
            turn = Turn.OPPONENT
            time.sleep(0.05)
            connection.send([piece, pieces, board])


        
def playVersusAINoReplay(difficulty, player1, player2):
    running = True

    board = boardLogic.createBoard()
    pieces = boardLogic.createPieces()
    
    turn = Turn.PLAYER

    prints.printFancyBoard(board, turn, player1, player2)
    prints.printPieces(pieces)
    
    prints.printPieceToGive(pieces)
    piece = userInput.askForPiece(pieces)
    turn = Turn.OPPONENT

    while (running):
        if (turn == Turn.PLAYER):
            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)
            prints.printPieceToPlace(piece, turn)
            coords = userInput.askWhereToPlace(board)
            boardLogic.updateBoard(board, piece, int(coords[0]), int(coords[1]))
            result = boardLogic.endGameNoReplay(board, piece, turn, player1, player2)
            if (result != 'NONE'):
          #      input('Press enter to advance')
                return result
            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)        
            piece = userInput.askForPiece(pieces)        
            turn = Turn.OPPONENT

        else:
            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)
            time.sleep(0.5)
            result = boardLogic.endGameNoReplay(board, piece, turn, player1, player2)
            if (result != 'NONE'):
         #       input('Press enter to advance')
                return result
            piece = AI.placePiece(board, piece, difficulty) #add difficulty
            result = boardLogic.endGameNoReplay(board, piece, turn, player1, player2)
            if (result != 'NONE'):
        #        input('Press enter to advance')
                return result
            piece = AI.pickPiece(board, pieces, difficulty) #add difficulty
            

            turn = Turn.PLAYER


def playVersusAI(difficulty, player1, player2):
    running = True

    board = boardLogic.createBoard()
    pieces = boardLogic.createPieces()
    
    turn = Turn.PLAYER

    prints.printFancyBoard(board, turn, player1, player2)
    prints.printPieces(pieces)
    
    prints.printPieceToGive(pieces)
    piece = userInput.askForPiece(pieces)
    turn = Turn.OPPONENT

    while (running):
        if (turn == Turn.PLAYER):
            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)
            prints.printPieceToPlace(piece, turn)
            coords = userInput.askWhereToPlace(board)
            boardLogic.updateBoard(board, piece, int(coords[0]), int(coords[1]))
            boardLogic.endGame(board, piece, turn, player1, player2)            
            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)        
            piece = userInput.askForPiece(pieces)        
            turn = Turn.OPPONENT

        else:
            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)
            time.sleep(0.5)
            boardLogic.endGame(board, piece, turn, player1, player2)
            piece = AI.placePiece(board, piece, difficulty) #add difficulty
            boardLogic.endGame(board, piece, turn, player1, player2) 
            piece = AI.pickPiece(board, pieces, difficulty) #add difficulty
            

            turn = Turn.PLAYER


def playVersusHumanNoReplay(player1, player2):
    running = True

    board = boardLogic.createBoard()
    pieces = boardLogic.createPieces()
    
    turn = Turn.PLAYER

    prints.printFancyBoard(board, turn, player1, player2)
    prints.printPieces(pieces)
    
    prints.printPieceToGive(pieces)
    piece = userInput.askForPiece(pieces)
    turn = Turn.OPPONENT

    while (running):
        if (turn == Turn.PLAYER):
            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)
            prints.printPieceToPlace(piece, turn)
            coords = userInput.askWhereToPlace(board)
            boardLogic.updateBoard(board, piece, int(coords[0]), int(coords[1]))
            result = boardLogic.endGameNoReplay(board, piece, turn, player1, player2)
            if (result != 'NONE'):
       #         input('Press enter to advance')
                return result
            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)        
            piece = userInput.askForPiece(pieces)        
            turn = Turn.OPPONENT
        else:
            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)
            prints.printPieceToPlace(piece, turn)
            coords = userInput.askWhereToPlace(board)
            boardLogic.updateBoard(board, piece, int(coords[0]), int(coords[1]))
            result = boardLogic.endGameNoReplay(board, piece, turn, player1, player2)
            if (result != 'NONE'):
      #          input('Press enter to advance')
                return result
            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)        
            piece = userInput.askForPiece(pieces)        
            turn = Turn.PLAYER


def playVersusHuman(player1, player2):
    running = True

    board = boardLogic.createBoard()
    pieces = boardLogic.createPieces()
    
    turn = Turn.PLAYER

    prints.printFancyBoard(board, turn, player1, player2)
    prints.printPieces(pieces)
    
    prints.printPieceToGive(pieces)
    piece = userInput.askForPiece(pieces)
    turn = Turn.OPPONENT

    while (running):
        if (turn == Turn.PLAYER):
            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)
            prints.printPieceToPlace(piece, turn)
            coords = userInput.askWhereToPlace(board)
            boardLogic.updateBoard(board, piece, int(coords[0]), int(coords[1]))
            boardLogic.endGame(board, piece, turn, player1, player2)            
            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)        
            piece = userInput.askForPiece(pieces)        
            turn = Turn.OPPONENT
        else:
            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)
            prints.printPieceToPlace(piece, turn)
            coords = userInput.askWhereToPlace(board)
            boardLogic.updateBoard(board, piece, int(coords[0]), int(coords[1]))
            boardLogic.endGame(board, piece, turn, player1, player2)            
            prints.printFancyBoard(board, turn, player1, player2)
            prints.printPieces(pieces)        
            piece = userInput.askForPiece(pieces)        
            turn = Turn.PLAYER


def playAIvsAI(difficulty, player1, player2):
    running = True

    board = boardLogic.createBoard()
    pieces = boardLogic.createPieces()
    
    turn = Turn.OPPONENT

   # prints.printFancyBoard(board, turn)
   # prints.printPieces(pieces)
    

    piece = AI.pickPiece(board, pieces, difficulty)
    turn = Turn.PLAYER

    while (running):
        if (turn == Turn.PLAYER):
    #        prints.printFancyBoard(board, turn)
     #       prints.printPieces(pieces)

            boardLogic.endGameNoReplay(board, piece, turn, player1, player2)
            piece = AI.placePiece(board, piece, difficulty)
            result = boardLogic.endGameNoReplay(board, piece, turn, player1, player2)
            if (result != 'NONE'):
                #input('Press enter to advance')
                return result
            piece = AI.pickPiece(board, pieces, difficulty)        
            turn = Turn.OPPONENT
        else:
      #      prints.printFancyBoard(board, turn)
       #     prints.printPieces(pieces)

            boardLogic.endGameNoReplay(board, piece, turn, player1, player2)
            piece = AI.placePiece(board, piece, difficulty)
            result = boardLogic.endGameNoReplay(board, piece, turn, player1, player2)
            if (result != 'NONE'):
                #input('Press enter to advance')
                return result
            piece = AI.pickPiece(board, pieces, difficulty)            
            turn = Turn.PLAYER

            
'''

Run main

'''

if __name__ == "__main__":
    main()
