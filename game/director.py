#Tyson
from game.player import Player
from game.board import Board
from game.display import Display
from game.roster import Roster
from game.turn  import Turn

# enhanced by allowing a variable length and player count

class Director:
    def __init__(self, numPlayers):
        self._numPlayers = numPlayers
        self._isRunning = True
        self._display = Display()
        self._roster = Roster()
        self._board = None

    def start_game(self):
        self._prepare_game()
        while self._isRunning ==  True:
            self._display.write(self._board.to_string())
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game(self): # populates roster and length of board
        secretLength = self._display.read(f"How long would you like the Secret Code to be? ")
        self._board = Board(secretLength)
        for p in range(self._numPlayers):
            name = self._display.read(f"Enter a name for player {p + 1}: ")
            player = Player(name)
            self._roster.add_player(player)
            self._board.prepare(player)

    def _get_inputs(self): #gets a turn
        player = self._roster.get_current()
        self._display.write(f"{player.get_name()}'s turn:")
        guess = self._display.read_int("What is your guess? ")
        turn = Turn(guess)
        player.set_turn(turn)

    def _do_updates(self): # makes the turns
        player = self._roster.get_current()
        turn = player.get_turn()
        self._board.apply(turn)

    def _do_outputs(self): #win condition
        lastTurn = self._roster.get_current().get_turn()
        if lastTurn == self._board.get_solution():
            winner = self._roster.get_current()
            name = winner.get_name()
            print(f"\n{name} won!")
            self._isRunning = False
        self._roster.next_player()