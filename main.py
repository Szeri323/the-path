import random

class Enemy:
    def __init__(self):
        pass
    
    def attack():
        pass

class Event:
    def __init__(self):
        self.__events_list = ['ambush', 'npc', 'treasure'] 
        
    def get_events_list(self):
        return self.__events_list
    
    def get_random_event(self):
        random_index = random.randint(0, len(self.__events_list)-1)
        random_event = self.__events_list[random_index]
        return random_event
    
    def event_action(self, event):
        if event == "ambush":
            enemy = Enemy()
            # turn fight mode
            print("BOOOOOOOO")
            pass
            
            # end fight mode
        if event == "npc":
            # create npc
            # npc can talk, give somthing or make a deal
            print("HELLO FRIEND")
            pass
            
        if event == "treasure":
            # treasure give some loot
            # it's chance for apear some monster or other adventurer
            print("MY PRESSIOUS")
            pass

class Path:
    def __init__(self, length):
        self.__length = length
        self.__path = self.create_path()
        self.__player_position = 0
    
    def create_path(self):
        path = []
        event = Event()
        path.append('')
        for i in range(1,self.__length):
            path.append(event.get_random_event())
        return path
    
    def show_path(self):
        print(self.__path)
        
    def move_player(self):
        event = Event()
        self.__player_position += 1
        print("player walk 1")
        
        return event.event_action(self.__path[self.__player_position])
        
class Player:
    def __init__(self):
        self.health = 10
        self.damage = 5
        self.backpack = []
        self.equipement = {}
    
    def show_map(self, path):
        # Take path list, make dictionary and set X on the active field
        pass
    
    def walk(self, path):
        # Position in Palyer or Path class?
        
        return path.move_player()
    
    def attack(self, target):
        pass
    
def main():
    print("How long The Path should be?")
    length = int(input())
    path = Path(length)
    path.show_path()
    player = Player()
    
    #players move
    print("plyers move")
    for _ in range(length-1):
        player.walk(path)

if __name__ == "__main__":
    main()