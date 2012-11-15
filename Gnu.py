import random

class Gnu:
    def __init__(self):
        self.health = 40
        self.x = None
        self.y = None
        self.z = None
        
    def move(self):
        if self.x != 1:
            self.x += randint(0, 1)
    	else:
            self.x += randint(-1, 0)
        
        if self.y != 1:
            self.y += randint(0, 1)
        else:
            self.y += randint(-1, 0)
    
    def check_spawn(self, po, spawn_rate):
        if po.day % spawn_rate == 0:
            self.x = randint(-1, 1)
            self.y = randint(-1, 1)
            self.z = randint(-6, 6)
        if self.x == po.x and self.y == po.y and self.z == po.z:
            self.check_spawn(po, spawn_rate)
        else:
            pass
        
    def on_attack(self, po, inv):
        if self.health == 0:
            self.on_death(self, inv)
        else:
            if random.randint(1,3) == 2:
                print "The Gnu rammed you."
                po.health -= random.randint(1,25)
            else:
                print "The Gnu kicked you."
                po.health -= random.randint(1,10)
    
    def on_death(self, inv):
        print "The Gnu dropped some Gnu Fur."
        inv.drops_load(1, random.randint(1, 4))
        
