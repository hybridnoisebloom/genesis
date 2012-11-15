# Inventory.py controls the inventory of the player.

class Inventory:
    def __init__(self):
        self.wood = 10
        self.stone = 0
        self.iron = 0
        self.silver = 0
        self.gold = 0
        self.diamond = 0
        self.novarock = 0
        self.obsidian = 0
        self.adamantium = 0
        self.unobtainium = 0
        self.involatilium = 0
        self.gunpowder = 0
        self.hellrock = 0
        self.cloudrock = 0
        self.snow = 0
		
        self.bow = 0
        self.dagger = 0
        self.crossbow = 0
        self.sword = 0
        self.magifier = 0
        
        self.hellporterpartone = 0
        self.hellporterparttwo = 0
        self.hellporterpartthree = 0
        self.hell_teleporter = 0
        
        self.skykeypartone = 0
        self.skykeyparttwo = 0
        self.skykeypartthree = 0
        self.skydim_key = 0
		
        self.gnufur = 0
        self.leather = 0
        self.zombiemeat = 0
        self.steak = 0
        self.gruefur = 0
        
        self.cloudsword = 0
        self.daemonsheart = 0
        
        self.UNMAGIC_HAD = 1
        self.MAGIC_HAD = 2
        self.PORTER_HAD = 1
        self.NOT_HAD = 0
        
    def drops_load(self, block_val, amount):
        if block_val == 1:
            self.gnufur += 1
        elif block_val == 2:
            self.leather += 1
        elif block_val == 3:
            self.zombiemeat += 1
        elif block_val == 4:
            self.steak += 1
        elif block_val == 5:
            self.gruefur += 1
    
    def load(self, block_val, amount):
        if block_val == 1:
            self.stone += amount
        elif block_val == 2:
            self.iron += amount
        elif block_val == 3:
            self.silver += amount
        elif block_val == 4:
            self.gold += amount
        elif block_val == 5:
            self.diamond += amount
        elif block_val == 6:
            self.novarock += amount
        elif block_val == 7:
            self.obsidian += amount
        elif block_val == 8:
            self.adamantium += amount
        elif block_val == 9:
            self.unobtainium += amount
        elif block_val == 10:
            self.involatilium += amount
        else:
            return None
    
    def load_hell(self, data_val, amount):
        if data_val == 1:
            self.hellrock += amount
        elif data_val == 2:
            self.obsidian += amount
        elif data_val == 3:
            self.stone += amount
        else:
            return None
    
    def load_sd(self, data_val, amount):
        if data_val == 1:
            self.snow += amount
        elif data_val == 2:
            self.cloudrock += amount
        elif data_val == 3:
            self.stone += amount
        else:
            return None
    
    def porter_load_one(self, block_val, amount):
        if block_val == 1:
            self.obsidian += amount
        elif block_val == 2:
            self.adamantium += amount
        elif block_val == 3:
            self.unobtainium += amount
        elif block_val == 4:
            self.involatilium += amount
        elif block_val == 5:
            self.hellporterpartone = self.UNMAGIC_HAD
        elif block_val == 6:
            self.hellporterparttwo = self.UNMAGIC_HAD
        elif block_val == 7:
            self.hellporterpartthree = self.UNMAGIC_HAD
        else:
            return None
            
    def porter_load_two(self, block_val, amount):
        if block_val == 1:
            self.obsidian += amount
        elif block_val == 2:
            self.adamantium += amount
        elif block_val == 3:
            self.unobtainium += amount
        elif block_val == 4:
            self.involatilium += amount
        elif block_val == 5:
            self.skykeypartone = self.UNMAGIC_HAD
        elif block_val == 6:
            self.skykeyparttwo = self.UNMAGIC_HAD
        elif block_val == 7:
            self.skykeypartthree = self.UNMAGIC_HAD
        else:
            return None

    def item_add(self, item_val):
        if item_val == 1:
            self.bow = self.UNMAGIC_HAD
        elif item_val == 2:
            self.dagger = self.UNMAGIC_HAD
        elif item_val == 3:
            self.crossbow = self.UNMAGIC_HAD
        elif item_val == 4:
            self.sword = self.UNMAGIC_HAD
        elif item_val == 5:
            self.bow = self.MAGIC_HAD
        elif item_val == 6:
            self.dagger = self.MAGIC_HAD
        elif item_val == 7:
            self.crossbow = self.MAGIC_HAD
        elif item_val == 8:
            self.sword = self.MAGIC_HAD
        elif item_val == 9:
            self.magifier = 1
            
    def load_special(self, item_code):
        if item_code == 1:
            self.cloudsword = 1
        elif item_code == 2:
            self.daemonsheart = 1
        elif item_code == 3:
            self.hell_teleporter = 1
        elif item_code == 4:
            self.skydim_key = 1
        else:
            pass
	        
    def magify(self, thing):
        if thing == "dagger" and self.dagger == self.UNMAGIC_HAD:
            self.dagger = self.MAGIC_HAD
        elif thing == "bow" and self.bow == self.UNMAGIC_HAD:
            self.bow = self.MAGIC_HAD
        elif thing == "sword" and self.sword == self.UNMAGIC_HAD:
            self.sword = self.MAGIC_HAD
        elif thing == "crossbow" and self.crossbow == self.UNMAGIC_HAD:
            self.crossbow = self.MAGIC_HAD
    
    def list_inv(self):
        print "NATURAL MATERIALS:"
        print "Wood:\t"+str(self.wood)
        print "Stone:\t"+str(self.stone)
        print "Iron:\t"+str(self.iron)
        print "Silver:\t"+str(self.silver)
        print "Gold:\t"+str(self.gold)
        print "Diamond:\t"+str(self.diamond)
        print "NovaRock:\t"+str(self.novarock)
        print "Snow:\t"+str(self.snow)
        print "\n"
        print "Hellrock:\t"+str(self.hellrock)
        print "Cloudrock:\t"+str(self.cloudrock)
        print "TELEPORTERS:"
        if self.hell_teleporter == self.NOT_HAD:
            pass
        elif self.hell_teleporter == self.UNMAGIC_HAD:
            print "Hell Teleporter\tTeleports to Hell"
        else:
            print "Something bad happened."
        
        if self.skydim_key == self.NOT_HAD:
            pass
        elif self.skydim_key == self.UNMAGIC_HAD:
            print "Sky Gate Key\tTeleports to Sky Dimension"
        else:
            print "Something bad happened."
        
        print "TOOLS AND WEAPONRY:"
        if self.bow == self.NOT_HAD:
            pass
        elif self.bow == self.UNMAGIC_HAD:
            print "Bow\tUnmagic Weapon, Tier 1"
        elif self.bow == self.MAGIC_HAD:
            print "Bow\tMagic Weapon, Tier 1"
        else:
            print "Whoops, an error occurred. Report it to cm.computer.official@gmail.com!"
        
        if self.dagger == self.NOT_HAD:
            pass
        elif self.dagger == self.UNMAGIC_HAD:
            print "Dagger\tUnmagic Weapon, Tier 1"
        elif self.dagger == self.MAGIC_HAD:
            print "Dagger\tMagic Weapon, Tier 1"
        else:
            print "Whoops, an error occurred. Report it to cm.computer.official@gmail.com!"
            
        if self.sword == self.NOT_HAD:
            pass
        elif self.sword == self.UNMAGIC_HAD:
            print "Sword\tUnmagic Weapon, Tier 2"
        elif self.bow == self.MAGIC_HAD:
            print "Sword\tMagic Weapon, Tier 2"
        else:
            print "Whoops, an error occurred. Report it to cm.computer.official@gmail.com!"
            
        if self.crossbow == self.NOT_HAD:
            pass
        elif self.crossbow == self.UNMAGIC_HAD:
            print "Crossbow\tUnmagic Weapon, Tier 2"
        elif self.bow == self.MAGIC_HAD:
            print "Crossbow\tMagic Weapon, Tier 2"
        else:
            print "Whoops, an error occurred. Report it to cm.computer.official@gmail.com!"
        
        if self.cloudsword == self.NOT_HAD:
            pass
        elif self.cloudsword == self.PORTER_HAD:
            print "The Dimensional Cloudsword\tMagic Weapon, Tier 5"
        else:
            print "WHOOPS."
        
        if self.daemonsheart == self.NOT_HAD:
            pass
        elif self.daemonsheart == self.PORTER_HAD:
            print "The Daemon's Heart Mace\tMagic Weapon, Tier 7"
        else:
            print "WHOOPS."
            
        return True
