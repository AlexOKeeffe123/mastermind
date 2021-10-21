import random

#Chase
class board:
    """
    """

    def __int__(self):
        """
        """
        self.prepare()
        self.attempt = []
        self.guessmove = []


    def getguess(self, correct, guess):
        """
        """
        guessoutput = [''] * len(correct)

        for i, (correctnum, guessnum) in enumerate(self.correct, guess):
            guessoutput[i] = "X"
            if guessnum == correctnum:
                print(guessoutput)
            else:
                print('0')
            return ''.join(guessoutput)


    def _prepare(self):
        """ Sets up the board with a random number
        """
        attempt = random.randint(0,3)
        for n in range(attempt):
            guessmove = random.randint(1, 9)
            self.attempt.append(guessmove)
        return attempt

