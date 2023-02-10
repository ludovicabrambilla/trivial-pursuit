import random

categories = {
    'brown': 'Arts & Literature',
    'pink': 'Entertainment',
    'blue': 'Geography',
    'yellow': 'History',
    'green': 'Science & Nature',
    'orange': 'Sports & Leisure',
    'white': 'Roll again',
    'start': 'Start'
}

board = {
    '0': categories['start'],
    'a1': categories['orange'],
    'a2': categories['pink'],
    'a3': categories['green'],
    'a4': categories['blue'],
    'a5': categories['brown'],
    'a6': categories['yellow'],
    'a7': categories['brown'],
    'a8': categories['white'],
    'a9': categories['green'],
    'a10': categories['orange'],
    'a11': categories['white'],
    'a12': categories['blue'],
    'b1': categories['yellow'],
    'b2': categories['green'],
    'b3': categories['brown'],
    'b4': categories['orange'],
    'b5': categories['blue'],
    'b6': categories['pink'],
    'b7': categories['blue'],
    'b8': categories['white'],
    'b9': categories['brown'],
    'b10': categories['yellow'],
    'b11': categories['white'],
    'b12': categories['orange'],
    'c1': categories['pink'],
    'c2': categories['brown'],
    'c3': categories['blue'],
    'c4': categories['yellow'],
    'c5': categories['orange'],
    'c6': categories['green'],
    'c7': categories['orange'],
    'c8': categories['white'],
    'c9': categories['blue'],
    'c10': categories['pink'],
    'c11': categories['white'],
    'c12': categories['yellow'],
    'd1': categories['green'],
    'd2': categories['blue'],
    'd3': categories['orange'],
    'd4': categories['pink'],
    'd5': categories['yellow'],
    'd6': categories['brown'],
    'd7': categories['yellow'],
    'd8': categories['white'],
    'd9': categories['orange'],
    'd10': categories['green'],
    'd11': categories['white'],
    'd12': categories['pink'],
    'e1': categories['brown'],
    'e2': categories['orange'],
    'e3': categories['yellow'],
    'e4': categories['green'],
    'e5': categories['pink'],
    'e6': categories['blue'],
    'e7': categories['pink'],
    'e8': categories['white'],
    'e9': categories['yellow'],
    'e10': categories['brown'],
    'e11': categories['white'],
    'e12': categories['green'],
    'f1': categories['blue'],
    'f2': categories['yellow'],
    'f3': categories['pink'],
    'f4': categories['brown'],
    'f5': categories['green'],
    'f6': categories['orange'],
    'f7': categories['green'],
    'f8': categories['white'],
    'f9': categories['pink'],
    'f10': categories['blue'],
    'f11': categories['white'],
    'f12': categories['brown']
}


class Player:
    # class var to keep track of the available tokens to be chosen
    available_tokens = {
        'pink': 'pink',
        'pink': 'yellow',
        'blue': 'orange',
        'yellow': 'blue',
        'green': 'brown',
        'orange': 'green'
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
        pass

    # get a random square in the table
    def roll_dice(self):
        square = random.choice(board.keys())
        print('Rolling the die...')
        print(f'Square {square}, category {board[square]}')
        # what happens if square == roll again?
        if board[square] == categories['white']:
            self.roll_dice()
        # TODO: what happens if square == start?
        elif board[square] == categories['start']:
            pass
        # what happens if square == category?
        else:
            self.ask_question()
        
