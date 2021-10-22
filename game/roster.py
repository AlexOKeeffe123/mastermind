#Alex
class Roster:
    def __init__(self,name):
        self.player_list = []
        self.name = name

    def add_player(self): 
            self.player_list.append(self.name)

    def get_current(self):
        count=len(self.player_list)
        self.current_player_index = 0
        #Starts the list over again
        if count == self.current_player_index:
            self.current_player_index = 0
        else:
            self.current_player_index +=1
        

    def next_player(self):
        next_play_name = self.player_list[self.current_player_index]
        return next_play_name