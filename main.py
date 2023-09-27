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
        MINARMIES = 2
        MAXARMIES = 3

        territories = self.risk_map.get_territories()

        for territory in territories:
            player = random.choice(self.players)
            player.add_territory(territory)
            self.risk_map.set_owner(territory, player.name)
            self.risk_map.set_armies(territory, random.randint(MINARMIES, MAXARMIES))

        self.print_turn_info()
        self.get_status()
        self.reinforce()

    def print_turn_info(self):
        """Print information about the current turn."""
        print("\n------------------------------------------")
        print(f"It's the {self.turns_completed + 1} turn.")
        print(f"It's {self.get_current_player().name}'s turn.")
        print("------------------------------------------")

    def next_turn(self):
        """Move to the next player's turn."""
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.turns_completed += 1
        self.print_turn_info()
        self.get_status()
        self.reinforce()

    def get_current_player(self):
        """Get the current player."""
        return self.players[self.current_player_index]

    def get_status(self):
        """Print territories and armies for each player."""
        for player in self.players:
            print(f"\n{player.name} owns:")
            for territory in player.territories:
                print("  ", territory, self.risk_map.get_territory(territory)["armies"])

    #
    # -------------------------------------------------------------- REINFORCEMENT PHASE
    #

    def reinforce(self):
        """Reinforce a territory."""

        # # no reinforcements on first turn
        # if self.turns_completed % len(self.players) == 0:
        #     return

        # Print reinforcement phase message
        print("\nReinforcement phase.")

        # Calculate the base number of reinforcements based on the number of territories owned
        reinforcements = len(self.get_current_player().get_territories()) // 3

        # Ensure a minimum of 3 reinforcements
        reinforcements = max(reinforcements, 3)

        # Check if player owns all territories in a continent and add continent bonus armies
        for continent in self.risk_map.get_continents():
            continent_territories = self.risk_map.get_continent_territories(continent)

            # Filter player's territories in the current continent
            player_territories = filter(
                lambda x: self.risk_map.get_continent(x) == continent,
                self.get_current_player().get_territories(),
            )

            # Check if the player owns all territories in the continent
            if set(continent_territories) == set(player_territories):
                # Add continent bonus armies to reinforcements
                reinforcements += self.risk_map.get_continent_score(continent)

        # Loop until all reinforcements are placed
        while reinforcements > 0:
            player_territories = self.get_current_player().get_territories()

            # Get user input for selecting a territory to reinforce
            territory = input_with_autocomplete(
                f"{reinforcements} reinforcements. Territory: ", player_territories
            ).title()

            # Get user input for the number of armies to reinforce
            rf_amount = int(input("How many armies? "))

            # Check if the selected territory and reinforcement amount are valid
            if territory in player_territories and 1 <= rf_amount <= reinforcements:
                # Update the number of armies in the selected territory
                self.risk_map.set_armies(
                    territory, self.risk_map.get_armies(territory) + rf_amount
                )

                # Decrement the remaining reinforcements
                reinforcements -= rf_amount

        # Display the updated status of territories and armies
        self.get_status()

    #
    # --------------------------------------------------------------------- ATTACK PHASE
    #
    def check_attack_legitimacy(self, from_territory, to_territory):
        """Check if an attack is legitimate."""
        attacker = self.get_current_player()

        # Check if from_territory is owned by attacker
        if from_territory not in attacker.territories:
            print(f"{attacker.name} does not own {from_territory}!")
            return False
        # Check if to_territory is owned by the same attacker
        if to_territory in attacker.territories:
            print(f"{attacker.name} already owns {to_territory}!")
            return False
        # Check if to_territory is adjacent to from_territory
        if to_territory not in self.risk_map.get_neighbors(from_territory):
            print(f"{to_territory} is not adjacent to {from_territory}!")
            return False
        # Check if from_territory has more than 1 army
        if self.risk_map.get_armies(from_territory) <= 1:
            print(f"{from_territory} does not have enough armies!")
            return False

        return True

    def player_attack(self):
        """Attacker attacks a territory. Attacks continue until attacker loses or wins."""
        print("\nAttack phase.")

        # from territory form
        from_territory = input_with_autocomplete(
            "\nFrom: ", self.get_current_player().get_territories()
        ).title()

        # to territory form
        enemy_neighbors = list(
            filter(
                lambda x: self.risk_map.get_owner(x) != self.get_current_player().name,
                self.risk_map.get_neighbors(from_territory),
            )
        )
        print("Attackable territories:", enemy_neighbors)
        to_territory = input_with_autocomplete("To: ", enemy_neighbors).title()

        #  check validity of attack
        if not self.check_attack_legitimacy(from_territory, to_territory):
            return

        attacker = self.get_current_player()
        print(f"{attacker.name} attacks {to_territory} from {from_territory}!")

        from_armies = self.risk_map.get_armies(from_territory)
        to_armies = self.risk_map.get_armies(to_territory)
        attacking = int(input(f"You have {from_armies} armies. Attack with how many? "))

        if attacking < 1 or attacking > from_armies:
            print("Attack aborted. Be serious brother war is not a game.")
            return
        if from_armies - attacking < 1:
            print("You don't have that many armies!")
            return

        attack_rem = attacking
        defense_rem = to_armies

        while True:
            print(
                f"\nAttacking with {attack_rem} armies. Defending {defense_rem} armies."
            )

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

            keep_going = input_with_autocomplete("Keep going? (y/n) ", ["y", "n"])
            if keep_going == "n":
                self.risk_map.set_armies(
                    from_territory, from_armies - attacking + attack_rem
                )
                self.risk_map.set_armies(to_territory, defense_rem)
                break

        # If defender loses all territories, remove them from players list
        self.players = [p for p in self.players if p.territories]
        self.get_status()

    #
    # ------------------------------------------------------------- STRATEGIC MOVE PHASE
    #
    def check_move_legitimacy(self, from_territory, to_territory, amount):
        """Check if a strategic move is legitimate."""
        player = self.get_current_player()

        # Check if from_territory is owned by player
        if from_territory not in player.territories:
            print(f"{player.name} does not own {from_territory}!")
            return False
        # Check if to_territory is owned by player
        if to_territory not in player.territories:
            print(f"{player.name} does not own {to_territory}!")
            return False
        # Check if to_territory is adjacent to from_territory
        if to_territory not in self.risk_map.get_neighbors(from_territory):
            print(f"{to_territory} is not adjacent to {from_territory}!")
            return False
        # Check if from_territory has enough armies
        if self.risk_map.get_armies(from_territory) <= amount:
            print(f"{from_territory} does not have enough armies!")
            return False

        return True

    def strategic_move(self):
        # Get the territories involved in the strategic move

        # From territory form
        player_territories = self.get_current_player().get_territories()
        from_territory = input_with_autocomplete("\nFrom: ", player_territories).title()

        # To territory form
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

        # Amount form
        amount = int(input("Amount: "))

        # Check the validity of the strategic move
        if not self.check_move_legitimacy(from_territory, to_territory, amount):
            return

        # Perform the strategic move
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
        action = input_with_autocomplete(
            "\nAttack (a), Strategic Move (will end turn) (s), End Turn (e)?",
            ["a", "s", "e"],
        )
        if action == "a":
            game.player_attack()
        elif action == "s":
            game.strategic_move()
            game.next_turn()
        elif action == "e":
            game.next_turn()

    print(f"\n{game.get_current_player().name} wins!")
