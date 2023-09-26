class Player:
    def __init__(self, name):
        self.name = name
        self.territories = []  # List of territories owned by the player
        # self.cards = []  # List of cards held by the player (if your game includes cards)

    def add_territory(self, territory):
        """Add a territory to the player's list of owned territories."""
        self.territories.append(territory)

    def remove_territory(self, territory):
        """Remove a territory from the player's list of owned territories."""
        if territory in self.territories:
            self.territories.remove(territory)

    def get_territories(self):
        """Return a list of territories owned by the player."""
        return self.territories

    
