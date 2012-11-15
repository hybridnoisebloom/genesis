class Quest:
    def __init__(self, desc="", name=""):
        self.description = desc
        self.name = name
        self.active = False
        self.complete = False
    
    def set_description(self, desc):
        self.description = desc
        
    def set_name(self, name):
        self.name = name
        
    def notify(self):
        print "A new quest is awaiting you: "+self.name
        
    def make_active(self, po):
        po.active_quest = self
