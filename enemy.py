class Enemy:
    def __init__(self):
        self._health = 2
        self._atack_damage = 1
        
    def is_alive(self):
        if self._health <= 0:
            return False
        return True
    
    def attack(self, target):
        target.take_damage(self._atack_damage)
    
    def take_damage(self, damage):
        self._health -= damage
        if self._health <= 0:
            print("enemy is daed")
            