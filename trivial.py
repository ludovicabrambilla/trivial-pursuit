import random
from utility import validate_option, print_options

class Player:
    # Initialize the player. Ask for name and token they want to choose.
    def __init__(self, game):
        self.game = game
        self.name = self.choose_name()        
        self.token = self.choose_token()

    
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

    # # simulate the player rolling the die
    # def roll_die(self):
    #     print('Rolling the die...')
    #     # picks a random square from the board
    #     square = random.choice(list(squares.keys()))
    #     # check the corresponding category
    #     category = squares[square]
    #     print(f'Square {square}, category {squares[square]}')
    #     # if square is roll again, call the function again
    #     if category == categories['white']:
    #         self.roll_die()
    #     # if die goes on Start, the user must choose a category
    #     elif category == categories['start']:
    #         labeled_categories = self.print_options(list(questions))
    #         # check if the provided category is valid
    #         category_checked = self.validate_input(
    #             labeled_categories,
    #             f"\nChoice? ",
    #             f"Please choose one of the categories {', '.join(labeled_categories)}"
    #             )
    #         # the category is chosen from the user
    #         category = labeled_categories[category_checked]

    #     # ask question from a category
    #     self.ask_question(category)
        
