from BlockLoader import BlockLoader

class Player:
    def __init__(self, inventory, name, quest):
        self.name = name
        self.health = 100
        self.equipped = "Fists"
        self.x = 0
        self.y = 0
        self.z = 0
        self.ax = None
        self.ay = None
        self.dimension = "Base"
        self.day = 0
        self.loader = BlockLoader()
        self.inv = inventory
        self.active_quest = quest
        if self.name == 'kvatchdebug':
            self.inv.item_add(9)
            self.inv.load_special(1)
            self.inv.load_special(2)
            self.inv.load_special(3)
            self.inv.load_special(4)

    def die(self, days):
        # Executed on death.
        print("You have died.")
        print("You lasted "+str(days)+" days.")
        exit(0)
    
    def attack(self, thing):
        if self.equipped == "Fists":
            thing.health -= randint(1,10)
        elif self.equipped == "L1":
            thing.health -= randint(10,25)
        elif self.equipped == "L2":
            thing.health -= randint(30,45)
        elif self.equipped == "L3":
            thing.health -= randint(50, 75)
        elif self.equipped == "L4":
            thing.health -= randint(75, 100)
        elif self.equipped == "L5":
            thing.health -= 100
        elif self.equipped == "L6":
            thing.health -= randint(100, 130)
        elif self.equipped == "L7":
            thing.health -= randint(100, 150)
        else:
            exit(001, "An Equipment Error was raised. Sorry for the inconvenience. Perhaps you'd like to report the bug to cm.computer.official@gmail.com?")
        thing.on_attack(self, self.inv)
            
    def move(self, direction):
        if direction == "LEFT":
            if self.x != -1:
                self.x -= 1
                self.loader.load_next(self.inv, self)
            else:
                print("You can't go any farther.")
        elif direction == "RIGHT":
            if self.x != 1:
                self.x += 1
                self.loader.load_next(self.inv, self)
            else:
                print("You can't go any farther.")
        elif direction == "FORWARD":
            if self.y != 1:
                self.y += 1
                self.loader.load_next(self.inv, self)
            else:
                print("You can't go any farther.")
        elif direction == "BACKWARD":
            if self.y != -1:
                self.y -= 1
                self.loader.load_next(self.inv, self)
            else:
                print("You can't go any farther.")
        elif direction == "UP":
            if self.z != 6:
                self.z += 1
                self.loader.load_next(self.inv, self)
            else:
                print("You can't go any farther.")
        elif direction == "DOWN":
            if self.z != -6:
                self.z -= 1
                self.loader.load_next(self.inv, self)
            else:
                print("You can't go any farther.")
        else:
            print("Whoops, the movement got whacked. You may want to report this to cm.computer.official@gmail.com.")
    
    def move_hell(self, direction):
        if direction == "LEFT":
            if self.x != -1:
                self.x -= 1
                self.loader.load_next_hell(self.inv, self)
            else:
                print("You can't go any farther.")
        elif direction == "RIGHT":
            if self.x != 1:
                self.x += 1
                self.loader.load_next_hell(self.inv, self)
            else:
                print("You can't go any farther.")
        elif direction == "FORWARD":
            if self.y != 1:
                self.y += 1
                self.loader.load_next_hell(self.inv, self)
            else:
                print("You can't go any farther.")
        elif direction == "BACKWARD":
            if self.y != -1:
                self.y -= 1
                self.loader.load_next_hell(self.inv, self)
            else:
                print("You can't go any farther.")
        elif direction == "UP":
            if self.z != 0:
                self.z += 1
                self.loader.load_next_hell(self.inv, self)
            else:
                print("You can't go any farther.")
        elif direction == "DOWN":
            if self.z != -9:
                self.z -= 1
                self.loader.load_next_hell(self.inv, self)
            else:
                print("You can't go any farther.")
        else:
            print("Whoops, the movement got whacked. You may want to report this to cm.computer.official@gmail.com.")
    
    def move_sd(self, direction):
        if direction == "LEFT":
            if self.x != -1:
                self.x -= 1
                self.loader.load_next_sd(self.inv, self)
            else:
                print("You can't go any farther.")
        elif direction == "RIGHT":
            if self.x != 1:
                self.x += 1
                self.loader.load_next_sd(self.inv, self)
            else:
                print("You can't go any farther.")
        elif direction == "FORWARD":
            if self.y != 1:
                self.y += 1
                self.loader.load_next_sd(self.inv, self)
            else:
                print("You can't go any farther.")
        elif direction == "BACKWARD":
            if self.y != -1:
                self.y -= 1
                self.loader.load_next_sd(self.inv, self)
            else:
                print("You can't go any farther.")
        elif direction == "UP":
            if self.z != 7:
                self.z += 1
                self.loader.load_next_sd(self.inv, self)
            else:
                print("You can't go any farther.")
        elif direction == "DOWN":
            if self.z != 0:
                self.z -= 1
                self.loader.load_next_sd(self.inv, self)
            else:
                print("You can't go any farther.")
        else:
            print("Whoops, the movement got whacked. You may want to report this to cm.computer.official@gmail.com.")
            
    def equip(self, stuff):
        if stuff == "bow":
            if self.inv.bow != self.inv.NOT_HAD:
                self.equipped = "L1"
            else:
                print("You can't equip that which you don't have.")
        elif stuff == "dagger":
            if self.inv.dagger != self.inv.NOT_HAD:
                self.equipped = "L1"
            else:
                print("You can't equip that which you don't have.")
        elif stuff == "crossbow":
            if self.inv.crossbow != self.inv.NOT_HAD:
                self.equipped = "L2"
            else:
                print("You can't equip that which you don't have.")
        elif stuff == "sword":
            if self.inv.sword != self.inv.NOT_HAD:
                self.equipped = "L2"
            else:
                print("You can't equip that which you don't have.")
        elif stuff == "cloudsword":
            if self.inv.cloudsword != self.inv.NOT_HAD:
                self.equipped = "L5"
            else:
                print("You can't equip that which you don't have.")
        elif stuff == "mace":
            if self.inv.daemonsheart != self.inv.NOT_HAD:
                self.equipped = "L7"
            else:
                print("You can't equip that which you don't have.")
        else:
            exit(001, "An Equipment Error was raised. Sorry for the inconvenience. Perhaps you'd like to report the bug to cm.computer.official@gmail.com?")
