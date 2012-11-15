from random import randint

class Cow:
    def __init__(self):
        self.health = 20
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
        if self.health != 0:
            print "MOO."
        else:
            self.on_death(inv)
            
    def on_death(self, inv):
        print "The Cow dropped some Steak."
        inv.drops_load(2, random.randint(1, 4))
        inv.drops_load(4, random.randint(1, 4))
