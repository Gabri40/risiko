
class RiskMap:
    def __init__(self):
        # Initialize the map data
        self.map_data = {
            # north america
            "Alaska": {
                "continent": "North America",
                "neighbors": ["Alberta", "Northwest Territories", "Kamchatka"],
                "owner": None,
                "armies": 0,
            },
            "Alberta": {
                "continent": "North America",
                "neighbors": [
                    "Alaska",
                    "Northwest Territories",
                    "Ontario",
                    "Western United States",
                ],
                "owner": None,
                "armies": 0,
            },
            "Northwest Territories": {
                "continent": "North America",
                "neighbors": ["Alaska", "Alberta", "Ontario", "Greenland"],
                "owner": None,
                "armies": 0,
            },
            "Greenland": {
                "continent": "North America",
                "neighbors": ["Northwest Territories", "Ontario", "Quebec", "Iceland"],
                "owner": None,
                "armies": 0,
            },
            "Ontario": {
                "continent": "North America",
                "neighbors": [
                    "Alberta",
                    "Northwest Territories",
                    "Greenland",
                    "Quebec",
                    "Western United States",
                    "Eastern United States",
                ],
                "owner": None,
                "armies": 0,
            },
            "Quebec": {
                "continent": "North America",
                "neighbors": ["Greenland", "Ontario", "Eastern United States"],
                "owner": None,
                "armies": 0,
            },
            "Western United States": {
                "continent": "North America",
                "neighbors": [
                    "Alberta",
                    "Ontario",
                    "Eastern United States",
                    "Central America",
                ],
                "owner": None,
                "armies": 0,
            },
            "Eastern United States": {
                "continent": "North America",
                "neighbors": [
                    "Ontario",
                    "Quebec",
                    "Western United States",
                    "Central America",
                ],
                "owner": None,
                "armies": 0,
            },
            "Central America": {
                "continent": "North America",
                "neighbors": [
                    "Western United States",
                    "Eastern United States",
                    "Venezuela",
                ],
                "owner": None,
                "armies": 0,
            },
            # south america
            "Argentina": {
                "continent": "South America",
                "neighbors": ["Brazil", "Peru"],
                "owner": None,
                "armies": 0,
            },
            "Brazil": {
                "continent": "South America",
                "neighbors": ["Argentina", "Peru", "Venezuela", "North Africa"],
                "owner": None,
                "armies": 0,
            },
            "Peru": {
                "continent": "South America",
                "neighbors": ["Argentina", "Brazil", "Venezuela"],
                "owner": None,
                "armies": 0,
            },
            "Venezuela": {
                "continent": "South America",
                "neighbors": ["Brazil", "Peru", "Central America"],
                "owner": None,
                "armies": 0,
            },
            # europe
            "Great Britain": {
                "continent": "Europe",
                "neighbors": [
                    "Iceland",
                    "Scandinavia",
                    "Northern Europe",
                    "Western Europe",
                ],
                "owner": None,
                "armies": 0,
            },
            "Iceland": {
                "continent": "Europe",
                "neighbors": ["Greenland", "Great Britain", "Scandinavia"],
                "owner": None,
                "armies": 0,
            },
            "Northern Europe": {
                "continent": "Europe",
                "neighbors": [
                    "Great Britain",
                    "Scandinavia",
                    "Western Europe",
                    "Southern Europe",
                    "Ukraine",
                ],
                "owner": None,
                "armies": 0,
            },
            "Scandinavia": {
                "continent": "Europe",
                "neighbors": ["Great Britain", "Iceland", "Northern Europe", "Ukraine"],
                "owner": None,
                "armies": 0,
            },
            "Southern Europe": {
                "continent": "Europe",
                "neighbors": [
                    "Northern Europe",
                    "Western Europe",
                    "Egypt",
                    "North Africa",
                    "Middle East",
                    "Ukraine",
                ],
                "owner": None,
                "armies": 0,
            },
            "Ukraine": {
                "continent": "Europe",
                "neighbors": [
                    "Northern Europe",
                    "Scandinavia",
                    "Southern Europe",
                    "Ural",
                    "Afghanistan",
                    "Middle East",
                ],
                "owner": None,
                "armies": 0,
            },
            "Western Europe": {
                "continent": "Europe",
                "neighbors": [
                    "Northern Europe",
                    "North Africa",
                    "Southern Europe",
                    "Great Britain",
                ],
                "owner": None,
                "armies": 0,
            },
            # africa
            "Congo": {
                "continent": "Africa",
                "neighbors": ["North Africa", "East Africa", "South Africa"],
                "owner": None,
                "armies": 0,
            },
            "East Africa": {
                "continent": "Africa",
                "neighbors": [
                    "Egypt",
                    "North Africa",
                    "Congo",
                    "South Africa",
                    "Madagascar",
                ],
                "owner": None,
                "armies": 0,
            },
            "Egypt": {
                "continent": "Africa",
                "neighbors": [
                    "Southern Europe",
                    "North Africa",
                    "East Africa",
                    "Middle East",
                ],
                "owner": None,
                "armies": 0,
            },
            "Madagascar": {
                "continent": "Africa",
                "neighbors": ["East Africa", "South Africa"],
                "owner": None,
                "armies": 0,
            },
            "North Africa": {
                "continent": "Africa",
                "neighbors": [
                    "Brazil",
                    "Egypt",
                    "East Africa",
                    "Congo",
                    "Western Europe",
                    "Southern Europe",
                ],
                "owner": None,
                "armies": 0,
            },
            "South Africa": {
                "continent": "Africa",
                "neighbors": ["Congo", "East Africa", "Madagascar"],
                "owner": None,
                "armies": 0,
            },
            # asia
            "Kamchatka": {
                "continent": "Asia",
                "neighbors": ["Alaska", "Japan", "Mongolia", "Cita", "Jakutsk"],
                "owner": None,
                "armies": 0,
            },
            "Afghanistan": {
                "continent": "Asia",
                "neighbors": ["Ukraine", "Ural", "China", "Middle East"],
                "owner": None,
                "armies": 0,
            },
            "China": {
                "continent": "Asia",
                "neighbors": [
                    "Mongolia",
                    "Siberia",
                    "Ural",
                    "Afghanistan",
                    "India",
                    "Siam",
                    "Middle East",
                ],
                "owner": None,
                "armies": 0,
            },
            "India": {
                "continent": "Asia",
                "neighbors": ["China", "Siam", "Middle East"],
                "owner": None,
                "armies": 0,
            },
            "Cita": {
                "continent": "Asia",
                "neighbors": ["Kamchatka", "Jacuzia", "Mongolia", "Siberia"],
                "owner": None,
                "armies": 0,
            },
            "Japan": {
                "continent": "Asia",
                "neighbors": ["Kamchatka", "Mongolia"],
                "owner": None,
                "armies": 0,
            },
            "Middle East": {
                "continent": "Asia",
                "neighbors": [
                    "Afghanistan",
                    "India",
                    "China",
                    "Southern Europe",
                    "Ukraine",
                    "Egypt",
                ],
                "owner": None,
                "armies": 0,
            },
            "Mongolia": {
                "continent": "Asia",
                "neighbors": ["China", "Cita", "Japan", "Kamchatka", "Siberia"],
                "owner": None,
                "armies": 0,
            },
            "Siam": {
                "continent": "Asia",
                "neighbors": ["China", "India", "Indonesia"],
                "owner": None,
                "armies": 0,
            },
            "Siberia": {
                "continent": "Asia",
                "neighbors": ["China", "Cita", "Mongolia", "Ural", "Jacuzia"],
                "owner": None,
                "armies": 0,
            },
            "Ural": {
                "continent": "Asia",
                "neighbors": ["Afghanistan", "China", "Siberia", "Ukraine"],
                "owner": None,
                "armies": 0,
            },
            "Jacuzia": {
                "continent": "Asia",
                "neighbors": ["Cita", "Kamchatka", "Siberia"],
                "owner": None,
                "armies": 0,
            },
            # indonesia
            "Eastern Australia": {
                "continent": "Australia",
                "neighbors": ["New Guinea", "Western Australia"],
                "owner": None,
                "armies": 0,
            },
            "Indonesia": {
                "continent": "Australia",
                "neighbors": ["New Guinea", "Western Australia", "Siam"],
                "owner": None,
                "armies": 0,
            },
            "New Guinea": {
                "continent": "Australia",
                "neighbors": ["Eastern Australia", "Indonesia", "Western Australia"],
                "owner": None,
                "armies": 0,
            },
            "Western Australia": {
                "continent": "Australia",
                "neighbors": ["Eastern Australia", "Indonesia", "New Guinea"],
                "owner": None,
                "armies": 0,
            },
        }

        # Initialize the continents
        self.continents = {
            "North America": [
                "Alaska",
                "Alberta",
                "Central America",
                "Eastern United States",
                "Greenland",
                "Northwest Territories",
                "Ontario",
                "Quebec",
                "Western United States",
            ],
            "South America": ["Argentina", "Brazil", "Peru", "Venezuela"],
            "Europe": [
                "Great Britain",
                "Iceland",
                "Northern Europe",
                "Scandinavia",
                "Southern Europe",
                "Ukraine",
                "Western Europe",
            ],
            "Africa": [
                "Congo",
                "East Africa",
                "Egypt",
                "Madagascar",
                "North Africa",
                "South Africa",
            ],
            "Asia": [
                "Afghanistan",
                "China",
                "India",
                "Irkutsk",
                "Japan",
                "Kamchatka",
                "Middle East",
                "Mongolia",
                "Siam",
                "Siberia",
                "Ural",
                "Yakutsk",
            ],
            "Australia": [
                "Eastern Australia",
                "Indonesia",
                "New Guinea",
                "Western Australia",
            ],
        }

        # Continets score:
        self.continents_score = {
            "North America": 5,
            "South America": 2,
            "Europe": 5,
            "Africa": 3,
            "Asia": 7,
            "Australia": 2,
        }

    def get_territory(self, territory):
        """Return a dictionary containing information about the given territory."""
        return self.map_data[territory]

    def get_territories(self):
        """Return a list of all territories."""
        return list(self.map_data.keys())

    def get_continents(self):
        """Return a list of all continents."""
        return list(self.continents.keys())

    def get_neighbors(self, territory):
        """Return a list of neighboring territories for the given territory."""
        return self.map_data[territory]["neighbors"]

    def get_continent(self, territory):
        """Return the continent to which the given territory belongs."""
        return self.map_data[territory]["continent"]

    def get_owner(self, territory):
        """Return the current owner of the given territory."""
        return self.map_data[territory]["owner"]

    def set_owner(self, territory, player):
        """Set the owner of the given territory to the specified player."""
        self.map_data[territory]["owner"] = player

    def get_armies(self, territory):
        """Return the number of armies on the given territory."""
        return self.map_data[territory]["armies"]

    def set_armies(self, territory, num_armies):
        """Set the number of armies on the given territory."""
        self.map_data[territory]["armies"] = num_armies

    def get_continent_territories(self, continent):
        """Return a list of territories in the given continent."""
        return self.continents[continent]

    def get_continent_score(self, continent):
        """Return the score of the given continent."""
        return self.continents_score[continent]
