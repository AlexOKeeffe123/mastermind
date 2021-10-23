#Alex
class Turn:
    def __init__(self,guess):
        self._guess = guess       

    def get_guess(self):
        #returns the players guess
        return self._guess