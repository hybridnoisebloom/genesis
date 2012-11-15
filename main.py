# TODO: Multiplayer mode, port 127 
# TODO: Possible graphical frontend?

from Player import Player
from Cow import Cow
from Gnu import Gnu
from Zombie import Zombie
from Grue import Grue
from Kitty import Kitty

from Lucifer import Lucifer
from Skyking import SkyKing

from Inventory import Inventory
from Portal import Portal
from Interface import Interface
from BlockLoader import BlockLoader

from time import sleep
from random import randint
import sys

class Main:
    def __init__(self, name):
        self.inv = Inventory()
        self.dim = Portal()
        self.ui = Interface()
        self.loader = BlockLoader()
        
        self.no_quest = Quest(desc="No quest.", name="None")
        self.you = Player(self.inv, name, self.no_quest)
        self.mob1 = Cow()
        self.mob2 = Gnu()
        self.mob3 = Zombie()
        self.mob4 = Grue()
        self.mob5 = Kitty()
        
        self.no_quest = Quest(desc="No quest.", name="None")
        self.hell_quest = Quest(desc="Conquer Hell!", name="Crusader")
        self.sky_quest = Quest(desc="Conquer the Sky Dimension!", name="Hostile Heavenly Takeover")
        self.magic_quest = Quest(desc="Magify something.", name="We Don't Have to Explain It")
        self.
        
        self.sk = SkyKing()
        self.satan = Lucifer()
        
    def clear_screen(self):
        if sys.platform.startswith("win32") or sys.platform.startswith("os2"):
            system("cls")
        else:
            sys.stdout.write('\033[2J')
            sys.stdout.write('\033[H')
            sys.stdout.flush()
    
    def run(self):
        while True:
            self.you.day += 1
            sleep(1)
            self.clear_screen()
            
            if self.you.dimension == "Hell":
                self.run_hell()
            elif self.you.dimension == "Sky Dimension":
                self.run_sd()
            elif self.you.dimension == "Base":
                pass
            else:
                print "ERR"
            
            cowspawn = self.mob1.x == None and self.mob1.y == None and self.mob1.z == None
            zomspawn = self.mob3.x == None and self.mob3.y == None and self.mob3.z == None
            gruespawn = self.mob4.x == None and self.mob4.y == None and self.mob4.z == None
            kittyspawn = self.mob5.x == None and self.mob5.y == None and self.mob5.z == None
            if cowspawn and zomspawn and gruespawn and kittyspawn:
                self.ui.load_peaceful_graphics(self.you)
            elif cowspawn and not zomspawn and gruespawn and kittyspawn:
                self.ui.load_zombie_graphics(self.you, self.mob3)
            elif cowspawn and zomspawn and not gruespawn and kittyspawn:
                self.ui.load_grue_graphics(self.you, self.mob4)
            elif not cowspawn and zomspawn and gruespawn and kittyspawn:
                self.ui.load_cow_graphics(self.you, self.mob1)
            elif cowspawn and zomspawn and gruespawn and not kittyspawn:
                self.ui.load_kitty_graphics(self.you, self.mob5)
            else:
                pass
            
            if not zomspawn:
                zomcheck1 = abs(self.mob3.y) - abs(self.you.y) == 1 and abs(self.mob3.x) - abs(self.you.x) == 0
            else:
                zomcheck1 = False
            if not zomspawn:
                zomcheck2 = abs(self.mob3.x) - abs(self.you.x) == 1 and abs(self.mob3.y) - abs(self.you.y) == 0
            else:
                zomcheck2 = False
            if zomcheck1 or zomcheck2:
                self.you.attack(self.mob3, self.inv)
            else:
                pass
            if not gruespawn:
                gruecheck1 = abs(self.mob4.y) - abs(self.you.y) == 1 and abs(self.mob4.x) - abs(self.you.x) == 0
            else:
                gruecheck1 = False
            if not gruespawn:
                gruecheck2 = abs(self.mob4.x) - abs(self.you.x) == 1 and abs(self.mob4.y) - abs(self.you.y) == 0
            else:
                gruecheck2 = False
            if gruecheck1 or gruecheck2:
                self.you.attack(self.mob4, self.inv)
            else:
                pass
            if not cowspawn:
                cowcheck1 = abs(self.mob1.y) - abs(self.you.y) == 1 and abs(self.mob1.x) - abs(self.you.x) == 0
            else:
                cowcheck1 = False
            if not cowspawn:
                cowcheck2 = abs(self.mob1.x) - abs(self.you.x) == 1 and abs(self.mob1.y) - abs(self.you.y) == 0
            else:
                cowcheck2 = False
            if cowcheck1 or cowcheck2:
                self.you.attack(self.mob1, self.inv)
            else:
                pass
                
            if self.inv.hellporterpartone == 1 and self.inv.hellporterparttwo == 1 and self.inv.hellporterpartthree == 1:
                print "You have created the Hell Teleporter!"
                self.inv.hell_teleporter = 1
            else:
                pass
            
            if self.inv.skykeypartone == 1 and self.inv.skykeyparttwo == 1 and self.inv.skykeypartthree == 1:
                print "You have created the key to the Stairway to the Sky Dimension!"
                self.inv.sky_key = 1

            self.mob1.check_spawn(self.you, randint(10, 15))
            self.mob2.check_spawn(self.you, 35)
            self.mob3.check_spawn(self.you, randint(20, 40))
            self.mob4.check_spawn(self.you, randint(30, 45))
            self.mob5.check_spawn(self.you, randint(60,75))
            command = str(raw_input("> "))
            
            if command.startswith("dig "):
                self.you.move(command[4:].upper())
            elif command == "inventory":
                self.clear_screen()
                self.inv.list_inv()
                sleep(3)
                self.clear_screen()
            elif command == "inv":
                self.clear_screen()
                self.inv.list_inv()
                sleep(3)
            elif command == "craft bow":
                if self.inv.wood >= 3:
                    self.inv.bow = self.inv.UNMAGIC_HAD
                    self.you.equipped = "L1"
                else:
                    print "You don't have enough materials."
            elif command == "craft dagger":
                if self.inv.wood >= 3:
                    self.inv.dagger = self.inv.UNMAGIC_HAD
                    self.you.equipped = "L1"
                else:
                    print "You don't have enough materials."
            elif command == "craft sword":
                if self.inv.wood >= 1 and self.inv.iron >= 2:
                    self.inv.sword = self.inv.UNMAGIC_HAD
                    self.you.equipped = "L2"
                else:
                    print "You don't have enough materials."
            elif command == "craft crossbow":
                if self.inv.wood >= 2 and self.inv.iron >= 2:
                    self.inv.crossbow = self.inv.UNMAGIC_HAD
                    self.you.equipped = "L2"
                else:
                    print "You don't have enough materials."
            elif command == "craft magifier":
                if self.inv.iron >= 3 and self.inv.gold >= 4 and self.inv.unobtainium >= 2:
                    self.inv.magifier = self.inv.UNMAGIC_HAD
                    print "You created the Magifier! You can now magify weaponry with 3 involatilium and the magifier!"
                else:
                    print "You don't have enough materials."
            elif command.startswith("magify "):
                if self.inv.magifier == self.inv.UNMAGIC_HAD:
                    self.inv.magify(command[7:])
                else:
                    print "You don't have the Magifier."
            elif command.startswith("teleport "):
                if command[9:].lower() == "hell" and self.you.dimension != "Hell":
                    if self.inv.hell_teleporter == self.inv.UNMAGIC_HAD:
                        self.dim.teleport(self.you, "Hell")
                    else:
                        print "You can't teleport to Hell without the Teleporter!"
                elif command[9:].lower() == "sky" and self.you.dimension != "Sky":
                    if self.inv.skydim_key == self.inv.UNMAGIC_HAD:
                        self.dim.teleport(self.you, "Sky")
                    else:
                        print "You can't teleport to the Sky Dimension without the key to the stairway!"
                elif command[9:].lower() == "base" and self.you.dimension != "Base":
                    self.dim.teleport(self.you, "Sky")
                else:
                    print "Either that dimension doesn't exist or it has not been implemented yet."
            elif command == "exit":
                temp = raw_input("Do you really want to exit?\n>")
                if temp.lower() == "yes" or temp.lower() == "y":
                    exit("Goodbye, then.")
                else:
                    pass
            elif command == "quests":
                self.questboard.display_board()
            else:
                print "Unrecognized command."
                
    def run_hell(self):
        while True:
            sleep(1)
            self.clear_screen()
            
            if self.you.dimension == "Hell":
                pass
            elif self.you.dimension == "Sky Dimension":
                self.run_sd()
            elif self.you.dimension == "Base":
                self.run()
            else:
                print "ERR"
            
            self.ui.load_peaceful_graphics(self.you)
            
            command = str(raw_input("> "))
            if command.startswith("dig "):
                self.you.move_hell(command[4:].upper())
            elif command == "inventory":
                self.clear_screen()
                self.inv.list_inv()
                sleep(2)
                self.clear_screen()
            elif command == "inv":
                self.clear_screen()
                self.inv.list_inv()
                sleep(2)
            elif command == "fight boss" or command == "boss fight":
                self.satan.boss_fight(self.you, self.inv)
            elif command.startswith("craft "):
                print "You can't craft in Hell."
            elif command.startswith("magify "):
                if self.inv.magifier == self.inv.UNMAGIC_HAD:
                    self.inv.magify(command[7:])
                else:
                    print "You don't have the Magifier."
            elif command.startswith("teleport"):
                if command[9:].lower() == "base" and self.you.dimension != "Base":
                    self.dim.teleport(self.you, "Base")
                else:
                    print "You can't teleport anywhere other than back to the base dimension while in Hell."
            elif command == "exit":
                temp = raw_input("Do you really want to exit?\n>")
                if temp.lower() == "yes" or temp.lower() == "y":
                    exit("Goodbye, then.")
                else:
                    pass
            else:
                print "Unrecognized command."
                
    def run_sd(self):
        while True:
            sleep(1)
            self.clear_screen()
            
            if self.you.dimension == "Hell":
                self.run_hell()
            elif self.you.dimension == "Sky Dimension":
                pass
            elif self.you.dimension == "Base":
                self.run()
            else:
                print "ERR"
            
            if command.startswith("dig "):
                self.you.move_sd(command[4:].upper())
            elif command == "inventory":
                self.clear_screen()
                self.inv.list_inv()
                sleep(3)
                self.clear_screen()
            elif command == "inv":
                self.inv.list_inv()
            elif command == "boss fight":
                self.sk.boss_fight(self.you, self.inv)
            elif command.startswith("craft "):
                print "You can't craft in the Sky Dimension."
            elif command.startswith("magify "):
                if self.inv.magifier == self.inv.UNMAGIC_HAD:
                    self.inv.magify(command[7:])
                else:
                    print "You don't have the Magifier."
            elif command == "boss fight" or command == "fight boss":
                print "Are you /sure/ you want to fight the Sky King? (y|n)"
                tmp = raw_input("> ")
                if tmp.lower() == "y" or tmp.lower() == "yes":
                    sk.boss_fight(self.you, self.inv)
                else:
                    pass
            elif command.startswith("teleport"):
                if command[9:].lower() == "base" and self.you.dimension != "Base":
                    self.dim.teleport(self.you, "Base")
                else:
                    print "You can't teleport anywhere other than back to the base dimension while in the Sky Dimension."
            elif command == "exit":
                temp = raw_input("Do you really want to exit?\n>")
                if temp.lower() == "yes" or temp.lower() == "y":
                    exit("Goodbye, then.")
                else:
                    pass
            else:
                print "Unrecognized command."

class TitleScreen:
    def __init__(self):
        pass
    
    def clear_screen(self):
        if sys.platform.startswith("win32") or sys.platform.startswith("os2"):
            system("cls")
        else:
            sys.stdout.write('\033[2J')
            sys.stdout.write('\033[H')
            sys.stdout.flush()
	
    def display(self):
        self.clear_screen()
        print "Genesis Beta!"
        if randint(1,3) == 1:
            print "Finally beta!"
        elif randint(1,3) == 2:
            print "This is my boomstick!"
        elif randint(1,3) == 3:
            print "Free and open sauce!"
        else:
            print "How unfortunate, an error appeared on the title screen."
            open("debug.txt", 'a').write("Title screen error: couldn't display clever remark.\n")
        print "1 - Start Game"
        print "2 - Show Credits"
        print "3 - Show License"
        print "4 - Exit Game"
        choice = raw_input("> ")
        if choice == "1":
            self.run_game()
        elif choice == "2":
            self.show_credits()
        elif choice == "3":
            self.show_license()
        elif choice == "4":
            exit(0)
        else:
            self.display()
    
    def show_license(self):
        self.clear_screen()
        print "Genesis 0.8 is free and open source software trilicensed under the Mozilla Public License v2.0, the GNU General Public License v3.0, and the Simplified BSD License."
        sleep(5)
        self.clear_screen()
        self.display()
    
    def show_credits(self):
        self.clear_screen()
        print "Programmed by Draven \"dbro\" Stedman"
        print "Designed by Draven \"dbro\" Stedman and D.J. Courtney"
        print "---GENESIS BETA---"
        sleep(3)
        self.clear_screen()
        self.display()
    
    def run_game(self):
        self.clear_screen()
        sunombre = str(raw_input("Enter your name!\n>"))
        game = Main(sunombre)
        sleep(1)
        self.clear_screen()
        game.run()
        
class Debugger:
    def __init__(self):
        pass
    
    def get_debug_info(self):
        name = raw_input("Please enter your name (first and last): ")
        opsys = raw_input("Please enter the name of your operating system: ")
        print "Writing debug information to debug file..."
        tmp = open("debug.txt", 'a')
        tmp.write("Tester Name: "+name+"\n")
        tmp.write("Operating System: "+opsys+"\n")
        tmp.write("Genesis version is Beta 2\n")
        tmp.close()

class BetaKeyHandler:
    def __init__(self):
        self.keys = ['15744-CP', '64829AZ', '307953L', '421217N', '46458CW', '861463O', '31748F0', '391554G', '264245Q']
        self.debugger = De+bugger()
        self.ts = TitleScreen()

    def run(self):
        print "Welcome to the Beta Test of Genesis!"
        betakey = str(raw_input("Enter beta key: "))
        
        if betakey.upper() in self.keys:
            print "You have been authentificated."
            self.debugger.get_debug_info()
            self.ts.display()
        else:
            print "The given beta key is invalid."

starter = BetaKeyHandler()
if __name__ == "__main__":
    starter.run()
else:
    print "Module loaded."
