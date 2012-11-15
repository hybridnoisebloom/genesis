import sys

class QuestBoard:
    def __init__(self):
        self.quests = []
        
    def clear_screen(self):
        if sys.platform.startswith("win32") or sys.platform.startswith("os2"):
            system("cls")
        else:
            sys.stdout.write('\033[2J')
            sys.stdout.write('\033[H')
            sys.stdout.flush()
    
    def add_quest(self, quest):
        self.quests.append(quest)
        
    def describe_quest(self, questnum):
        print self.quests[questnum].description
        
    def remove_quest(self, questnum):
        self.quests.pop(questnum)
        
    def display_board(self):
        self.clear_screen()
        print "QUEST BOARD"
        for i in range(0, len(self.quests)-1):
            tmp = self.quests[i]
            print tmp.name
        print "1 - Choose a Quest"
        print "2 - Exit"
        temp = str(raw_input(">"))
        if temp == "1":
            self.choose_quest()
        else:
            pass
            
    def choose_quest(self):
        print "Choose a quest by number."
        self.quests[ int( raw_input(">") )-1 ].active = True
