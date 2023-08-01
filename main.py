from cmu_graphics import *
import math
import copy
from customers import *
from tickets import *

# regular
#TODO: orange
#? blue
#! red
#* green

#TODO: make customers appear gradually
def getSceneName(sceneNumber):
    if sceneNumber == 0:
        return 'lobby'
    elif sceneNumber == 1:
        return 'coding'
    elif sceneNumber == 2:
        return 'compiling'
    elif sceneNumber == 3:
        return 'naming'
    elif sceneNumber == 4:
        return 'evaluating'

def drawScene(app, sceneNumber):
    if sceneNumber == 0:
        #draw lobby
        drawRect(0,0,app.width,app.height,fill='lightGray')
    elif sceneNumber == 1:
        #draw coding
        drawRect(0,0,app.width,app.height,fill='lightBlue')
    elif sceneNumber == 2:
        #draw compiling
        drawRect(0,0,app.width,app.height,fill='lightGreen')
    elif sceneNumber == 3:
        #draw naming
        drawRect(0,0,app.width,app.height,fill='lightCoral')
    elif sceneNumber == 4:
        #draw evaluating
        drawRect(0,0,app.width,app.height,fill='pink')
    drawLabel(f'Active Scene: {app.sceneName}', app.width/2, app.height-150, bold=True, border='white', borderWidth=1, size=25)

def drawSceneButtons(app):
    #TODO: make buttons pretty
    drawRect(0,app.height-100,app.width,100,fill='lightSlateGray')
    for i in range(5):
        drawRect(62.5+i*100,app.height-75,75,50,fill='dodgerBlue')
        drawLabel(getSceneName(i),100+i*100,app.height-50,bold=True)

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
    #TODO: figure out width and height
    app.width = 600
    app.height = 600
    app.dayNumber = 1
    startNewDay(app, app.dayNumber)

def startNewDay(app, dayNumber):
    app.sceneNumber = 0
    app.sceneName = getSceneName(app.sceneNumber)
    
    app.nameList = ['Ray', 'Liv', 'Avi', 'Amalia', 'Anna', 'Emily', 'Gleb', 'Hanson', 'Maerah', 'Peter', 'Rubie', 'Rong', 'Samuel', 'Sheng', 'Sonya', 'Teadora', 'Theo']
    
    #TODO: make different options available by day
    app.availableItems = ['if statement', 'booleans', 'for loop', 'while loop', 'list', 'set', 'dictionary']
    
    app.customerList = createCustomers(app)
    app.activeTicket = None

def makeRandomCustomer(app):
    ticket = makeRandomTicket(app)
    name = getRandomName(app)
    customer = Customer(name, ticket)
    return customer

def makeRandomTicket(app):
    if app.dayNumber<=3:
        numberItems = 3
    elif app.dayNumber<=5:
        numberItems = 4
    else:
        numberItems = 5
    
    ingredientList = copy.copy(app.availableItems)
    for i in range(len(ingredientList)-numberItems):
        randomIndex = randrange(0, len(ingredientList))
        ingredientList.pop(randomIndex)
    
    ticket = Ticket(ingredientList)
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
print('hello')