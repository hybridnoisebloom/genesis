# BlockLoader.py loads the next block mined and gives it to you
from random import randint
from Inventory import Inventory

class BlockLoader:
    def load_next(self, inv, po):
        if po.z > -4 and po.z <= 5:
            inv.load(randint(1, 4), randint(1,3))
        elif po.z < -4:
            inv.load(randint(4, 10), randint(1, 3))
        elif po.z < -5:
            inv.porter_load_one(randint(1, 7), randint(1, 3))
        elif po.z > 5:
            inv.porter_load_two(randint(1, 7), randint(1, 3))
        else:
            return None
    
    def load_next_hell(self, inv, po):
        inv.load_hell(randint(1, 3), randint(1,3))
    
    def load_next_sd(self, inv, po):
        inv.load_sd(randint(1, 3), randint(1,3))
	
