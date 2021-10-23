#Alex
class Roster:
    def __init__(self):
        #sets the variables that will be used in the Roster class
        self.player_list = []
        self.current = -1

    def add_player(self,player): 
        #takes the player name and adds it to a list
        self.player_list.append(player)

    def get_current(self):
        #gets the current player in the list
        return self.player_list[self.current]
        
    def next_player(self):
        count=len(self.player_list)
        #Starts the list over again
        if count == self.current:
            self.current = 0
        else:
            self.current +=1