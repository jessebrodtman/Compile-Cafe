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
    drawRect(25,130,60,60,fill='white')
    drawLabel('Press to make', 55, 145, size=9)
    drawLabel('new order!', 55, 160, size=9)
    
    drawRect(25,210,60,60,fill='white')
    drawLabel('Press to trash', 55, 225, size=9)
    drawLabel('current order!', 55, 240, size=9)
    
    drawRect(25,290,60,60,fill='white')
    drawLabel('Press to move', 55, 305, size=9)
    drawLabel('current order!', 55, 320, size=9)
    
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