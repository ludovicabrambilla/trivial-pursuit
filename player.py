import random
from utility import validate_option, print_options
from board import Board

class Player:
    # Initialize the player. Ask for name and token they want to choose.
    def __init__(self, game):
        self.game = game
        self.name = self.choose_name()        
        self.token = self.choose_token()
        self.is_playing = False
        self.square = Board.start
        self.score = {color:0 for color in Board.colors}

    # Player chooses name
    def choose_name(self):
        name = input('\nCHOOSE A NAME FOR YOUR PLAYER: ').strip()
        print(f'Your player name is "{name}"')
        return name

    # Player chooses token
    def choose_token(self):
        # Print the available tokens
        print('\nThese are the available tokens:')
        labeled_available_tokens = print_options(self.game.available_tokens)
        # Validate the choice
        token_checked = validate_option(
            labeled_available_tokens,
            '\nCHOOSE A TOKEN. Type the corresponding letter to make your choice: ',
            f"\nPlease choose one of the available tokens: {', '.join(labeled_available_tokens)}"
        )
        # Store the valid chosen token value in a variable
        token = labeled_available_tokens[token_checked]
        print(f"Your token is \"{token}\".")
        return token
    

    # Check if player is on start
    def is_on_start(self):
        return (self.square == Board.start)
    
    # Check if player is on special square
    def is_on_special(self):
        return (self.square in Board.special_squares)

    # simulate the player rolling the die
    def roll_die(self, squares):
        print('\n\nRolling the die...')
        # picks a random square from the board
        square = random.choice(list(squares.keys()))
        self.square = square
        print(f'Square {square}.')
        return square

    # add a point to the score
    def add_point(self, color):
        if self.score[color] < 1:
            self.score[color] += 1
    
    # Check if player can win (== all scores are 1)
    def can_win(self):
        return all(score == 1 for score in self.score.values()) and self.is_on_start() == True