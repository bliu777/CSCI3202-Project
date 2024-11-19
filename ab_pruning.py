import copy as cp
from mancala import Mancala

def alpha_beta(game, depth):
    alpha = float("-inf")
    beta = float("inf")
    if game.current_player == 1:
        best_util = float("-inf")
        best_move = 0
        for i in range(1, game.pits_per_player + 1):
            if game.valid_move(i) == 0:
                curr_util = ab_maxi(game, i, depth - 1, alpha, beta)
                if curr_util > best_util:
                    best_util = curr_util
                    best_move = i
    elif game.current_player == 2:
        best_util = float("inf")
        best_move = 0
        for i in range(1, game.pits_per_player + 1):
            if game.valid_move(i) == 0:
                curr_util = ab_mini(game, i, depth - 1, alpha, beta)
                if curr_util < best_util:
                    best_util = curr_util
                    best_move = i
    return best_move

def ab_maxi(game, pit, depth, alpha, beta):
    gameCopy = cp.deepcopy(game)
    gameCopy.play(pit, True)
    if depth > 0:
        best_util = float("-inf")
        best_move = 0
        for i in range(1, game.pits_per_player + 1):
            if gameCopy.valid_move(i) == 0:
                curr_util = ab_mini(gameCopy, i, depth - 1, alpha, beta)
                if curr_util > best_util:
                    best_util = curr_util
                    best_move = i
            if best_util >= beta:
                return best_util
            alpha = max(best_util,alpha)
        return best_util
    else:
        return utility_eval(game)

def ab_mini(game, pit, depth, alpha, beta):
    gameCopy = cp.deepcopy(game)
    gameCopy.play(pit, True)
    if depth > 0:
        best_util = float("inf")
        best_move = 0
        for i in range(1, game.pits_per_player + 1):
            if gameCopy.valid_move(i) == 0:
                curr_util = ab_maxi(gameCopy, i, depth - 1, alpha, beta)
                if curr_util < best_util:
                    best_util = curr_util
                    best_move = i
            if best_util <= alpha:
                return best_util
            beta = min(best_util,beta)
        return best_util
    else:
        return utility_eval(game)

def utility_eval(game):
    utility = game.board[game.p1_mancala_index] - game.board[game.p2_mancala_index]
    if not utility and utility != 0:
        print(utility)
        game.display_board()
    return utility
