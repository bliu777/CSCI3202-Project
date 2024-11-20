import copy as cp
from mancala import Mancala

def minimax(game, depth):
    if game.current_player == 1:
        best_util = float("-inf")
        best_move = 0
        for i in range(1, game.pits_per_player + 1):
            if game.valid_move(i) == 0:
                curr_util = maxi(game, i, depth - 1)
                if curr_util > best_util:
                    best_util = curr_util
                    best_move = i
    elif game.current_player == 2:
        best_util = float("inf")
        best_move = 0
        for i in range(1, game.pits_per_player + 1):
            if game.valid_move(i) == 0:
                curr_util = mini(game, i, depth - 1)
                if curr_util < best_util:
                    best_util = curr_util
                    best_move = i
    return best_move

def maxi(game, pit, depth):
    gameCopy = cp.deepcopy(game)
    gameCopy.play(pit, True)

    if depth <= 0 or gameCopy.winning_eval() == True:
        return utility_eval(gameCopy)
    
    best_util = float("-inf")
    best_move = 0
    for i in range(1, game.pits_per_player + 1):
        if gameCopy.valid_move(i) == 0:
            curr_util = mini(gameCopy, i, depth - 1)
            if curr_util > best_util:
                best_util = curr_util
                best_move = i
    return best_util

def mini(game, pit, depth):
    gameCopy = cp.deepcopy(game)
    gameCopy.play(pit, True)

    if depth <= 0 or gameCopy.winning_eval() == True:
        return utility_eval(gameCopy)
    
    best_util = float("inf")
    best_move = 0
    for i in range(1, game.pits_per_player + 1):
        if gameCopy.valid_move(i) == 0:
            curr_util = maxi(gameCopy, i, depth - 1)
            if curr_util < best_util:
                best_util = curr_util
                best_move = i
    return best_util

def utility_eval(game):
    utility = game.board[game.p1_mancala_index] - game.board[game.p2_mancala_index]
    if not utility and utility != 0:
        print(utility)
        game.display_board()
    return utility
