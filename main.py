import random

from gamemap import RiskMap
from player import Player
from attack import attack_roll
from autocomplete_input_territories import input_with_autocomplete

class Game:
    def __init__(self, players):
        """
        Initialize the game with a list of players.

        Args:
        - players (list): A list of Player objects representing the players in the game.
        """
        self.risk_map = RiskMap()
        self.players = players
        self.current_player_index = 0
        self.turns_completed = 0

    def start(self):
        """Start the game by assigning territories and armies."""
        territories = self.risk_map.get_territories()

        for territory in territories:
            player = random.choice(self.players)
            player.add_territory(territory)
            self.risk_map.set_owner(territory, player.name)
            self.risk_map.set_armies(territory, random.randint(2, 3))

        self.print_turn_info()
        self.get_status()
        self.reinforce()

    def print_turn_info(self):
        """Print information about the current turn."""
        print("\n------------------------------------------")
        print(f"It's the {self.turns_completed + 1} turn.")
        print(f"It's {self.get_current_player().name}'s turn.")
        print("------------------------------------------")

    def get_current_player(self):
        """Get the current player."""
        return self.players[self.current_player_index]

    def next_turn(self):
        """Move to the next player's turn."""
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.turns_completed += 1
        self.print_turn_info()
        self.get_status()
        self.reinforce()

    def reinforce(self):
        """Reinforce a territory."""
        print("\nReinforcement phase.")
        reinforcements = len(self.get_current_player().get_territories()) // 3

        if reinforcements < 3:
            reinforcements = 3

        # Check if player owns all territories in a continent and add continent bonus armies
        for continent in self.risk_map.get_continents():
            continent_territories = self.risk_map.get_continent_territories(continent)
            player_territories = filter(
                lambda x: self.risk_map.get_continent(x) == continent,
                self.get_current_player().get_territories(),
            )

            if set(continent_territories) == set(player_territories):
                reinforcements += self.risk_map.get_continent_score(continent)

        player_territories = self.get_current_player().get_territories()
        territory = input_with_autocomplete(
            f"{reinforcements} reinforcements. Territory: ", player_territories
        ).title()

        if territory in player_territories:
            self.risk_map.set_armies(
                territory, self.risk_map.get_armies(territory) + reinforcements
            )
            self.get_status()
        else:
            return  # Add loop check

    def get_status(self):
        """Print territories and armies for each player."""
        for player in self.players:
            print(f"\n{player.name} owns:")
            for territory in player.territories:
                print("  ", territory, self.risk_map.get_territory(territory)["armies"])

    def player_attack(self):
        """Attacker attacks a territory."""
        print("\nAttack phase.")

        from_territory = input_with_autocomplete(
            "\nFrom: ", self.get_current_player().get_territories()
        ).title()

        enemy_neighbors = list(
            filter(
                lambda x: self.risk_map.get_owner(x) != self.get_current_player().name,
                self.risk_map.get_neighbors(from_territory),
            )
        )

        print("Attackable territories:", enemy_neighbors)

        to_territory = input_with_autocomplete("To: ", enemy_neighbors).title()

        attacker = self.get_current_player()

        print(f"{attacker.name} attacks {to_territory} from {from_territory}!")

        # Check if from_territory is owned by attacker
        if from_territory not in attacker.territories:
            print(f"{attacker.name} does not own {from_territory}!")
            return
        # Check if to_territory is owned by the same attacker
        if to_territory in attacker.territories:
            print(f"{attacker.name} already owns {to_territory}!")
            return
        # Check if to_territory is adjacent to from_territory
        if to_territory not in self.risk_map.get_neighbors(from_territory):
            print(f"{to_territory} is not adjacent to {from_territory}!")
            return
        # Check if from_territory has more than 1 army
        if self.risk_map.get_armies(from_territory) <= 1:
            print(f"{from_territory} does not have enough armies!")
            return

        from_armies = self.risk_map.get_armies(from_territory)
        to_armies = self.risk_map.get_armies(to_territory)
        attacking = int(input(f"You have {from_armies} armies. Attack with how many? "))

        if attacking == 0:
            print("Attack aborted.")
            return
        if from_armies - attacking < 1:
            print("You don't have that many armies!")
            return

        attack_rem = attacking
        defense_rem = to_armies

        while True:
            attack_rem, defense_rem = attack_roll(attack_rem, defense_rem)

            if attack_rem < 1:
                print("Attack aborted.")
                self.risk_map.set_armies(
                    from_territory, from_armies - attacking + attack_rem
                )
                self.risk_map.set_armies(to_territory, defense_rem)
                break

            if defense_rem < 1:
                print(f"{attacker.name} wins! Now owns {to_territory}!")

                for p in self.players:
                    if to_territory in p.territories:
                        p.territories.remove(to_territory)

                self.risk_map.set_armies(from_territory, from_armies - attacking)
                self.risk_map.set_armies(to_territory, attack_rem)
                self.risk_map.set_owner(to_territory, attacker.name)
                attacker.add_territory(to_territory)
                break

        # If defender loses all territories, remove them from players list
        self.players = [p for p in self.players if p.territories]
        self.get_status()

    def strategic_move(self):
        player_territories = self.get_current_player().get_territories()
        from_territory = input_with_autocomplete("\nFrom: ", player_territories).title()

        owned_neighbor_territories = list(
            filter(
                lambda x: self.risk_map.get_owner(x) == self.get_current_player().name,
                self.risk_map.get_neighbors(from_territory),
            )
        )

        print("Neighboring Owned:", owned_neighbor_territories)

        to_territory = input_with_autocomplete(
            "To: ", owned_neighbor_territories
        ).title()
        amount = int(input("Amount: "))

        if amount > self.risk_map.get_armies(from_territory) - 1:
            print("You don't have that many armies!")
            return

        if (
            from_territory not in player_territories
            or to_territory not in player_territories
        ):
            print("You don't own those territories!")
            return

        if to_territory not in self.risk_map.get_neighbors(from_territory):
            print(f"{to_territory} is not adjacent to {from_territory}!")
            return

        self.risk_map.set_armies(
            from_territory, self.risk_map.get_armies(from_territory) - amount
        )
        self.risk_map.set_armies(
            to_territory, self.risk_map.get_armies(to_territory) + amount
        )


if __name__ == "__main__":
    # Create players
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    player3 = Player("player 3")
    player4 = Player("player 4")
    player5 = Player("player 5")
    player6 = Player("player 6")

    # Create a game instance
    players_list = [
        player1,
        player2,
        player3,
        # player4,
        # player5,
        # player6
    ]
    game = Game(players_list)

    game.start()

    while len([player for player in players_list if player.territories]) > 1:
        action = input(
            "\nAttack (a), Strategic Move (will end turn) (s), End Turn (e)?"
        )
        if action == "a":
            game.player_attack()
        elif action == "s":
            game.strategic_move()
            game.next_turn()
        elif action == "e":
            game.next_turn()

    print(f"\n{game.get_current_player().name} wins!")
