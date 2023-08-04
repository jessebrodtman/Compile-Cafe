from cmu_graphics import *
#! draw scenes 

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

def drawCompiling(app):
    drawRect(0,0,app.width,app.height,fill='lightGreen')

def drawNaming(app):
    drawRect(0,0,app.width,app.height,fill='lightCoral')

def drawEval(app):
    drawRect(0,0,app.width,app.height,fill='pink')

def drawSceneButtons(app):
    #TODO: make buttons pretty
    drawRect(0,app.height-100,app.width,100,fill='lightSlateGray')
    for i in range(5):
        drawRect(62.5+i*100,app.height-75,75,50,fill='dodgerBlue')
        drawLabel(getSceneName(i),100+i*100,app.height-50,bold=True)