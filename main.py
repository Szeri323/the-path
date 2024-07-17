from enemy import Enemy
from event import Event
from path import Path
from player import Player
  
def main():
    print("How long The Path should be?")
    length = int(input())
    event = Event()
    path = Path(length, event)
    path.show_path()
    player = Player()
    
    #player's move
    print("You woke up in empty room")
    for i in range(length-1):
        print(f'------ Level: {i+1} ------')
        event_action = player.walk(path)
        if event_action == "":
            print("Nothing's there")
            continue
        elif event_action == "enemy":
            enemy = Enemy()
            while player.is_alive() or enemy.is_alive():
                player.attack(enemy)
                enemy.attack(player)
            print("encounter enemy")
        elif event_action == "npc":
            print("encounter npc")
        elif event_action == "treasure":
            print("encounter trasure")

if __name__ == "__main__":
    main()