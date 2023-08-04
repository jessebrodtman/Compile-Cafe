from cmu_graphics import *
from orders import *

#! draw scenes 
#TODO: make backgrounds for each scene
#TODO: make buttons pretty for each scene

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
        drawLobby(app)
    elif sceneNumber == 1:
        #draw coding
        drawCoding(app)
    elif sceneNumber == 2:
        #draw compiling
        drawCompiling(app)
    elif sceneNumber == 3:
        #draw naming
        drawNaming(app)
    elif sceneNumber == 4:
        #draw evaluating
        drawEval(app)
    
    #? draw label until scenes are done
    drawLabel(f'Active Scene: {app.sceneName}', app.width/2, app.height-150, bold=True, border='white', borderWidth=1, size=25)
    
def drawLobby(app):
    drawRect(0,0,app.width,app.height,fill='lightGray')

def drawCoding(app):
    drawRect(0,0,app.width,app.height,fill='lightBlue')
    #make buttons
    #new order
    drawRect(25,130,60,60,fill='white')
    drawLabel('Press to make', 55, 150, size=9)
    drawLabel('new order!', 55, 165, size=9)
    #trash order
    drawRect(25,210,60,60,fill='white')
    drawLabel('Press to trash', 55, 230, size=9)
    drawLabel('current order!', 55, 245, size=9)
    #move order
    drawRect(25,290,60,60,fill='white')
    drawLabel('Press to move', 55, 310, size=9)
    drawLabel('current order!', 55, 325, size=9)
    #TODO: make items grayed out until they're open
    #TODO: print with a loop
    #make first column of buttons
    for i in range(4):
        currItem = app.availableCodeItems[i]
        drawRect(420,220+50*i,60,40,fill='white')
        drawLabel(currItem, 450, 240+50*i, size=11)
    #make second column of buttons
    numAvailableCodeItems = len(app.availableCodeItems)
    for i in range(4,numAvailableCodeItems):
        currItem = app.availableCodeItems[i]
        drawRect(500,220+50*(i-4),60,40,fill='white')
        drawLabel(currItem, 530, 240+50*(i-4), size=11)
    #gray out remaining buttons
    for i in range(numAvailableCodeItems,8):
        drawRect(500,220+50*(i-4),60,40,fill='gray')
        drawLabel('Coming Soon!', 530, 240+50*(i-4), size=9)
    # drawRect(420,220,60,40,fill='white')
    # drawLabel('If', 450, 240, size=12)
    # drawRect(420,270,60,40,fill='white')
    # drawLabel('Elif', 450, 290, size=12)
    # drawRect(420,320,60,40,fill='white')
    # drawLabel('Else', 450, 340, size=12)
    # drawRect(420,370,60,40,fill='white')
    # drawLabel('List', 450, 390, size=12)
    # drawRect(500,220,60,40,fill='white')
    # drawLabel('For Loop', 530, 240, size=11)
    # drawRect(500,270,60,40,fill='white')
    # drawLabel('While Loop', 530, 290, size=11)
    # drawRect(500,320,60,40,fill='white')
    # drawLabel('Set', 530, 340, size=12)
    # drawRect(500,370,60,40,fill='white')
    # drawLabel('Dict', 530, 390, size=12)
    
    #display active order
    if app.activeOrders[1] != []:
        activeOrder = app.activeOrders[1][0]
        activeOrder.drawOrder()

def drawCompiling(app):
    drawRect(0,0,app.width,app.height,fill='lightGreen')
    
    #draw buttons
    drawRect(25,210,60,60,fill='white')
    drawLabel('Press to trash', 55, 225, size=9)
    drawLabel('current order!', 55, 240, size=9)
    
    drawRect(25,290,60,60,fill='white')
    drawLabel('Press to move', 55, 305, size=9)
    drawLabel('current order!', 55, 320, size=9)
    
    #display active order
    if app.activeOrders[2] != []:
        activeOrder = app.activeOrders[2][0]
        activeOrder.drawOrder()

def drawNaming(app):
    drawRect(0,0,app.width,app.height,fill='lightCoral')
    
    #draw buttons
    drawRect(25,210,60,60,fill='white')
    drawLabel('Press to trash', 55, 225, size=9)
    drawLabel('current order!', 55, 240, size=9)
    
    drawRect(25,290,60,60,fill='white')
    drawLabel('Press to move', 55, 305, size=9)
    drawLabel('current order!', 55, 320, size=9)
    
    #display active order
    if app.activeOrders[3] != []:
        activeOrder = app.activeOrders[3][0]
        activeOrder.drawOrder()

def drawEval(app):
    drawRect(0,0,app.width,app.height,fill='pink')

def drawSceneButtons(app):
    #TODO: make buttons pretty
    drawRect(0,app.height-100,app.width,100,fill='lightSlateGray')
    for i in range(5):
        drawRect(62.5+i*100,app.height-75,75,50,fill='dodgerBlue')
        drawLabel(getSceneName(i),100+i*100,app.height-50,bold=True)