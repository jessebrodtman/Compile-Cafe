from cmu_graphics import *
import time
from tickets import *
from orders import *
from PIL import Image

class Customer:
    def __init__(self, name, ticket):
        self.name = name
        self.ticket = ticket
        self.served = False
    
    def drawPicture(self, x, y, size):
        picture = Image.open(f'C:\\Users\\jesse\\Desktop\\15-112\\Images\\{self.name}.jpeg')
        picture = CMUImage(picture)
        drawImage(picture,x,y,width=size,height=size)
    
    def getTicketNum(self):
        return self.ticket.id
    
    def __eq__(self, other):
        if not isinstance(other, Customer): return False
        return (self.name == other.name) and (self.ticket==other.ticket)
    
    def __repr__(self):
        return f'Customer(Name: {self.name}, Served: {self.served})'

    def __hash__(self):
        return hash(str(self))
    
    def evaluateTicket(self, order):
        '''
        time - 5 seconds per item
        15 point deduction for extra item
        15 point deduction for missing item
        10 point deduction for wrong order
        20 point deduction for wrong compile
        20 point deduction for wrong name item
        <60 means game over
        '''
        self.served = True
        
        timeTaken = time.time()-order.creationTime
        ticket = self.ticket
        
        numItems = len(ticket.codeItems)+len(ticket.nameItems)
        estimatedTime = numItems*5+ticket.compileLevel*5
        timeOver = max(0, timeTaken-estimatedTime)
        lobbyScore = 100-5*timeOver
        
        extraCodeItems = differenceInItems(order.codeItems, ticket.codeItems)
        missingCodeItems = differenceInItems(ticket.codeItems, order.codeItems)
        numCodeItemsWrong = wrongPlace(ticket.codeItems, order.codeItems)
        codingScore = 100-15*len(extraCodeItems)-15*len(missingCodeItems)-10*numCodeItemsWrong
                
        compileDiff = abs(order.compileLevel-ticket.compileLevel)
        compilingScore = 100-20*compileDiff
        
        numNameItemsWrong = 0
        nameItems = ['Name','Style','Size']
        for i in range(3):
            currItem = nameItems[i]
            if order.nameItems.get(currItem,None) != ticket.nameItems.get(currItem,None):
                numNameItemsWrong += 1
        namingScore = 100-20*numNameItemsWrong
        
        overallScore = (lobbyScore+codingScore+compilingScore+namingScore)//4
        self.scores = [lobbyScore, codingScore, compilingScore, namingScore, overallScore]
        
        app.score += overallScore
        
        if overallScore<70:
            return True
        return False
    
def differenceInItems(A, B):
    #return list of items in A but not in B
    L = []
    for item in A:
        if item not in B:
            L.append(item)
    return L

def wrongPlace(A, B):
    #return number of items in both A and B that are not in the same index
    num = 0
    index = 0
    while index<len(A) and index<len(B):
        item = A[index]
        if item in B and item!=B[index]:
            num += 1
        index += 1
    return num