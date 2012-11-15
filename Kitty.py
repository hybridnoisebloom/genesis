# The kitty is a pretty simple but rare passive mob. If you attack it, 
# there's a one in five chance it will scratch you.

from random import randint

class Kitty:
    def __init__(self):
        self.health = 37
        self.x = None
        self.y = None
        self.z = None
        
    def on_attack(self, po, inv):
        if self.health != 0:
            if randint(1,5) == 4:
                print "The cat hisses and scratches you."
                po.health -= randint(1,7)
            else:
                print "The cat hisses at you, angry that you just hit it."
        else:
            self.on_death()
        
    def on_death(self):
        print "You don't get anything from killing a cute little kitty, you monster!"
    
    def check_spawn(self, po, spawn_rate):
        if po.day % spawn_rate == 0:
            self.x = randint(-1, 1)
            self.y = randint(-1, 1)
            self.z = randint(-6, 6)
        if self.x == po.x and self.y == po.y and self.z == po.z:
            self.check_spawn(po, spawn_rate)
        else:
            pass
