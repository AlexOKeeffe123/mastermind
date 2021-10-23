import random
from typing import Text

#Chase
class Board:
    def __init__(self, length):
        """The class constructor

		Args:
			self (Display): an instance of Display	
		"""
        self._items = {} # this is an empty dictionary
        self._solutionLength = length


    def to_string(self):
        """Converts the board data to its string representation.

        Args:
           self (Board): an instance of Board.

        Returns:
            string: A representation of the current board.
        """
        lines = "\n--------------"
        for i, (name, values) in enumerate(self._items):
            "Player {name}: ----, ****"
            lines += f"Player {name}: {values[1]}, {values[2]}"
        lines += "\n--------------"
        return lines


    def apply(self, turn):
        """ Applies the given turn to the playing surface. Gets player's turn, name, and values
        
        Args:
            self (Board): an instance of Board.
            turn (Turn): The turn to apply.
        """
        guesserName = turn.get_guesser_name()
        values = self._items[guesserName]
        values[1] = turn.get_guess()
        values[2] = self._create_hint(values[0], values[1])

    def prepare(self, player):
            """Sets up the board with an entry for each player.
            
            Args:
                self (Board): an instance of Board.
                player (string): gets player's values
            """
            name = player.get_name()
            code = str(random.randint(10 ** (self._solutionLength - 1), 10 ** self._solutionLength))

            
            name = player.get_name()
            code = str(random.randint(1000, 10000))
            
    def _create_hint(self, code, guess):
        """Generates a hint based on the given code and guess.

        Args:
            self (Board): An instance of Board.
            code (string): The code to compare with.
            guess (string): The guess that was made.

        Returns:
            string: A hint in the form [xxxx]"""
        
        hint = ""
        for index, letter in enumerate(guess):
            if code[index] == letter:
                hint += "x"
            elif letter in code:
                hint += "o"
            else:
                hint += "*"
        return hint

    def get_solution(self, name):
        """Gets solution

        Args:
            self (Board): An instance of Board.
       
        Return:
            name (String): gets player's name
            integer (Int): gets code"""
        
        return self._items[name][0]