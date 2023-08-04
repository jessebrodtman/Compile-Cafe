from cmu_graphics import *
import math
import copy
from customers import *
from tickets import *
from orders import *
from scenes import *
import time

# regular
#TODO: orange
#? blue
#! red
#* green

#TODO: make customers appear gradually
#TODO: give order to ticket and score
def checkSceneSwitch(app, mouseX, mouseY):
    #check if in right vertical space
    if app.height-75<=mouseY<=app.height-25:
        #check if in a box
        for i in range(5):
            if 62.5+i*100<=mouseX<=137.5+i*100:
                app.sceneNumber = i
                app.sceneName = getSceneName(i)
                return

def onAppStart(app):
    #TODO: figure out adaptive width and height
    app.width = 600
    app.height = 600
    app.dayNumber = 3
    app.availableCodeItems = []
    app.availableCompileLevels = []
    app.availableNameItems = []
    
    #TODO: make more names, sizes, and styles
    app.fileNames = ['Henry', 'Billy', 'Joe']
    app.fileSizes = ['big file', 'medium file', 'small file']
    app.fileStyles = ['Light Mode', 'Dark Mode', 'Hotdog']
    
    #TODO: figure out scoring system and display
    app.score = 0
    
    startNewDay(app, app.dayNumber)

def onStep(app):
    if app.width != 600:
        app.width = 600
    if app.height != 600:
        app.height = 600
    
    for order in app.activeOrders[2]:
        order.updateCompileLevel()
    
def startNewDay(app, dayNumber):
    app.sceneNumber = 0
    app.sceneName = getSceneName(app.sceneNumber)
    
    app.nameList = ['Ray', 'Liv', 'Avi', 'Amalia', 'Anna', 'Emily', 'Gleb', 'Hanson', 'Maerah', 'Peter', 'Rubie', 'Rong', 'Samuel', 'Sheng', 'Sonya', 'Teadora', 'Theo']
    app.activeOrders = {1: [], 2: [], 3: [], 4: []}
    
    if dayNumber == 1:
        app.availableCodeItems = ['If', 'Elif', 'Else', 'List']
        app.availableCompileLevels = [2, 3]
        app.availableNameItems = ['Name']
    elif dayNumber == 2:
        app.availableCodeItems = ['If', 'Elif', 'Else', 'List', 'For Loop','While Loop']
        app.availableCompileLevels = [2, 3, 4]
        app.availableNameItems = ['Name', 'File Size']
    elif dayNumber >= 3:
        app.availableCodeItems = ['If', 'Elif', 'Else', 'List', 'For Loop','While Loop', 'Set', 'Dict']
        app.availableCompileLevels = [1, 2, 3, 4, 5]
        app.availableNameItems = ['Name', 'File Size', 'Style']
        
    app.customerList = createCustomers(app)
    app.activeTicket = None

def makeRandomCustomer(app):
    ticket = makeRandomTicket(app)
    name = getRandomName(app)
    customer = Customer(name, ticket)
    return customer

def makeRandomTicket(app):
    if app.dayNumber<=3:
        numberCodeItems = 2
        numberNameItems = 1
    elif app.dayNumber<=5:
        numberCodeItems = 3
        numberNameItems = 2
    else:
        numberCodeItems = 4
        numberNameItems = 3

    codeList = copy.copy(app.availableCodeItems)
    
    #remove random elements until we have the right number of items
    for i in range(len(codeList)-numberCodeItems):
        randomIndex = randrange(0, len(codeList))
        codeList.pop(randomIndex)
    
    nameList = copy.copy(app.availableNameItems)
    for i in range(len(nameList)-numberNameItems):
        randomIndex = randrange(0, len(nameList))
        nameList.pop(randomIndex)
    #make the names a dict
    nameDict = dict()
    for option in nameList:
        if option == 'Name':
            index = randrange(0, len(app.fileNames))
            nameDict['Name'] = app.fileNames[index]
        elif option == 'File Size':
            index = randrange(0, len(app.fileSizes))
            nameDict['File Size'] = app.fileSizes[index]
        elif option == 'Style':
            index = randrange(0, len(app.fileStyles))
            nameDict['Style'] = app.fileStyles[index]
    
    compileLevel = app.availableCompileLevels[randrange(0,len(app.availableCompileLevels))]
        
    ticket = Ticket(codeList, compileLevel, nameDict)
    return ticket

def getRandomName(app):
    randomIndex = randrange(0,len(app.nameList))
    name = app.nameList.pop(randomIndex)
    return name

def createCustomers(app):
    customers = []
    if app.dayNumber <=5:
        numberCustomers = 5
    else:
        numberCustomers = 5 + math.ceil((dayNumber-5)/2)
    
    for i in range(numberCustomers):
        newCustomer = makeRandomCustomer(app)
        customers.append(newCustomer)
    
    return customers

def redrawAll(app):
    #draw background and title
    drawScene(app, app.sceneNumber)
        
    #draw buttons
    drawSceneButtons(app)
    
    #draw active ticket section
    drawRect(app.width-140,20,130,170, fill='black')
    
    #draw tickets
    for i in range(len(app.customerList)):
        customer = app.customerList[i]
        ticket = customer.ticket
        if i == app.activeTicket:
            ticket.drawTicket(480, 40, 90, 130)
        else:
            ticket.drawTicket(25+80*i, 25, 60, 90)
    
def onKeyPress(app, key):
    if key.isnumeric():
        app.activeTicket = int(key)-1

def onMousePress(app, mouseX, mouseY):
    #check if switching scenes
    checkSceneSwitch(app, mouseX, mouseY)
    
    #check buttons based on active scene
    if app.sceneNumber == 0:
        pass
    elif app.sceneNumber == 1:
        #pressed new order button
        if(25<=mouseX<=85 and 130<=mouseY<=190):
            app.activeOrders[1].append(Order())
        if len(app.activeOrders[1])>0:
            #pressed trash order button
            if(25<=mouseX<=85 and 210<=mouseY<=270):
                app.activeOrders[1].pop(0)
            #pressed move order button
            elif(25<=mouseX<=85 and 290<=mouseY<=350):
                app.activeOrders[1][0].startTimer()
                app.activeOrders[2].append(app.activeOrders[1].pop(0))
            #check first column of buttons
            elif(420<=mouseX<=480):
                for i in range(4):
                    if (220+50*i<=mouseY<=260+50*i):
                        currItem = app.availableCodeItems[i]
                        app.activeOrders[1][0].addCodeItem(currItem)
            #check second column of buttons
            elif(500<=mouseX<=560):
                numAvailableCodeItems = len(app.availableCodeItems)
                for i in range(4,numAvailableCodeItems):
                    if (220+50*(i-4)<=mouseY<=260+50*(i-4)):
                        currItem = app.availableCodeItems[i]
                        app.activeOrders[1][0].addCodeItem(currItem)       
    elif app.sceneNumber == 2:
        if len(app.activeOrders[2])>0:
            #pressed trash order button
            if(25<=mouseX<=85 and 210<=mouseY<=270):
                app.activeOrders[2].pop(0)
            #pressed move order button
            elif(25<=mouseX<=85 and 290<=mouseY<=350):
                app.activeOrders[2][0].updateCompileLevel()
                app.activeOrders[3].append(app.activeOrders[2].pop(0))
    elif app.sceneNumber == 3:
        if len(app.activeOrders[3])>0:
            #pressed trash order button
            if(25<=mouseX<=85 and 210<=mouseY<=270):
                    app.activeOrders[3].pop(0)
            #pressed move order button
            elif(25<=mouseX<=85 and 290<=mouseY<=350):
                pass
                #TODO: make function to evaluate order
    elif app.sceneNumber == 4:
        pass

def main():
    runApp()

main()