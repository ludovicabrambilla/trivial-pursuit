import random
from string import ascii_lowercase
from board import categories, board
from questions import questions


class Player:
    # class var to keep track of the available tokens to be chosen
    available_tokens = {
        'a': 'pink',
        'b': 'yellow',
        'c': 'orange',
        'd': 'blue',
        'e': 'brown',
        'f': 'green'
    }

    # class var to keep track of the tokens already taken by other players
    taken_tokens = {}

    # Initialize the player. Ask for name and token they want to choose.
    def __init__(self):
        # make the user choose its name for the game
        name = input('Choose a name for your player: ').strip()
        self.name = name
        # make the user choose a token
        print('These are the available tokens:')
        for item,value in Player.available_tokens.items():
            print(f'{item}. {value}')
        token = input('Choose one token. Type the corresponding letter to make your choice: ').strip().lower()
        # TODO: reprompt the player if he doesn't choose a valid token
        try:
            Player.taken_tokens[self.name] = Player.available_tokens.pop(token)
            print(Player.available_tokens)
            print(Player.taken_tokens)
        except KeyError:
            # TODO: how to block the creation of a player without a token?
            print('Sorry, the token you chose is not available.')
        
        self.token = Player.taken_tokens[self.name]


    # TODO: prompt a question to the player
    def ask_question(self, category):
        # TODO: make num_correct an instance variable
        num_correct = 0 # keeps score
        question = random.choice(list(questions[categories[category]]))
        print(f"{question}")

        options = questions[categories[category]][question]
        correct_answer = options[0]
        # shuffle the order of the options with random sample
        # present the options as "a) option"
        labeled_options = dict(zip(ascii_lowercase, random.sample(options, k=len(options))))
        for label, option in labeled_options.items():
            print(f" {label}) {option}")

        # ERROR HANDLING: Reprompt the player if he/she gives an answer not in the options given
        answer_label = input(f"\nChoice? ").strip().lower()
        while answer_label not in labeled_options:
            print(f"Please answer one of {', '.join(labeled_options)}")


        answer = labeled_options[answer_label]
        if answer == correct_answer:
            num_correct += 1
            print('⭐ Correct!⭐')
        else:
            print(f"The answer is {correct_answer!r}, not {answer!r}")


    # simulate the player rolling the die
    def roll_die(self):
        print('Rolling the die...')
        # picks a random square from the board
        square = random.choice(board.keys())
        # check the corresponding category
        category = board[square]
        print(f'Square {square}, category {board[square]}')
        # if square is roll again, call the function again
        if board[square] == categories['white']:
            self.roll_dice()
        # TODO: what happens if square == start?
        # player chooses a color
        # ask a question from that color
        elif category == categories['start']:
            pass
        # what happens if square == category? ask question from that category
        else:
            self.ask_question(category)
        
