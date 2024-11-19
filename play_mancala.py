from driver import driver
import time

def mancala_sim():
    suppress_output = True
    plies = 5
    numGames = 100
    p1type = 2
    p2type = 4

    if p1type == 1:
        p1typestring = "Human"
    elif p1type == 2:
        p1typestring = "Random"
    elif p1type == 3:
        p1typestring = "Minimax"
    elif p1type == 4:
        p1typestring = "Alpha-Beta"

    if p2type == 1:
        p2typestring = "Human"
    elif p2type == 2:
        p2typestring = "Random"
    elif p2type == 3:
        p2typestring = "Minimax"
    elif p2type == 4:
        p2typestring = "Alpha-Beta"

    print("Now playing", numGames, "games of", p1typestring, "vs", p2typestring)

    totalTime = 0.

    moveSum = 0.

    p1wins = 0.
    p2wins = 0.
    for i in range(numGames):
        startTime = time.time()
        (gameResult, gameMoves) = driver(suppress_output,p1type,p2type,plies)
        endTime = time.time()
        if gameResult == 1:
            p1wins += 1.
        elif gameResult == 2:
            p2wins += 1.
        moveSum += gameMoves
        totalTime += (endTime - startTime)
        #print(endTime - startTime)
    
    print("Player 1 wins", p1wins, "games, Player 2 wins", p2wins, "games")

    p1WinPercent = (p1wins / numGames) * 100
    p2WinPercent = (p2wins / numGames) * 100
    print("Player 1 win percentage:", p1WinPercent, "%")
    print("Player 2 win percentage:", p2WinPercent, "%")

    avgMoves = moveSum / numGames
    print("Average game length:", avgMoves, "total moves")

    avgTime = totalTime / numGames
    print("Average game time:", avgTime, "seconds")

mancala_sim()