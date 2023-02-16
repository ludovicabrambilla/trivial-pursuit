import random
from string import ascii_lowercase
from board import categories, squares
from questions import questions


class Player:
    # Class var to keep track of the available tokens to be chosen
    available_tokens = ['pink', 'yellow', 'orange', 'blue', 'brown', 'green']

    # Class var to keep track of the tokens already taken by other players
    taken_tokens = {}

    # Function to check if the input provided from the user is valid
    # Takes the input prompt and value, the list where you want to check if the value exists, the error message to display if the input is not valid
    def validate_input(self, validation_list, user_input, error_message):
        while True:
            label = input(user_input).strip().lower()
            if label in validation_list:
                return label
            print(error_message)
    
    # Function to print available options in format "a) option"
    def print_options(self, options_list):
        labeled_options = dict(zip(ascii_lowercase, options_list))
        for label, option in labeled_options.items():
            print(f" {label}) {option}")
        return labeled_options

    # Player chooses name
    def choose_name(self):
        name = input('Choose a name for your player: ').strip()
        return name

    # Player chooses token
    def choose_token(self):
        # Print the available tokens
        print('These are the available tokens:')
        labeled_available_tokens = self.print_options(Player.available_tokens)
        # Validate the choice
        token_checked = self.validate_input(
            labeled_available_tokens,
            'Choose one token. Type the corresponding letter to make your choice: ',
            f"Please choose one of the available tokens: {', '.join(labeled_available_tokens)}"
        )
        # Store the valid chosen token value in a variable
        token = labeled_available_tokens[token_checked]
        # Remove it from the available tokens
        Player.available_tokens.remove(token)
        # Add it to the taken_tokens
        Player.taken_tokens[self.name] = token
        print(f"Your token is {token}.")
        return Player.taken_tokens[self.name]


    # Initialize the player. Ask for name and token they want to choose.
    def __init__(self):
        self.name = self.choose_name()        
        self.token = self.choose_token()


    # Prompt a question to the player
    def ask_question(self, category):
        # TODO: make num_correct an instance variable
        num_correct = 0 # keeps score
        question = random.choice(list(questions[category]))
        print(f"{question}")

        # get the answer options of the questions picked
        options = questions[category][question]
        # the correct answer is always the first in the options list
        correct_answer = options[0]
        # shuffle the order of the options with a random sample that takes all the available options and print them
        labeled_options = self.print_options(random.sample(options, k=len(options)))

        # ERROR HANDLING: Reprompt the player if he/she gives an answer not in the options given
        answer_checked = self.validate_input(
            labeled_options,
            f"\nChoice? ",
            f"Please answer one of {', '.join(labeled_options)}"
            )
        answer = labeled_options[answer_checked]
        if answer == correct_answer:
            num_correct += 1
            print('⭐ Correct!⭐')
        else:
            print(f"Sorry, incorrect answer. The answer is {correct_answer!r}, not {answer!r}")


    # simulate the player rolling the die
    def roll_die(self):
        print('Rolling the die...')
        # picks a random square from the board
        square = random.choice(list(squares.keys()))
        # check the corresponding category
        category = squares[square]
        print(f'Square {square}, category {squares[square]}')
        # if square is roll again, call the function again
        if category == categories['white']:
            self.roll_die()
        # if die goes on Start, the user must choose a category
        elif category == categories['start']:
            labeled_categories = self.print_options(list(questions))
            # check if the provided category is valid
            category_checked = self.validate_input(
                labeled_categories,
                f"\nChoice? ",
                f"Please choose one of the categories {', '.join(labeled_categories)}"
                )
            # the category is chosen from the user
            category = labeled_categories[category_checked]

        # ask question from a category
        self.ask_question(category)
        
