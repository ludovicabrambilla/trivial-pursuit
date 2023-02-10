
board = {
    'Arts & Literature': ['a5', 'a7', 'b3', 'b9', 'c2', 'd6', 'e1', 'e10', 'f4', 'f12'],
    'Entertainment': ['a2', 'b6', 'c1', 'c10', 'd4', 'd12', 'e5', 'e7', 'f3', 'f9'],
    'Geography': ['a4', 'a12', 'b5', 'b7', 'c3', 'c9', 'd2', 'e6', 'f1', 'f10'],
    'History': ['a6', 'b1', 'b10', 'c4', 'c12', 'd5', 'd7', 'e3', 'e9', 'f2'],
    'Science & Nature': ['a3', 'a9', 'b2', 'c6', 'd1', 'd10', 'e4', 'e12', 'f5', 'f7'],
    'Sports & Leisure': ['a1', 'a10', 'b4', 'b12', 'c5', 'c7', 'd3', 'd9', 'e2', 'f6'],
    'Roll again': ['a8', 'a11', 'b8', 'b11', 'c8', 'c11', 'd8', 'd11', 'e8', 'e11', 'f8', 'f11'],
    'Start' : 0
}

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
            self.token = Player.taken_tokens[token]
        except KeyError:
            # TODO: how to block the creation of a player without a token?
            print('Sorry, the token you chose is not available.')


player1 = Player()
player2 = Player()