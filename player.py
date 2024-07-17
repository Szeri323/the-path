class Player:
    def __init__(self):
        self._health = 10
        self._atack_damage = 5
        self._backpack = []
        self._equipement = {
            "head": "",
            "torso": "",
            "left_hand": "",
            "right_hand": "",
            "left_leg": "",
            "right_leg": "",
        }
    
    def show_map(self, path):
        # Take path list, make dictionary and set X on the active field
        pass
    
    def walk(self, path):
        # Position in Palyer or Path class?
        return path.move_player()
    
    def is_alive(self):
        if self._health <= 0:
            return False
        return True
    
    def attack(self, target):
        target.take_damage(self._atack_damage)
    
    def take_damage(self, damage):
        self._health -= damage
        if self._health <= 0:
            print("player is daed")