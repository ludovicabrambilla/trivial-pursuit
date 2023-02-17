import random
from player import Player
from utility import validate_option, print_options
from questions import default_questions, default_categories
from board import Board


class Game:
    tokens = [i for i in Board.colors]

    min_players = 2
    max_players = 6

    def __init__(self):
        print('\n\nWELCOME TO OUR TRIVIA GAME!!! ENJOY AND HAVE FUN!\n\n')
        print('Let\'s first set up the game. Please, follow the instructions to change the game settings.\n\n')

        # Game setup
        self.board = Board()
        self.category_names = default_categories
        self.categories = {color:category_name for (color, category_name) in zip(self.board.colors, self.category_names)}
        self.questions = default_questions

        # Players setup
        self.players_num = self.get_number_of_players()
        self.available_tokens = random.sample(Game.tokens, k=self.players_num)
        self.taken_tokens = {}
        self.players = self.create_players(self.players_num)
        self.ordered_players = self.get_players_order()
        self.play(self.ordered_players)

    # CREATE PLAYERS AND UPDATE THE NUMBER OF TOKENS
    # Ask the user how many players he/she wants to create
    def get_number_of_players(self):
        while True:
            num = input("\nHow many players do you want to create (min. 2 - max. 6)? ").strip().lower()
            try:
                num = int(num)
                if num >= 2 and num <= 6:
                    return num
                else:
                    print("Sorry, you entered an invalid number of players.")
            except ValueError:
                print("Please enter a number.")

    # Create players (as many as indicated with get_number_of_players)
    def create_players(self, number):
        self.players = []
        for i in range(number):
            player = Player(self)
            self.players.append(player)
            print(f"\nPlayer n. {i+1}, \"{player.name}\" created successfully.")
            self.update_tokens(player)
        return self.players
    
    # Update the number of tokens each time a player is created
    def update_tokens(self, player):
        # Add the token to the taken tokens
        self.taken_tokens[player.name] = player.token
        # Remove it from the available tokens
        self.available_tokens.remove(player.token)

    # Define the order of the players
    def get_players_order(self):
        return random.sample(self.players, k=len(self.players))
    
    # Check who is playing
    def check_is_playing(self, players):
        for player in players:
            if player.is_playing == True:
                self.playing = player

    def get_color_from_square(self, square):
        color = self.board.squares[square]
        return color

    # DEFINE THE PATHS THE GAME TAKES AFTER THE PLAYER ROLLS THE DIE
    def get_category(self, player):
        square = player.roll_die(self.board.squares)
        print(f'The player is on {square}')
        color = self.get_color_from_square(square)
        if color == 'roll again':
            self.get_category(player)
        elif color == 'start':
            return self.choose_category()
        else:
            # category is already assigned to the square
            return self.categories[color]
            
    
    # Make the user choose a category for the question
    def choose_category(self):
        print('Please, choose a category.')
        labeled_categories = print_options(self.categories.values())
        # check if the provided category is valid
        category_checked = validate_option(
            validation_list=labeled_categories,
            user_input=f"\nChoice? ",
            error_message=f"Please choose one of the categories {', '.join(labeled_categories)}"
            )
        # the category is chosen from the user
        return labeled_categories[category_checked]

   

    # ASK A QUESTION TO THE PLAYER    
    def ask_question(self, category):
        print(f'\nThe category is: {category}')
        # Display the question
        question = random.choice(list(self.questions[category]))
        print(f"\n{question}")
        # Get the answer options (use question as key)
        options = self.questions[category][question]
        # Get the correct answer (it is always the first in the options list)
        correct_answer = options[0]
        # Shuffle the order of the options with a random sample that takes all the available options and print them
        labeled_options = print_options(random.sample(options, k=len(options)))
        # ERROR HANDLING: Reprompt the player if he/she gives an answer not in the options given
        answer_checked = validate_option(
            labeled_options,
            f"\nChoice? ",
            f"Please answer one of {', '.join(labeled_options)}"
            )
        answer = labeled_options[answer_checked]
        if answer == correct_answer:
            print('\n⭐ Correct!⭐\n')
            return True
        else:
            print(f"\nSorry, incorrect answer. The answer is {correct_answer!r}, not {answer!r}\n")
            return False        
              

    # After instantiating the game, play it
    def play(self, players):
        print(' \n--------------------------------------------------------------------')
        print('\n\nOkay, now that everything is set...LET THE GAMES BEGIN!!!\n\n')
        print('--------------------------------------------------------------------\n')
        
        for player in players:
            print(f'It\'s \"{player.name}\"\'s turn.')
            self.playing = player
            player.is_playing = True
            while player.is_playing:
                print(f'{player.name} is playing: {player.is_playing}')
                category = self.get_category(player)
                color = self.get_color_from_square(player.square)
                
                player_on_special = player.is_on_special()
                player_can_win = player.can_win()

                if player_on_special:
                    print('You play for a token!')
                elif player_can_win:
                    print('YOU PLAY TO WIN!')

                answer = self.ask_question(category)
                if answer:
                    if player_on_special:
                        player.add_point(color)
                    elif player.can_win():
                        print('***************************')
                        print(f'{player} won the game!!!!')
                        print('***************************')
                        return False
                print(f'{player.score}')
            player.is_playing = False
