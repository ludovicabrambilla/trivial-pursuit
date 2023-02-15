import random
from string import ascii_lowercase
from board import categories, board
from questions import questions


class Player:
    # Class var to keep track of the available tokens to be chosen
    available_tokens = ['pink', 'yellow', 'orange', 'blue', 'brown', 'green']

    # Class var to keep track of the tokens already taken by other players
    taken_tokens = {}

    # Function to check if the input provided from the user is valid
    # Takes the input prompt and value, the list where you want to check if the value exists, the error message to display if the input is not valid
    def validate_input(self, user_input, validation_list, error_message):
        while True:
            label = input(user_input).strip().lower()
            if label in validation_list:
                return label
            print(error_message)

    

    # Initialize the player. Ask for name and token they want to choose.
    def __init__(self):
        # USER CHOOSES A NAME FOR THE GAME
        name = input('Choose a name for your player: ').strip()
        self.name = name

        # USER CHOOSES A TOKEN
        # Print the available tokens
        print('These are the available tokens:')
        labeled_available_tokens = dict(zip(ascii_lowercase, Player.available_tokens))
        for label, token in labeled_available_tokens.items():
            print(f'{label}) {token}')
        # Check if the input is valid
        token_label_prompt = 'Choose one token. Type the corresponding letter to make your choice: '
        token_error_message = f"Please choose one of the available tokens: {', '.join(labeled_available_tokens)}"
        token_checked = self.validate_input(token_label_prompt, labeled_available_tokens, token_error_message)

        # Store the valid chosen token value in a variable
        token = labeled_available_tokens[token_checked]
        # Remove it from the available tokens
        Player.available_tokens.remove(token)
        # Add it to the taken_tokens
        Player.taken_tokens[self.name] = token
        print(f"Your token is {token}.")
        # TODO: debug functions
        print(Player.available_tokens)
        print(Player.taken_tokens)
        
        # Store the token as an instance variable
        self.token = Player.taken_tokens[self.name]


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
        # shuffle the order of the options with a random sample that takes all the available options
        # present the options as "a) option"
        labeled_options = dict(zip(ascii_lowercase, random.sample(options, k=len(options))))
        for label, option in labeled_options.items():
            print(f" {label}) {option}")

        # ERROR HANDLING: Reprompt the player if he/she gives an answer not in the options given
        answer_label_prompt = f"\nChoice? "
        answer_error_message = f"Please answer one of {', '.join(labeled_options)}"
        answer_checked = self.validate_input(answer_label_prompt, labeled_options, answer_error_message)
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
        square = random.choice(list(board.keys()))
        # check the corresponding category
        category = board[square]
        print(f'Square {square}, category {board[square]}')
        # if square is roll again, call the function again
        if category == categories['white']:
            self.roll_die()
        # if die goes on Start, the user must choose a category
        elif category == categories['start']:
            labeled_categories = dict(zip(ascii_lowercase, list(questions)))
            print('Choose a category for your question:')
            for label, question_category in labeled_categories:
                print(f" {label}) {question_category}")

            # check if the provided category is valid
            category_label_prompt = f"\nChoice? "
            category_error_message = f"Please choose one of the categories {', '.join(labeled_categories)}"
            category_checked = self.validate_input(category_label_prompt, labeled_categories, category_error_message)
            # the category is chosen from the user
            category = labeled_categories[category_checked]

        # ask question from a category
        self.ask_question(category)
        
