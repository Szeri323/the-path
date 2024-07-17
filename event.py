import random

class Event:
    def __init__(self):
        self._events_list = ['', 'enemy', 'npc', 'treasure'] 
        
    def get_events_list(self):
        return self._events_list
    
    def get_random_event(self):
        random_index = random.randint(0, len(self._events_list)-1)
        random_event = self._events_list[random_index]
        return random_event
    
    def event_action(self, event):
        if event == "":
            print('empty room')
            return ''
        if event == "enemy":
            # turn fight mode
            print("BOOOOOOOO")
            return "enemy"
            
            # end fight mode
        if event == "npc":
            # create npc
            # npc can talk, give somthing or make a deal
            print("HELLO FRIEND")
            return "npc"
            
        if event == "treasure":
            # treasure give some loot
            # it's chance for apear some monster or other adventurer
            print("MY PRESSIOUS")
            return "treasure"