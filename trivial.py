import random
from board import categories, board
#from questions import questions

questions = [
    ("What year was the very first model of the iPhone released?", "2007"),
    ("What\’s the shortcut for the \“copy\” function on most computers?", "ctrl c"),
    ("What is often seen as the smallest unit of memory?", "kilobyte"),
    ("What is Hawkeye’s real name?", "Clint Barton")
    ]


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
    def ask_question(self):
        for question, correct_answer in questions:
            answer = input(f"{question}? ")
            if answer == correct_answer:
                print('Correct!')
            else:
                print(f"The answer is {correct_answer}, not {answer!r}")

    # get a random square in the table
    def roll_die(self):
        square = random.choice(board.keys())
        print('Rolling the die...')
        print(f'Square {square}, category {board[square]}')
        # if square is roll again, call the function again
        if board[square] == categories['white']:
            self.roll_dice()
        # TODO: what happens if square == start?
        # player chooses a color
        # ask a question from that color
        elif board[square] == categories['start']:
            pass
        # what happens if square == category?
        # ask question from that category
        else:
            self.ask_question()
        
class Trivia:
    questions = prepare_questions()

