import random
#random.seed(109)

class Mancala:
    def __init__(self, pits_per_player = 6, stones_per_pit = 4):
        """
        The constructor for the Mancala class defines several instance variables:

        pits_per_player: This variable stores the number of pits each player has.
        stones_per_pit: It represents the number of stones each pit contains at the start of any game.
        board: This data structure is responsible for managing the Mancala board.
        current_player: This variable takes the value 1 or 2, as it's a two-player game, indicating which player's turn it is.
        moves: This is a list used to store the moves made by each player. It's structured in the format (current_player, chosen_pit).
        p1_pits_index: A list containing two elements representing the start and end indices of player 1's pits in the board data structure.
        p2_pits_index: Similar to p1_pits_index, it contains the start and end indices for player 2's pits on the board.
        p1_mancala_index and p2_mancala_index: These variables hold the indices of the Mancala pits on the board for players 1 and 2, respectively.
        """
        self.pits_per_player = pits_per_player
        self.board = [stones_per_pit] * ((pits_per_player+1) * 2)  # Initialize each pit with stones_per_pit number of stones 
        self.players = 2
        self.current_player = 1
        self.moves = []
        self.p1_pits_index = [0, self.pits_per_player-1]
        self.p1_mancala_index = self.pits_per_player
        self.p2_pits_index = [self.pits_per_player+1, len(self.board)-1-1]
        self.p2_mancala_index = len(self.board)-1
        
        # Zeroing the Mancala for both players
        self.board[self.p1_mancala_index] = 0
        self.board[self.p2_mancala_index] = 0

    def display_board(self):
        """
        Displays the board in a user-friendly format
        """
        player_1_pits = self.board[self.p1_pits_index[0]: self.p1_pits_index[1]+1]
        player_1_mancala = self.board[self.p1_mancala_index]
        player_2_pits = self.board[self.p2_pits_index[0]: self.p2_pits_index[1]+1]
        player_2_mancala = self.board[self.p2_mancala_index]

        print('P1               P2')
        print('     ____{}____     '.format(player_2_mancala))
        for i in range(self.pits_per_player):
            if i == self.pits_per_player - 1:
                print('{} -> |_{}_|_{}_| <- {}'.format(i+1, player_1_pits[i], 
                        player_2_pits[-(i+1)], self.pits_per_player - i))
            else:    
                print('{} -> | {} | {} | <- {}'.format(i+1, player_1_pits[i], 
                        player_2_pits[-(i+1)], self.pits_per_player - i))
            
        print('         {}         '.format(player_1_mancala))
        turn = 'P1' if self.current_player == 1 else 'P2'
        print('Turn: ' + turn)
        
    def valid_move(self, pit):
        """
        Function to check if the pit chosen by the current_player is a valid move.
        """

        #check if pit number is valid
        if pit < 1 or pit > self.pits_per_player:
            return 2 #invalid move (invalid pit number)

        #calculate offset for player 2
        if self.current_player == 1:
            pit_index_offset = 0
        else:
            pit_index_offset = self.p1_mancala_index + 1

        #check if pit is empty
        if self.board[pit + pit_index_offset - 1] == 0:
            return 1 #invalid move (empty pit)
        return 0 #valid move
        
    def random_move_generator(self, suppress_output):
        """
        Function to generate random valid moves with non-empty pits for the random player
        """
        #create list of non-empty pits (legal moves)
        legal_moves = []
        for i in range(self.pits_per_player):
            if self.valid_move(i + 1) == 0:
                legal_moves.append(i + 1)
        #print(legal_moves)
        #Generate random a random move from the list of legal moves   
        selected_pit = random.choice(legal_moves)
        self.play(selected_pit, suppress_output)
        
        return self.board
        

    def play(self, pit, suppress_output):
        """
        This function simulates a single move made by a specific player using their selected pit. It primarily performs three tasks:
        1. It checks if the chosen pit is a valid move for the current player. If not, it prints "INVALID MOVE" and takes no action.
        2. It verifies if the game board has already reached a winning state. If so, it prints "GAME OVER" and takes no further action.
        3. After passing the above two checks, it proceeds to distribute the stones according to the specified Mancala rules.

        Finally, the function then switches the current player, allowing the other player to take their turn.
        """
        #Check if one player has won (the game is over)
        if self.winning_eval() == True:
            if suppress_output == False:
                print("GAME OVER")
            return self.board
        #calculate offset for player 2
        if self.current_player == 1:
            pit_index_offset = 0
        else:
            pit_index_offset = self.p1_mancala_index + 1
        #Check if the given move is valid
        if self.valid_move(pit) != 0:
            print("INVALID MOVE", self.valid_move(pit), pit)
            return self.board
        #Output
        if suppress_output == False:
            print("Player", self.current_player, "chose pit:", pit)
        #Take game actions
        current_pit_index = pit + pit_index_offset - 1
        remaining_stones = self.board[current_pit_index]
        self.board[current_pit_index] = 0
        while remaining_stones > 0:
            if current_pit_index < len(self.board)-1:
                current_pit_index += 1
            else:
                current_pit_index = 0
            self.board[current_pit_index] += 1
            remaining_stones -= 1
        
        #steal stones
        if current_pit_index >= 0 + pit_index_offset and current_pit_index < self.pits_per_player + pit_index_offset and self.board[current_pit_index] == 1:
            if self.current_player == 1:
                opposing_pit = self.p2_pits_index[0] + (6 - current_pit_index)
            else:
                opposing_pit = self.p1_pits_index[0] + (6 - current_pit_index)
            self.board[self.pits_per_player + pit_index_offset] += self.board[opposing_pit] + 1
            self.board[opposing_pit] = 0
            self.board[current_pit_index] = 0
            
        #Record the move made
        self.moves.append((self.current_player, pit))
        #Switch players
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1
            
        return self.board
    
    def winning_eval(self):
        """
        Function to verify if the game board has reached the winning state.
        Hint: If either of the players' pits are all empty, then it is considered a winning state.
        """
        p1_over = True
        p2_over = True
        for i in range(self.pits_per_player):
            if self.board[i] > 0:
                #print(i, self.board[i])
                p1_over = False
            if self.board[i + self.p1_mancala_index + 1] > 0:
                #print(i + self.p1_mancala_index + 1, self.board[i + self.p1_mancala_index + 1])
                p2_over = False
        if p1_over == True or p2_over == True:
            return True
        return False