from driver import driver

def mancala_sim():
    suppress_output = True
    plies = 5
    numGames = 100
    p1type = 2
    p2type = 4

    p1wins = 0.
    p2wins = 0.
    for i in range(numGames):
        gameResult = driver(suppress_output,p1type,p2type,plies)
        if gameResult == 1:
            p1wins += 1.
        elif gameResult == 2:
            p2wins += 1.
    
    print(p1wins, p2wins)

    p1WinPercent = (p1wins / numGames) * 100
    p2WinPercent = (p2wins / numGames) * 100
    print("Player 1 win percentage:", p1WinPercent, "%")
    print("Player 2 win percentage:", p2WinPercent, "%")

mancala_sim()