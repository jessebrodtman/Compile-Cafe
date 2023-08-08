from cmu_graphics import *

class Ticket:
    ticketId = 0
    
    def __init__(self, codeItems, compileLevel, nameItems):
        self.codeItems = codeItems
        self.compileLevel = compileLevel
        self.nameItems = nameItems
        self.id = Ticket.ticketId
        Ticket.ticketId += 1
        
    def drawTicket(self, x, y, width, height):
        drawRect(x, y, width, height, fill='white')
        
        lines = str(self).splitlines()
        for i in range(len(lines)):
            line = lines[i]
            drawLabel(line, x+width/2, y+width/5+i*width//6, size=width//9)
    
    def __eq__(self, other):
        if not isinstance(other, ticket): return False
        return self.id == other.id
    
    def __repr__(self):
        s = f"""Ticket #{self.id+1}:"""
        for item in self.codeItems:
            s += '\n'+item
        
        s += f'\n Compile Level: {self.compileLevel}'
        
        for key in self.nameItems:
            s += f'\n{key}: {self.nameItems[key]}'
        return s
    
    def __hash__(self):
        return hash(self.id)
