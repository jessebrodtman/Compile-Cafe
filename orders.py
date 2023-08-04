from cmu_graphics import *

#TODO: track time
class Order:
    def __init__(self):
        self.codeItems = []
        self.compileLevel = 0
        self.nameItems = dict()
        
    def drawOrder(self):
        #TODO: make pretty
        x = app.width//2 - 120
        y = app.height//2 - 150
        width = 190
        height = 230
        drawRect(x, y, width, height, fill='white')
        
        lines = str(self).splitlines()
        for i in range(len(lines)):
            line = lines[i]
            drawLabel(line, x+width/2, y+width/5+i*width//6, size=width//10)
        
    def addCodeItem(self, item):
        self.codeItems.append(item)
    
    def increaseCompileLevel(self):
        self.compileLevel += 1
    
    def setNameItems(self, category, value):
        self.nameItems[category] = value
    
    def __eq__(self, other):
        if not isinstance(other, order): return False
        return self.items == other.items
    
    def __repr__(self):
        s = f"""Order with items:"""
        for item in self.codeItems:
            s += '\n'+item

        for key in self.nameItems:
            s += f'\n{key}: {self.nameItems[key]}'
        return s
    
    def __hash__(self):
        return hash(str(self))