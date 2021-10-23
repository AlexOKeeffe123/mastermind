#Alex
class Turn:
    def __init__(self,guess, guesser_name):
        self._guess = guess       
        self._guesser_name = guesser_name

    def get_guess(self):
        #returns the players guess
        return self._guess
    
    def get_guesser_name(self):
        #Gets the current guesser's name
        return self._guesser_name