from Interface import Interface
from random import randint
from time import sleep
import sys

class Lucifer:
    def __init__(self):
        self.health = 100
        self.tui = Interface()
        self.defeated = False
        
    def clear_screen(self):
        if sys.platform.startswith("win32") or sys.platform.startswith("os2"):
            system("cls")
        else:
            sys.stdout.write('\033[2J')
            sys.stdout.write('\033[H')
            sys.stdout.flush()
    
    def on_attack(self, po):
        print "The Morning Star regenerated some health!"
        self.health += randint(1, 15)
        print "Satan attacked you!"
        po.health -= randint(25, 50)
        
    def on_death(self, inv):
        inv.load_special(2)
        self.defeated = True
    
    def boss_fight(self, po, inv):
        self.clear_screen()
        po.ay = -1
        po.ax = 0
        while True:
            if self.health <= 0:
                print "You defeated Satan himself!"
                self.on_death(inv)
            else:
                pass
            
            if po.health <= 0:
                po.die("negative infinity")
            else:
                pass
            
            self.clear_screen()
            print "Lucifer Health: "+str(self.health)
            print "Player Health:"+str(po.health)
            self.tui.load_arena_graphics(po, bossrepr="%")
            temp = raw_input("> ")
            if temp == "move left" or temp == "left" or temp == "dig left":
                if po.ax != -1:
                    po.ax -= 1
                else:
                    print "There's nowhere left to run!"
            elif temp == "move right" or temp == "right" or temp == "dig right":
                if po.ax != 1:
                    po.ax += 1
                else:
                    print "There's nowhere left to run!"
            elif temp == "move forward" or temp == "forward" or temp == "dig forward":
                if po.ay != 1:
                    if po.ax == 0 and po.ay == 0:
                        print "You can't ram the boss."
                    else:
                        po.ay += 1
                else:
                    print "There's nowhere left to run!"
            elif temp == "move backward" or temp == "backward" or temp == "dig backward":
                if po.ay != -1:
                    po.ay -= 1
                else:
                    print "There's nowhere left to run!"
            elif temp == "attack":
                po.attack(self, po.inv)
            else:
                print "Unrecognized command!"
            sleep(3)
