#Alex
class Roster:
    def __init__(self):
        self.player_list = []


    def add_player(self): 
            self.player_list.append(self.name)
            player_count= int(input("How many palyers are playing today? "))
            for p in player_count:
                name = input(f"What is player{p+1}'s name? ")
                self.player_list.append(name)

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