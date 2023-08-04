from cmu_graphics import *

class Order:
    def __init__(self):
        self.codeItems = []
        self.compileLevel = 0
        self.nameItems = dict()
        
    def addCodeItem(self, item):
        self.codeItems.append(item)
    
    def setCompileLevel(self, level):
        self.compileLevel = level
    
    def setNameItems(self, category, value):
        self.nameItems[category] = value
    
    def __eq__(self, other):
        if not isinstance(other, order): return False
        return self.items == other.items
    
    def __repr__(self):
        s = f"""Order with items: {self.items}"""
    
    def __hash__(self):
        return hash(str(self))