#Alex
class Roster:
    def __init__(self,):
        self.player_list = []

    def add_player(self): 
        num_players= int(input("How many players are playing today? "))
        for n in range(num_players):
            name = input(f"Enter the name of player{n+1}: ")
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
        print(f"{next_play_name}'s turn: ")