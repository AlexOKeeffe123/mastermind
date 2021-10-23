#Alex
class Player:
    def __init__(self, name):
        #sets the variables that will be used in the Player class
        self._turn = None
        self._name = name

    def get_name(self):
        #Gets the name of the current player
        return self._name

    def set_turn(self,turn):
        #sets the players last turn
        self._turn = turn

    def get_turn(self):
        #returns the players name
        return self._turn