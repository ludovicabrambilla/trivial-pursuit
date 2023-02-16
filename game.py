from trivial import Player

class Game:
    min_players = 2
    max_players = 6

    def __init__(self):
        self.players_num = self.get_number_of_players()
        self.players = []
        self.create_players(self.players_num)

    def get_number_of_players(self):
        try:
            num = int(input("How many players do you want to create (min. 2 - max. 6)?\n ").strip().lower())
            if num >= 2 and num <= 6:
                return num
            else:
                print("Sorry, you entered an invalid number of players.")
        except ValueError:
            print("Please enter a number.")

    def create_players(self, number):
        for i in range(number):
            player = Player()
            self.players.append(player)
            print(f"Player n. {i+1}, \"{player.name}\" created successfully.")
        return self.players
        

game = Game()
