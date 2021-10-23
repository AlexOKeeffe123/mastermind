#Tyson
from game.player import Player
from game.board import Board
from game.display import Display
from game.roster import Roster
from game.turn  import Turn

# enhanced by allowing a variable length and player count

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller
    Attributes:
        board (Board): An instance of the class of objects known as Board.
        display (Display): An instance of the class of objects known as Display.
        isRunning (boolean): Whether or not the game can continue.
        turn (Turn): An instance of the class of objects known as Turn.
        roster (Roster): An instance of the class of objects known as Roster.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._numPlayers = None
        self._isRunning = True
        self._display = Display()
        self._roster = Roster()
        self._board = None

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._prepare_game()
        while self._isRunning ==  True:
            self._display.write(self._board.to_string())
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game(self): 
        """Prepares the game before it begins. In this case, that means determing how many players, how long the Secret Code should be, 
        getting the player names, and adding them to the roster.
        
        Args:
            self (Director): An instance of Director.
        """
        self._numPlayers = self._display.read_int("How many players are there? ")
        secretLength = self._display.read("How long would you like the Secret Code to be? ")
        self._board = Board(secretLength)
        for p in range(self._numPlayers):
            name = self._display.read(f"Enter a name for player {p + 1}: ")
            player = Player(name)
            self._roster.add_player(player)
            self._board.prepare(player)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the turn from the current player.

        Args:
            self (Director): An instance of Director.
        """
        player = self._roster.get_current()
        self._display.write(f"{player.get_name()}'s turn:")
        guess = self._display.read_int("What is your guess? ")
        turn = Turn(guess, player.get_name())
        player.set_turn(turn)

    def _do_updates(self): 
        """Updates the important game information for each round of play. In 
        this case, that means updating the board with the current turn.

        Args:
            self (Director): An instance of Director.
        """
        player = self._roster.get_current()
        turn = player.get_turn()
        self._board.apply(turn)

    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if the latest turn matches the solution
        .
        Args:
            self (Director): An instance of Director.
        """
        lastTurn = self._roster.get_current().get_turn()
        if lastTurn == self._board.get_solution(lastTurn.get_guesser_name()):
            winner = self._roster.get_current()
            name = winner.get_name()
            print(f"\n{name} won!")
            self._isRunning = False
        self._roster.next_player()