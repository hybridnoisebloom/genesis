# Interface.py controls the interface.

class Interface:
    def load_peaceful_graphics( self, po ):
        if po.x == 0 and po.y == 0:
            print "###########"
            print "####   ####"
            print "#### @ ####"
            print "####   ####"
            print "###########"     
        elif po.x == 1 and po.y == 0:
            print "###########"
            print "####   ####"
            print "####  @####"
            print "####   ####"
            print "###########"
        elif po.x == -1 and po.y == 0:
            print "###########"
            print "####   ####"
            print "####@  ####"
            print "####   ####"
            print "###########"
        elif po.x == 0 and po.y == 1:
            print "###########"
            print "#### @ ####"
            print "####   ####"
            print "####   ####"
            print "###########"
        elif po.x == 1 and po.y == 1:
            print "###########"
            print "####  @####"
            print "####   ####"
            print "####   ####"
            print "###########"
        elif po.x == -1 and po.y == 1:
            print "###########"
            print "####@  ####"
            print "####   ####"
            print "####   ####"
            print "###########"
        elif po.x == 0 and po.y == -1:
            print "###########"
            print "####   ####"
            print "####   ####"
            print "#### @ ####"
            print "###########"
        elif po.x == 1 and po.y == -1:
            print "###########"
            print "####   ####"
            print "####   ####"
            print "####  @####"
            print "###########"
        elif po.x == -1 and po.y == -1:
            print "###########"
            print "####   ####"
            print "####   ####"
            print "####@  ####"
            print "###########"
        else:
            print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
        print "Name: "+str(po.name)
        print "X: "+str(po.x)+"\tY: "+str(po.y)+"\tZ: "+str(po.z)
        print "HP: "+str(po.health)+"\tDimension: "+po.dimension
        print "Active Quest: "+po.active_quest.name
        print "---GENESIS BETA---"

    def load_arena_graphics(self, po, bossrepr="b"):
        if po.ay == 1 and po.ax == 0:
            exit(1, msg="Graphics error.")
        else:
            if po.ay == 1:
                if po.ax == -1:
                    print "_____"
                    print "|@"+bossrepr+".|"
                    print "|...|"
                    print "|...|"
                    print "-----"
                elif po.ax == 1:
                    print "_____"
                    print "|."+bossrepr+"@|"
                    print "|...|"
                    print "|...|"
                    print "-----"
                else:
                    pass
            elif po.ay == 0:
                if po.ax == 0:
                    print "_____"
                    print "|."+bossrepr+".|"
                    print "|.@.|"
                    print "|...|"
                    print "-----"
                elif po.ax == 1:
                    print "_____"
                    print "|."+bossrepr+".|"
                    print "|..@|"
                    print "|...|"
                    print "-----"
                elif po.ax == -1:
                    print "_____"
                    print "|."+bossrepr+".|"
                    print "|@..|"
                    print "|...|"
                    print "-----"
                else:
                    pass
            elif po.ay == -1:
                if po.ax == 0:
                    print "_____"
                    print "|."+bossrepr+".|"
                    print "|...|"
                    print "|.@.|"
                    print "-----"
                elif po.ax == 1:
                    print "_____"
                    print "|."+bossrepr+".|"
                    print "|...|"
                    print "|..@|"
                    print "-----"
                elif po.ax == -1:
                    print "_____"
                    print "|."+bossrepr+".|"
                    print "|...|"
                    print "|@..|"
                    print "-----"
    def load_zombie_graphics(self, po, zom):
        if zom.z == po.z:
            if zom.x == 0 and zom.y == 0:
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "#### Z@####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####@Z ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == 1:
                    print "###########"
                    print "#### @ ####"
                    print "#### Z ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "#### Z ####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "#### Z ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "#### Z ####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "#### Z ####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "#### Z ####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif zom.x == 0 and zom.y == 1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "#### Z ####"
                    print "#### @ ####"
                    print "####   ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "#### Z ####"
                    print "####  @####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "#### Z ####"
                    print "####@  ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "#### Z@####"
                    print "####   ####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@Z ####"
                    print "####   ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "#### Z ####"
                    print "####   ####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "#### Z ####"
                    print "####   ####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "#### Z ####"
                    print "####   ####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif zom.x == 0 and zom.y == -1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "#### @ ####"
                    print "#### Z ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####  @####"
                    print "#### Z ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####@  ####"
                    print "#### Z ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "####   ####"
                    print "#### Z ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "####   ####"
                    print "#### Z ####"
                    print "###########"
                elif po.x == 0 and po.y == 1:
                    print "###########"
                    print "#### @ ####"
                    print "####   ####"
                    print "#### Z ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "#### Z@####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "####@Z ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif zom.x == 1 and zom.y == 0:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "#### @Z####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####@ Z####"
                    print "####   ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "####  Z####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "####  Z####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####  Z####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####  Z####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####  Z####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif zom.x == 1 and zom.y == 1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####  Z####"
                    print "#### @ ####"
                    print "####   ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####  Z####"
                    print "####  @####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####  Z####"
                    print "####@  ####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@ Z####"
                    print "####   ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####  Z####"
                    print "####   ####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####  Z####"
                    print "####   ####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####  Z####"
                    print "####   ####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif zom.x == 1 and zom.y == -1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "#### @ ####"
                    print "####  Z####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####  @####"
                    print "####  Z####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####@  ####"
                    print "####  Z####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "####   ####"
                    print "####  Z####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "####   ####"
                    print "####  Z####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "#### @Z####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "####@ Z####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif zom.x == -1 and zom.y == 0:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####Z@ ####"
                    print "####   ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####Z @####"
                    print "####   ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "####Z  ####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "####Z  ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####Z  ####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####Z  ####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####Z  ####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif zom.x == -1 and zom.y == 1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####Z  ####"
                    print "#### @ ####"
                    print "####   ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####Z  ####"
                    print "####  @####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####Z  ####"
                    print "####@  ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####Z @####"
                    print "####   ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####Z  ####"
                    print "####   ####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####Z  ####"
                    print "####   ####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####Z  ####"
                    print "####   ####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif zom.x == -1 and zom.y == -1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "#### @ ####"
                    print "####Z  ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####  @####"
                    print "####Z  ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####@  ####"
                    print "####Z  ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "####   ####"
                    print "####Z  ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "####   ####"
                    print "####Z  ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "####Z@ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "####Z @####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
                print "Name: "+str(po.name)
                print "X: "+str(po.x)+"\tY: "+str(po.y)+"\tZ: "+str(po.z)
                print "HP: "+str(po.health)+"\tDimension: "+po.dimension
                print "Active Quest: "+po.active_quest.name
                print "---GENESIS BETA---"
            else:
                self.load_peaceful_graphics(po)
        
    def load_cow_graphics(self, po, cow):
        if cow.z == po.z:
            if cow.x == 0 and cow.y == 0:
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "#### C@####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####@C ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == 1:
                    print "###########"
                    print "#### @ ####"
                    print "#### C ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "#### C ####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "#### C ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "#### C ####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "#### C ####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "#### C ####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif cow.x == 0 and cow.y == 1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "#### C ####"
                    print "#### @ ####"
                    print "####   ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "#### C ####"
                    print "####  @####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "#### C ####"
                    print "####@  ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "#### C@####"
                    print "####   ####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@C ####"
                    print "####   ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "#### C ####"
                    print "####   ####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "#### C ####"
                    print "####   ####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "#### C ####"
                    print "####   ####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif cow.x == 0 and cow.y == -1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "#### @ ####"
                    print "#### C ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####  @####"
                    print "#### C ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####@  ####"
                    print "#### C ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "####   ####"
                    print "#### C ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "####   ####"
                    print "#### C ####"
                    print "###########"
                elif po.x == 0 and po.y == 1:
                    print "###########"
                    print "#### @ ####"
                    print "####   ####"
                    print "#### C ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "#### C@####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "####@C ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif cow.x == 1 and cow.y == 0:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "#### @C####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####@ C####"
                    print "####   ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "####  C####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "####  C####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####  C####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####  C####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####  C####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif cow.x == 1 and cow.y == 1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####  C####"
                    print "#### @ ####"
                    print "####   ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####  C####"
                    print "####  @####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####  C####"
                    print "####@  ####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@ C####"
                    print "####   ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####  C####"
                    print "####   ####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####  C####"
                    print "####   ####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####  C####"
                    print "####   ####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif cow.x == 1 and cow.y == -1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "#### @ ####"
                    print "####  C####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####  @####"
                    print "####  C####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####@  ####"
                    print "####  C####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "####   ####"
                    print "####  C####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "####   ####"
                    print "####  C####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "#### @C####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "####@ C####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif cow.x == -1 and cow.y == 0:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####C@ ####"
                    print "####   ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####C @####"
                    print "####   ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "####C  ####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "####C  ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####C  ####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####C  ####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####C  ####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif cow.x == -1 and cow.y == 1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####C  ####"
                    print "#### @ ####"
                    print "####   ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####C  ####"
                    print "####  @####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####C  ####"
                    print "####@  ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####C @####"
                    print "####   ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####C  ####"
                    print "####   ####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####C  ####"
                    print "####   ####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####C  ####"
                    print "####   ####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif cow.x == -1 and cow.y == -1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "#### @ ####"
                    print "####C  ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####  @####"
                    print "####C  ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####@  ####"
                    print "####C  ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "####   ####"
                    print "####C  ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "####   ####"
                    print "####C  ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "####C@ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "####C @####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
                print "Name: "+str(po.name)
                print "X: "+str(po.x)+"\tY: "+str(po.y)+"\tZ: "+str(po.z)
                print "HP: "+str(po.health)+"\tDimension: "+po.dimension
                print "Active Quest: "+po.active_quest.name
                print "---GENESIS BETA---"
            else:
                self.load_peaceful_graphics(po)
        
    def load_grue_graphics(self, po, grue):
        if grue.z == po.z:
            if grue.x == 0 and grue.y == 0:
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "#### G@####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####@G ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == 1:
                    print "###########"
                    print "#### @ ####"
                    print "#### G ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "#### G ####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "#### G ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "#### G ####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "#### G ####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "#### G ####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif grue.x == 0 and grue.y == 1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "#### G ####"
                    print "#### @ ####"
                    print "####   ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "#### G ####"
                    print "####  @####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "#### G ####"
                    print "####@  ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "#### G@####"
                    print "####   ####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@G ####"
                    print "####   ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "#### G ####"
                    print "####   ####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "#### G ####"
                    print "####   ####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "#### G ####"
                    print "####   ####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif grue.x == 0 and grue.y == -1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "#### @ ####"
                    print "#### G ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####  @####"
                    print "#### G ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####@  ####"
                    print "#### G ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "####   ####"
                    print "#### G ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "####   ####"
                    print "#### G ####"
                    print "###########"
                elif po.x == 0 and po.y == 1:
                    print "###########"
                    print "#### @ ####"
                    print "####   ####"
                    print "#### G ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "#### G@####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "####@G ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif grue.x == 1 and grue.y == 0:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "#### @G####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####@ G####"
                    print "####   ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "####  G####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "####  G####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####  G####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####  G####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####  G####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif grue.x == 1 and grue.y == 1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####  G####"
                    print "#### @ ####"
                    print "####   ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####  G####"
                    print "####  @####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####  G####"
                    print "####@  ####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@ G####"
                    print "####   ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####  G####"
                    print "####   ####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####  G####"
                    print "####   ####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####  G####"
                    print "####   ####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif grue.x == 1 and grue.y == -1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "#### @ ####"
                    print "####  G####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####  @####"
                    print "####  G####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####@  ####"
                    print "####  G####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "####   ####"
                    print "####  G####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "####   ####"
                    print "####  G####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "#### @G####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "####@ G####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif grue.x == -1 and grue.y == 0:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####G@ ####"
                    print "####   ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####G @####"
                    print "####   ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "####G  ####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "####G  ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####G  ####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####G  ####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####G  ####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif grue.x == -1 and grue.y == 1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####G  ####"
                    print "#### @ ####"
                    print "####   ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####G  ####"
                    print "####  @####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####G  ####"
                    print "####@  ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####G @####"
                    print "####   ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####G  ####"
                    print "####   ####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####G  ####"
                    print "####   ####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####G  ####"
                    print "####   ####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif grue.x == -1 and grue.y == -1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "#### @ ####"
                    print "####G  ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####  @####"
                    print "####G  ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####@  ####"
                    print "####G  ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "####   ####"
                    print "####G  ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "####   ####"
                    print "####G  ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "####G@ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "####G @####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
                print "Name: "+str(po.name)
                print "X: "+str(po.x)+"\tY: "+str(po.y)+"\tZ: "+str(po.z)
                print "HP: "+str(po.health)+"\tDimension: "+po.dimension
                print "Active Quest: "+po.active_quest.name
                print "---GENESIS BETA---"
            else:
                self.load_peaceful_graphics(po)
    def load_gnu_graphics(self, po, gnu):
        if gnu.z == po.z:
            if gnu.x == 0 and gnu.y == 0:
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "#### Y@####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####@Y ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == 1:
                    print "###########"
                    print "#### @ ####"
                    print "#### Y ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "#### Y ####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "#### Y ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "#### Y ####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "#### Y ####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "#### Y ####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif gnu.x == 0 and gnu.y == 1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "#### Y ####"
                    print "#### @ ####"
                    print "####   ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "#### Y ####"
                    print "####  @####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "#### Y ####"
                    print "####@  ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "#### Y@####"
                    print "####   ####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@Y ####"
                    print "####   ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "#### Y ####"
                    print "####   ####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "#### Y ####"
                    print "####   ####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "#### Y ####"
                    print "####   ####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif gnu.x == 0 and gnu.y == -1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "#### @ ####"
                    print "#### Y ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####  @####"
                    print "#### Y ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####@  ####"
                    print "#### Y ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "####   ####"
                    print "#### Y ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "####   ####"
                    print "#### Y ####"
                    print "###########"
                elif po.x == 0 and po.y == 1:
                    print "###########"
                    print "#### @ ####"
                    print "####   ####"
                    print "#### Y ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "#### Y@####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "####@Y ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif gnu.x == 1 and gnu.y == 0:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "#### @Y####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####@ Y####"
                    print "####   ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "####  Y####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "####  Y####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####  Y####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####  Y####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####  Y####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif gnu.x == 1 and gnu.y == 1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####  Y####"
                    print "#### @ ####"
                    print "####   ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####  Y####"
                    print "####  @####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####  Y####"
                    print "####@  ####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@ Y####"
                    print "####   ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####  Y####"
                    print "####   ####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####  Y####"
                    print "####   ####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####  Y####"
                    print "####   ####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif gnu.x == 1 and gnu.y == -1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "#### @ ####"
                    print "####  Y####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####  @####"
                    print "####  Y####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####@  ####"
                    print "####  Y####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "####   ####"
                    print "####  Y####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "####   ####"
                    print "####  Y####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "#### @Y####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "####@ Y####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif gnu.x == -1 and gnu.y == 0:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####Y@ ####"
                    print "####   ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####Y @####"
                    print "####   ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "####Y  ####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "####Y  ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####Y  ####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####Y  ####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####Y  ####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif gnu.x == -1 and gnu.y == 1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####Y  ####"
                    print "#### @ ####"
                    print "####   ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####Y  ####"
                    print "####  @####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####Y  ####"
                    print "####@  ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####Y @####"
                    print "####   ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####Y  ####"
                    print "####   ####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####Y  ####"
                    print "####   ####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####Y  ####"
                    print "####   ####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif gnu.x == -1 and gnu.y == -1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "#### @ ####"
                    print "####Y  ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####  @####"
                    print "####Y  ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####@  ####"
                    print "####Y  ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "####   ####"
                    print "####Y  ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "####   ####"
                    print "####Y  ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "####Y@ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "####Y @####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
                print "Name: "+str(po.name)
                print "X: "+str(po.x)+"\tY: "+str(po.y)+"\tZ: "+str(po.z)
                print "HP: "+str(po.health)+"\tDimension: "+po.dimension
                print "Active Quest: "+po.active_quest.name
                print "---GENESIS BETA---"
            else:
                self.load_peaceful_graphics(po)
    
    def load_kitty_graphics(self, po, cat):
        if cat.z == po.z:
            if cat.x == 0 and cat.y == 0:
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "#### C@####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####@C ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == 1:
                    print "###########"
                    print "#### @ ####"
                    print "#### C ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "#### C ####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "#### C ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "#### C ####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "#### C ####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "#### C ####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif cat.x == 0 and cat.y == 1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "#### C ####"
                    print "#### @ ####"
                    print "####   ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "#### C ####"
                    print "####  @####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "#### C ####"
                    print "####@  ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "#### C@####"
                    print "####   ####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@C ####"
                    print "####   ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "#### C ####"
                    print "####   ####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "#### C ####"
                    print "####   ####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "#### C ####"
                    print "####   ####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif cat.x == 0 and cat.y == -1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "#### @ ####"
                    print "#### C ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####  @####"
                    print "#### C ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####@  ####"
                    print "#### C ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "####   ####"
                    print "#### C ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "####   ####"
                    print "#### C ####"
                    print "###########"
                elif po.x == 0 and po.y == 1:
                    print "###########"
                    print "#### @ ####"
                    print "####   ####"
                    print "#### C ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "#### C@####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "####@C ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif cat.x == 1 and cat.y == 0:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "#### @C####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####@ C####"
                    print "####   ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "####  C####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "####  C####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####  C####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####  C####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####  C####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif cat.x == 1 and cat.y == 1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####  C####"
                    print "#### @ ####"
                    print "####   ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####  C####"
                    print "####  @####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####  C####"
                    print "####@  ####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@ C####"
                    print "####   ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####  C####"
                    print "####   ####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####  C####"
                    print "####   ####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####  C####"
                    print "####   ####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif cat.x == 1 and cat.y == -1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "#### @ ####"
                    print "####  C####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####  @####"
                    print "####  C####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####@  ####"
                    print "####  C####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "####   ####"
                    print "####  C####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "####   ####"
                    print "####  C####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "#### @C####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "####@ C####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif cat.x == -1 and cat.y == 0:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####C@ ####"
                    print "####   ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####C @####"
                    print "####   ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "####C  ####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "####C  ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####C  ####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####C  ####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####C  ####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif cat.x == -1 and cat.y == 1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####C  ####"
                    print "#### @ ####"
                    print "####   ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####C  ####"
                    print "####  @####"
                    print "####   ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####C  ####"
                    print "####@  ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####C @####"
                    print "####   ####"
                    print "####   ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####C  ####"
                    print "####   ####"
                    print "#### @ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####C  ####"
                    print "####   ####"
                    print "####  @####"
                    print "###########"
                elif po.x == -1 and po.y == -1:
                    print "###########"
                    print "####C  ####"
                    print "####   ####"
                    print "####@  ####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
            elif cat.x == -1 and cat.y == -1:
                if po.x == 0 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "#### @ ####"
                    print "####C  ####"
                    print "###########"
                if po.x == 1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####  @####"
                    print "####C  ####"
                    print "###########"
                elif po.x == -1 and po.y == 0:
                    print "###########"
                    print "####   ####"
                    print "####@  ####"
                    print "####C  ####"
                    print "###########"
                elif po.x == 1 and po.y == 1:
                    print "###########"
                    print "####  @####"
                    print "####   ####"
                    print "####C  ####"
                    print "###########"
                elif po.x == -1 and po.y == 1:
                    print "###########"
                    print "####@  ####"
                    print "####   ####"
                    print "####C  ####"
                    print "###########"
                elif po.x == 0 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "####C@ ####"
                    print "###########"
                elif po.x == 1 and po.y == -1:
                    print "###########"
                    print "####   ####"
                    print "####   ####"
                    print "####C @####"
                    print "###########"
                else:
                    print "Whoops, the graphics didn't load! You may want to report this bug to cm.computer.official@gmail.com!"
                print "Name: "+str(po.name)
                print "X: "+str(po.x)+"\tY: "+str(po.y)+"\tZ: "+str(po.z)
                print "HP: "+str(po.health)+"\tDimension: "+po.dimension
                print "Active Quest: "+po.active_quest.name
                print "---GENESIS BETA---"
            else:
                self.load_peaceful_graphics(po)
