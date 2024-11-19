from mancala import Mancala
from minimax import minimax
from ab_pruning import alpha_beta

def driver(suppress_output, p1type, p2type, plies):
    '''
        This driver function takes 4 arguments and outputs 1 value.

        Inputs:
            suppress_output: Boolean value. Chooses if there should be console output or not.
                True: There should be no output to console
                False: Console output is wanted
            p1type: Integer from 0-4, inclusive. Dictates the player type of Player 1.
                0: Lets you select the player type of Player 1 from console. Should only be used if suppress_output=False.
                1: Player 1 is a human player
                2: Player 1 is a random player (makes a random legal move each turn)
                3: Player 1 is an AI player using Minimax
                4: Player 1 is an AI player using Alpha-Beta Pruning
            p2type: Integer from 0-4, inclusive. Dictates the player type of Player 2.
                0: Lets you select the player type of Player 2 from console. Should only be used if suppress_output=False.
                1: Player 2 is a human player
                2: Player 2 is a random player (makes a random legal move each turn)
                3: Player 2 is an AI player using Minimax
                4: Player 2 is an AI player using Alpha-Beta Pruning
            plies: Integer >0. Dictates the number of plies the AI game tree searches down. No effect if neither player is an AI.

        Outputs:
            winner: Integer value from 0-2, inclusive. Represents the winning player of the game.
                0: The game was a tie
                1: Player 1 won the game
                2: Player 2 won the game
    '''

    game = Mancala()

    if suppress_output == False:
        if p1type == 0:
            print("What type of player should P1 be? Input a number.")
            print("     1. Human")
            print("     2. Random")
            print("     3. AI (Minimax)")
            print("     4. AI (Alpha-Beta Pruning)")

            validInput = False
            while validInput == False:
                consoleInput = input("==> ")
                if consoleInput == "1":
                    p1type = 1
                    validInput = True
                elif consoleInput == "2":
                    p1type = 2
                    validInput = True
                elif consoleInput == "3":
                    p1type = 3
                    validInput = True
                elif consoleInput == "4":
                    p1type = 4
                    validInput = True
                else:
                    print("Invalid input, try again")
        
        if p2type == 0:
            print("What type of player should P2 be? Input a number.")
            print("     1. Human")
            print("     2. Random")
            print("     3. AI (Minimax)")
            print("     4. AI (Alpha-Beta Pruning)")

            validInput = False
            while validInput == False:
                consoleInput = input("==> ")
                if consoleInput == "1":
                    p2type = 1
                    validInput = True
                elif consoleInput == "2":
                    p2type = 2
                    validInput = True
                elif consoleInput == "3":
                    p2type = 3
                    validInput = True
                elif consoleInput == "4":
                    p2type = 4
                    validInput = True
                else:
                    print("Invalid input, try again")


        print("Starting game...")

    #print("p1 =", p1type)
    #print("p2 =", p2type)

    if suppress_output == False:
        game.display_board()
    while game.winning_eval() == False:
        if game.current_player == 1:
            if p1type == 1 :
                #player turn
                player_turn(game, suppress_output)
            elif p1type == 2:
                #random player turn
                game.random_move_generator(suppress_output)
            elif p1type == 3:
                #minimax player turn
                minimaxMove = minimax(game, 5)
                game.play(minimaxMove, True)
            else:
                #alpha-beta player turn
                ab_move = alpha_beta(game, 5)
                game.play(ab_move, True)
        else:
            if p2type == 1:
                #player turn
                player_turn(game, suppress_output)
            elif p2type == 2:
                #random player turn
                game.random_move_generator(suppress_output)
            elif p2type == 3:
                #minimax player turn
                minimaxMove = minimax(game, 5)
                game.play(minimaxMove, True)
            else:
                #alpha-beta player turn
                ab_move = alpha_beta(game, 5)
                game.play(ab_move, True)
        if suppress_output == False and (p1type != 1 or p2type != 1):
            game.display_board()
    p1_score = game.board[game.p1_mancala_index]
    p2_score = game.board[game.p2_mancala_index]
    if p1_score > p2_score:
        if suppress_output == False and (p1type != 1 or p2type != 1):
            print("Game Over! Player 1 has won with", p1_score-p2_score, "extra stones!")
        winner = 1
    elif p2_score > p1_score:
        if suppress_output == False and (p1type != 1 or p2type != 1):
            print("Game Over! Player 2 has won with", p2_score-p1_score, "extra stones!")
        winner = 2
    else:
        if suppress_output == False and (p1type != 1 or p2type != 1):
            print("Game Over! The game is a draw!")
        winner = 0
    return winner


def player_turn(game, suppress_output):
    print("What move would Player", game.current_player, "like to make?")
    validInput = False
    while validInput == False:
        consoleInput = input("==> ")
        intInput = int(consoleInput)
        if intInput <= game.pits_per_player and intInput > 0:
            game.play(intInput, suppress_output)
            validInput = True
        else:
            print("Invalid input, please select a pit number.")