import readline


def input_with_autocomplete(prompt, options=None):
    """
    A function that captures user input from the terminal with autocompletion support.

    Parameters:
    - prompt (str): A string that serves as the prompt or message displayed to the user before input.
    - options (list, optional): A list of autocompletion options. If None, a default list is used.

    Returns:
    str: The user's input obtained from the terminal with autocompletion.

    Usage:
    - Use this function to capture user input in a way that suggests autocompletion options based on the provided list.

    - Users can start typing, and when they press Tab, the function suggests autocompletion options based on the current input.

    - The function returns the final user input as a string.


    """

    def completer(text, state):
        # Use custom options list if provided, otherwise use default territory_options
        autocomplete_options = options or territory_options
        filtered_options = [
            opt for opt in autocomplete_options if opt.startswith(text.title())
        ]
        return filtered_options[state] if state < len(filtered_options) else None

    readline.set_completer(completer)
    readline.parse_and_bind("tab: complete")

    return input(prompt)


# Default list of territory options
territory_options = [
    "Alaska",
    "Alberta",
    "Central America",
    "Eastern United States",
    "Greenland",
    "Northwest Territories",
    "Ontario",
    "Quebec",
    "Western United States",
    "Argentina",
    "Brazil",
    "Peru",
    "Venezuela",
    "Great Britain",
    "Iceland",
    "Northern Europe",
    "Scandinavia",
    "Southern Europe",
    "Ukraine",
    "Western Europe",
    "Congo",
    "East Africa",
    "Egypt",
    "Madagascar",
    "North Africa",
    "South Africa",
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
    "Eastern Australia",
    "Indonesia",
    "New Guinea",
    "Western Australia",
]

if __name__ == "__main__":
    # Example usage:
    territory = input_with_autocomplete("Select a territory: ")

    territory = input_with_autocomplete("Select a territory: ", ["Alaska", "Alberta"])
