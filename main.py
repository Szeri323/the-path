import random

class Event:
    def __init__(self):
        self.__events_list = ['ambush', 'npc', 'treasuer'] 
        
    def get_events_list(self):
        return self.__events_list
    
    def get_random_event(self):
        random_index = random.randint(0, len(self.__events_list)-1)
        print(random_index)
        return self.__events_list[random_index]

class Path:
    def __init__(self, length):
        self.__length = length
        self.path = self.create_path()
    
    def create_path(self):
        path = []
        event = Event()
        for i in range(self.__length):
            path.append(event.get_random_event())
        return path
    
    def show_path(self):
        print(self.path)
        
def main():
    print("How long The Path should be?")
    length = int(input())
    path = Path(length)
    path.show_path()

if __name__ == "__main__":
    main()