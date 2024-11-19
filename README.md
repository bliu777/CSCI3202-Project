# CSCI3202-Project
Class project for CSCI 3202 Intro to AI. The goal is to create a functional AI for playing games of Mancala.

To play, run the play_mancala.py file in the terminal.

play_mancala.py has 5 variables that can be changed:
    suppress_output: Boolean, dictates if you want console output for the individual moves of the game. Make sure this is False if one of the players is a human.
    plies: Integer, dictates the depth in the game tree that the two AI player options search. No effect if neither player is an AI.
    numGames: Integer, the number of games that you want to simulate. Recommended to be 1 if one of the players is a human.
    p1type, p2type: Integer from 0-4, inclusive. Dictates the type of player for Player 1 and Player 2, respectively. The options are as below:
        0: Variable. For each individual game, you will be prompted for input from the console to decide the type of the player.
        1: Human. This player will make moves by taking input from the console.
        2: Random. For each move, this player will make a random legal move.
        3: Minimax. This AI player uses the Minimax optimization algorithm to select each move, with the utility function (stones in P1 mancala) - (stones in p2 mancala), to a depth dixtated by the plies variable.
        4: Alpha-Beta. This AI player uses the minimax algorithm similarly to 3, but uses Alpha-Beta Pruning to prune branches from the game tree. 