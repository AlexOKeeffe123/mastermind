#Alex
class Roster:
    def __init__(self):
        #sets the variables that will be used in the Roster class
        self.player_list = []
        self.current = 0

    def add_player(self,player): 
        #takes the player name and adds it to a list
        self.player_list.append(player)

    def get_current(self):
        #gets the current player in the list
        return self.player_list[self.current]
        
    def next_player(self):
        maxPlayerIndex = len(self.player_list) - 1
        #Starts the list over again
        if maxPlayerIndex == self.current:
            self.current = 0
        else:
            self.current += 1