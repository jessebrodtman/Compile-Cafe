from cmu_graphics import *

class Ticket:
    ticketId = 1
    
    def __init__(self, items):
        #! items is a list of items to include in order
        self.items = items
        self.id = Ticket.ticketId
        Ticket.ticketId += 1
        
    def drawTicket(self, x, y, width, height):
        drawRect(x, y, width, height, fill='white')
        
        lines = str(self).splitlines()
        for i in range(len(lines)):
            line = lines[i]
            drawLabel(line, x+width/2, y+width/5+i*width//6, size=width//7)
    
    def __eq__(self, other):
        if not isinstance(other, ticket): return False
        return self.id == other.id
    
    def __repr__(self):
        s = f"""Ticket #{self.id}:"""
        for item in self.items:
            s += '\n'+item
        return s
    
    def __hash__(self):
        return hash(self.id)
