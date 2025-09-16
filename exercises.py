class Game:
    # Creating an initial state / Creating Game class with initial state
    # Also, defining the Game class with attributes like board, turn, winner & tie status
    # What this does is that it creates a game class with a board/dictionary with keys like a1, current turn X starts, tie status is false and winner is none.
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None
         }
        
    # ADDING play_game method function to print a welcome message as per labs step 2
    # def play_game(self):
    #     print("Welcome to Tic-Tac-Toe!")

    # Lastly, updated the play_game function above to run the full game loop
    # Commenting out the function above and putting it under the check_for_tie for full functionality.
    # I'm pretty sure I need to move it here so that it will work after all the other functions? Correct?
    def play_game(self):
        print("Welcome to Tic-Tac-Toe!") # user story welcoming to game
        while not self.winner and not self.tie:
            self.print_board()
            self.print_message()
            self.get_move()
            self.check_for_winner()
            self.check_for_tie()
            self.switch_turn()
        self.print_board()
        self.print_message()
    
    # Adding print_board method function - for displaying the 3X3 board
    def print_board(self): # user story printing board on console before being prompted for a move
        b = self.board
        print(f"""
            A   B   C
        1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
            ---------
        2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
            ---------
        3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    # Adding print_message to show whose turn it is and if winner or tie
    def print_message(self):
        if self.tie:
            print("Tie game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!") #user story showing whose turn it is

    # Adding get_move function to get and validate player's move and need to make sure lower case
    def get_move(self):
        while True:
            move = input(f"Enter a valid move (example: A1): ").lower() #user story to be prompted to enter a move and provided a valid input
            if move in self.board and self.board[move] is None:
                self.board[move] = self.turn
                break
            print("Invalid move! Try again.")

    # Adding check_for_winner function to check the win conditions
    def check_for_winner(self):
        b = self.board
        if (b['a1'] and b['a1'] == b['b1'] == b['c1']) or \
           (b['a2'] and b['a2'] == b['b2'] == b['c2']) or \
           (b['a3'] and b['a3'] == b['b3'] == b['c3']):
            self.winner = self.turn
        elif (b['a1'] and b['a1'] == b['a2'] == b['a3']) or \
             (b['b1'] and b['b1'] == b['b2'] == b['b3']) or \
             (b['c1'] and b['c1'] == b['c2'] == b['c3']):
            self.winner = self.turn
        elif (b['a1'] and b['a1'] == b['b2'] == b['c3']) or \
             (b['c1'] and b['c1'] == b['b2'] == b['a3']):
            self.winner = self.turn

    # Adding check_for_tie function so that you check to see if players tie
    def check_for_tie(self):
        if not self.winner and all(self.board.values()):
            self.tie = True

    # Adding switch_turn function at the end so I can alternate between players using X and O (so it goes back and forth between player X & O) after each move.
    def switch_turn(self):
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'





# Testing code but need to remove after testing
# To test 1st function above
# game = Game()
# print(game.turn)


# To test 2nd function of play_game
# game = Game()
# game.play_game()


# To test 3rd function above of print_board
# game = Game()
# game.print_board()


# To test 4th function above of print_message
# game = Game()
# game.print_message()


# Testing 5th function of get_move
# game = Game()
# game.get_move()
# game.print_board()


# Testing 6th function of check_for_winner
# game = Game()
# game.board['a1'] = 'X'
# game.board['b1'] = 'X'
# game.board['c1'] = 'X'
# game.check_for_winner()
# game.print_message()

# Testing 7th function of check_for_tie
# game = Game()
# for key in game.board:
#     game.board[key] = 'X'
# game.check_for_tie()
# game.print_message()

#Testing 8th function which is just a reworking of the play_game function
game = Game()
game.play_game()