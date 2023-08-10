from cmu_graphics import *
from orders import *

#draw all the scenes 
def getSceneName(sceneNumber):
    if sceneNumber == -2:
        return 'instructions'
    if sceneNumber == -1:
        return 'title'
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
    if sceneNumber == -2:
        #draw instructions
        drawInstructions(app)
    elif sceneNumber == -1:
        #draw title
        drawTitle(app)
    elif sceneNumber == 0:
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

def drawGuide(app, num):
    #add all the guided messages
    messages = ['''Welcome to the Coderia!\nPress anywhere to start''',
                ('At any time, you can use the left/right arrows\nto go to the' 
                +' next or previous instruction\nTry it now and go to the '
                +'next instruction!'),
                ('This is the lobby!\nHere you will see all your customers for'
                +' the day!\nYou can also see your tickets to the right.\n'
                +'You can make a ticket big by pressing\n the number key. '
                +"Try it!\nPress 1 to see Ray's ticket"),
                ('Now that you can see all the requirements,\ngo to the coding'
                ' screen by\npressing the button below'),
                ('Welcome to the coding screen!\nHere you will add your first'
                 +' ingredients!\nStart by making a new order\nwith the button'
                 +' on the left'),
                ('Ray wants an if statement!\nClick the if button to add it'
                 +' to the order'),
                ('She also wants an elif statement!\n'
                 +'Click the elif button to add it!'),
                ('Now that all the code items are added,\nMove to the compile'
                 +' menu by pressing\nthe move current order button'),
                ('Welcome to the compile menu!\nHere you will prepare your '
                 +'code\nThe compile level will go up automatically.'
                 +'\n(go to the next instruction)'),
                ('Once the desired level has been reached,\nmove the order'
                 ' to the naming stage!\nBe careful not to move it too'
                 +' early or too late!'),
                ('Welcome to the naming stage!\nHere you will add the final'
                 +' touches!\nClick the rename order button to\ncycle through'
                 +' names.'),
                ('When everything looks right, move the order'
                 +'\nto get scored!'),
                ('Welcome to the scoring menu!\nHere you can see how you did on'
                 +' the last order.\nWhen you are ready, go back to the lobby'),
                ("Welcome back!\nPress 2 to see James' order."),
                ('When you are ready, make his order'
                 +'\nto complete the tutorial!'),
                ('Once this order is served, you will\nstart out at day 1! As '
                 +'you play,\nnew ingredients will unlock,\nmore customers'
                 +' will come,\nand orders will get more complicated!')]
    num = max(0,num)
    num = min(num, len(messages)-1)
    drawRect(180,20,270,130,fill='white')
    
    numLines = len(messages[num].splitlines())
    distancePer = 20
    for i in range(numLines):
        line = messages[num].splitlines()[i]
        drawLabel(line, 315, 138/2-(numLines//2-i-1)*distancePer)

def drawInstructions(app):
    drawRect(0,0,app.width,app.height,fill='black')
    
    drawLabel("Papa's",app.width/2,90,fill='white',size=50, bold=True)  
    drawLabel("Coderia",app.width/2,150,fill='white',size=50, bold=True)  
    drawRect(75,400,150,100,fill='lightgray')
    drawLabel('Title Page',150,450,size=20)
    drawRect(375,400,150,100,fill='lightgray')
    drawLabel('Start Game',450,450,size=20)
    
    drawLabel('Your mission is to serve your customers!',
              300,210,size=16,fill='white')
    drawLabel('You must take customers orders and',
              300,230,size=16,fill='white')
    drawLabel('create their desired program.',300,250,size=16,fill='white')
    drawLabel('Serve every customer to pass the day!',
              300,270,size=16,fill='white')
    drawLabel('But be careful, if you mess up an',300,290,size=16,fill='white')
    drawLabel("order, it's game OVER :(",300,310,size=16,fill='white')

def drawTitle(app):
    drawRect(0,0,app.width,app.height,fill='black')
    drawLabel("Papa's",app.width/2,90,fill='white',size=50, bold=True)  
    drawLabel("Coderia",app.width/2,150,fill='white',size=50, bold=True)  
    drawRect(75,400,150,100,fill='lightgray')
    drawLabel('Instructions',150,450,size=20)
    drawRect(375,400,150,100,fill='lightgray')
    drawLabel('Start Game',450,450,size=20)
    drawLabel('Welcome!',app.width/2,250,fill='white',size=35,bold=True)
    drawLabel('Press the Buttons',app.width/2,285,fill='white',
              size=35,bold=True)
    drawLabel('To Get Started!',app.width/2,320,fill='white',size=35,bold=True)
    
def drawLobby(app):
    drawRect(0,0,app.width,app.height,fill='lightGray')
    
    for i in range(len(app.customerList)):
        customer = app.customerList[i]
        customer.drawPicture(50+100*i,225,85)
        drawLabel(customer.name,92.5+100*i,323,size=15,bold=True)

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
    #trash order
    drawRect(25,210,60,60,fill='white')
    drawLabel('Press to trash', 55, 225, size=9)
    drawLabel('current order!', 55, 240, size=9)
    #move order
    drawRect(25,290,60,60,fill='white')
    drawLabel('Press to move', 55, 305, size=9)
    drawLabel('current order!', 55, 320, size=9)
    
    buttonText = ['Rename Order', 'Change File Size', 'Change Style']
    for i in range(len(app.availableNameItems)):
        drawRect(420, 220+70*i,140,50,fill='white')
        drawLabel(buttonText[i],490,245+70*i,size=17)
    for i in range(len(app.availableNameItems),3):
        drawRect(420, 220+70*i,140,50,fill='gray')
        drawLabel('Coming Soon!',490,245+70*i,size=17)
    
    #display active order
    if app.activeOrders[3] != []:
        activeOrder = app.activeOrders[3][0]
        activeOrder.drawOrder()

def drawEval(app):
    drawRect(0,0,app.width,app.height,fill='pink')
    if app.activeOrders[4] != None:
        customer, order = app.activeOrders[4]
        order.drawOrder()
        customer.drawPicture(400,225,150)
        drawLabel(f'{customer.name} has been served!',450,410,size=20,bold=True)
        
        scoreNames = ['Time Score:', 'Coding Score:', 'Compiling Score:', 
                      'Naming Score:', 'Total Score:']
        for i in range(5):
            currScore = customer.scores[i]
            drawRect(62.5+i*100,app.height-165,75,50,fill='dodgerBlue')
            drawLabel(scoreNames[i],100+i*100,app.height-149,bold=True, size=9)
            drawLabel(currScore,100+i*100,app.height-133,bold=True)

def drawSceneButtons(app):
    drawRect(0,app.height-100,app.width,100,fill='lightSlateGray')
    for i in range(5):
        drawRect(62.5+i*100,app.height-75,75,50,fill='dodgerBlue')
        drawLabel(getSceneName(i),100+i*100,app.height-50,bold=True)