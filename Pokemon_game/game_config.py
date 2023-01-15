import pokemons as p


class Player:
    def __init__(self, name: str):
        self.name = name
        self.pokemon = p.choose_pokemon()


class Game:
    def __init__(self):
        self.player1 = self.set_player()
        self.player2 = self.set_player()

    @staticmethod
    def set_player():
        name = input("Insert your name: ")
        player = Player(name)
        return player

    @staticmethod
    def game_ui(player: Player, initial_hp: int):
        print(f"What will {player.pokemon.name} do?")
        print(f"{player.pokemon.name}: {player.pokemon.life}/{initial_hp}")
        print("1- Attack\n2- Defense")

    @staticmethod
    def action_selected():

    def play(self):
        p1_start_hp = self.player1.pokemon.life
        p2_start_hp = self.player2.pokemon.life

        for player in [self.player1, self.player2]:
            if player == self.player1:
                self.game_ui(player, p1_start_hp)
            else:
                self.game_ui(player, p2_start_hp)
            choose = int(input("Select: "))
