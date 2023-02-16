import random
from utility import validate_option, print_options

class Player:
    # Initialize the player. Ask for name and token they want to choose.
    def __init__(self, game):
        self.game = game
        self.name = self.choose_name()        
        self.token = self.choose_token()
        self.is_playing = False

    
    # Player chooses name
    def choose_name(self):
        name = input('Choose a name for your player: ').strip()
        print(f'Your player name is "{name}"')
        return name

    # Player chooses token
    def choose_token(self):
        # Print the available tokens
        print('These are the available tokens:')
        labeled_available_tokens = print_options(self.game.available_tokens)
        # Validate the choice
        token_checked = validate_option(
            labeled_available_tokens,
            'Choose one token. Type the corresponding letter to make your choice: ',
            f"Please choose one of the available tokens: {', '.join(labeled_available_tokens)}"
        )
        # Store the valid chosen token value in a variable
        token = labeled_available_tokens[token_checked]
        print(f"Your token is \"{token}\".")
        return token

    # simulate the player rolling the die
    def roll_die(self, squares, categories):
        print('Rolling the die...')
        # picks a random square from the board
        square = random.choice(list(squares.keys()))
        print(f'Square {square}.')
        return square
    

        
