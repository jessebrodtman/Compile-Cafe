from cmu_graphics import *
import math
import copy
from customers import *
from tickets import *
from orders import *
from scenes import *

# regular
#TODO: orange
#? blue
#! red
#* green

#TODO: make customers appear gradually
#TODO: make orders work: draw at start, send from one station to next, trash anytime
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
    app.dayNumber = 1
    app.availableCodeItems = []
    app.availableCompileLevels = []
    app.availableNameItems = []
    
    #TODO: make more names, sizes, and styles
    app.fileNames = ['Henry', 'Billy', 'Joe']
    app.fileSizes = ['big file', 'medium file', 'small file']
    app.fileStyles = ['Light Mode', 'Dark Mode', 'Hotdog']
    
    startNewDay(app, app.dayNumber)

def startNewDay(app, dayNumber):
    app.sceneNumber = 0
    app.sceneName = getSceneName(app.sceneNumber)
    
    app.nameList = ['Ray', 'Liv', 'Avi', 'Amalia', 'Anna', 'Emily', 'Gleb', 'Hanson', 'Maerah', 'Peter', 'Rubie', 'Rong', 'Samuel', 'Sheng', 'Sonya', 'Teadora', 'Theo']
    
    #TODO: make different options available by day
    if dayNumber == 1:
        app.availableCodeItems = ['If', 'Else', 'Elif', 'List']
        app.availableCompileLevels = [2, 3]
        app.availableNameItems = ['Name']
    elif dayNumber == 2:
        app.availableCodeItems.extend(['Set','For Loop'])
        app.availableCompileLevels.extend([4])
        app.availableNameItems.extend(['File Size'])
    elif dayNumber == 3:
        app.availableCodeItems.extend(['Dict', 'While Loop'])
        app.availableCompileLevels.extend([1, 5])
        app.availableNameItems.extend(['Style'])
        
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

def main():
    runApp()

main()