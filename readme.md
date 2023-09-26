# RiskGame

The `RiskGame` class represents a game of Risk.

### Properties

- `players`: A list of `Player` objects representing the players in the game.
- `current_player_index`: An integer representing the index of the current player in the `players` list.
- `turns_completed`: An integer representing the number of turns completed in the game.
- `risk_map`: A `RiskMap` object representing the game board.

### Methods

- `__init__(self, player_names)`: Initializes a new game with the given player names.
- `get_current_player(self) -> Player`: Returns the current player.
- `next_turn(self) -> None`: Moves to the next player's turn.
- `reinforce(self) -> None`: Performs the reinforcement phase of the current player's turn.
- `get_status(self) -> str`: Returns a string representation of the territories and armies for each player.

## Player

The `Player` class represents a player in the game.

### Properties

- `name`: A string representing the player's name.
- `territories`: A list of strings representing the territories owned by the player.

### Methods

- `__init__(self, name)`: Initializes a new player with the given name.
- `add_territory(self, territory) -> None`: Adds a territory to the player's list of territories.
- `remove_territory(self, territory) -> None`: Removes a territory from the player's list of territories.
- `get_territories(self) -> List[str]`: Returns a list of the player's territories.

## RiskMap

The `RiskMap` class represents the game board.

### Properties

- `territories`: A dictionary mapping territory names to `Territory` objects.
- `continents`: A dictionary mapping continent names to lists of territory names.

### Methods

- `__init__(self, territories, continents)`: Initializes a new game board with the given territories and continents.
- `get_territories(self) -> List[str]`: Returns a list of all territory names.
- `get_continents(self) -> List[str]`: Returns a list of all continent names.
- `get_continent_territories(self, continent) -> List[str]`: Returns a list of territory names in the given continent.
- `get_continent_score(self, continent) -> int`: Returns the bonus armies for owning all territories in the given continent.
- `set_owner(self, territory, owner) -> None`: Sets the owner of the given territory.
- `get_owner(self, territory) -> str`: Returns the owner of the given territory.
- `set_armies(self, territory, armies) -> None`: Sets the number of armies on the given territory.
- `get_armies(self, territory) -> int`: Returns the number of armies on the given territory.
