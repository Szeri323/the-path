
class Path:
    def __init__(self, length, event):
        self._length = length
        self._events_on_path = self._create_path(event)
        self._player_position = 0
        self.__event = event
    
    def _create_path(self, event):
        path = []
        path.append('')
        for i in range(1,self._length):
            path.append(event.get_random_event())
        return path
    
    def show_path(self):
        print(self._events_on_path)
        
    def move_player(self):
        print("player walk 1")
        self._player_position += 1
        return self.__event.event_action(self._events_on_path[self._player_position])