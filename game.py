import random
from trivial import Player
from utility import validate_option, print_options
from questions import default_questions, default_categories
from board import Board




class Game:
    tokens = [i for i in Board.colors]

    min_players = 2
    max_players = 6

    def __init__(self):
        # Game setup
        self.board = Board()
        self.categories = {}
        self.questions = {}
        self.customize = self.ask_if_customize()

        # Players setup
        self.players_num = self.get_number_of_players()
        self.players = []
        self.available_tokens = Game.tokens[:self.players_num]
        self.taken_tokens = {}

        self.create_players(self.players_num)
    

    # Ask the user if they want to customize their categories and questions
    def ask_if_customize(self):
        print("The game provides standard categories and questions for each category.\nHowever, you can make your own categories and questions.")
        while True:
            customize = input("Do you want to create your own categories (y/n)? ").strip().lower()
            if customize == 'y':
                # call the function to create the categories
                self.create_categories()
                # call the function to create the questions
                self.create_questions()
                return True
            elif customize == 'n':
                # provide the default categories
                category_names = ['Geography', 'Arts & Literature', 'Science & Nature', 'History','Sports & Leisure', 'Entertainment']
                self.categories = {color:category_name for (color, category_name) in zip(self.board.colors, category_names)}
                # provide the default questions
                self.questions = default_questions
                return False
            
            print('Please enter a valid answer ("y" or "n").')


    # Allow the user to choose the categories for its game. Provide a default values.
    def create_categories(self):
        pass

    def create_questions(self):
        pass


    # CREATE PLAYERS AND UPDATE THE NUMBER OF TOKENS
    # Ask the user how many players he/she wants to create
    def get_number_of_players(self):
        try:
            num = int(input("How many players do you want to create (min. 2 - max. 6)?\n ").strip().lower())
            if num >= 2 and num <= 6:
                return num
            else:
                print("Sorry, you entered an invalid number of players.")
        except ValueError:
            print("Please enter a number.")

    # Create players (as many as indicated with get_number_of_players)
    def create_players(self, number):
        for i in range(number):
            player = Player(self)
            self.players.append(player)
            print(f"Player n. {i+1}, \"{player.name}\" created successfully.")
            self.update_tokens(player)
        return self.players
    
    # Update the number of tokens each time a player is created
    def update_tokens(self, player):
        # Add the token to the taken tokens
        self.taken_tokens[player.name] = player.token
        # Remove it from the available tokens
        self.available_tokens.remove(player.token)

    def validate_roll_die(self, player, square):
        # check the corresponding category
        color = self.board.squares[square]
        if color == 'roll again':
            player.roll_die()
        # if die goes on Start, the user must choose a category
        elif color == 'start':
            category = self.ask_category()
        else:
            category = self.categories[color]
        print(category)
        # ask question from a category
        self.ask_question(category)

    def ask_category(self):
        labeled_categories = print_options(self.categories.values())
        # check if the provided category is valid
        category_checked = validate_option(
            labeled_categories,
            f"\nChoice? ",
            f"Please choose one of the categories {', '.join(labeled_categories)}"
            )
        # the category is chosen from the user
        category = labeled_categories[category_checked]
        return category


    def ask_question(self, category):
        # Choose a question
        question = random.choice(list(self.questions[category]))
        print(f"{question}")
        # Get the answer options (use question as key)
        options = self.questions[category][question]
        # the correct answer is always the first in the options list
        correct_answer = options[0]
        # shuffle the order of the options with a random sample that takes all the available options and print them
        labeled_options = print_options(random.sample(options, k=len(options)))
        # ERROR HANDLING: Reprompt the player if he/she gives an answer not in the options given
        answer_checked = validate_option(
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

game1 = Game()
game1.validate_roll_die(game1.players[0], 'a1')