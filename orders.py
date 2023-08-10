from cmu_graphics import *
import time

class Order:
    def __init__(self):
        self.codeItems = []
        self.compileLevel = 0
        self.nameItems = dict()
        self.startTime = 0
        self.creationTime = time.time()
    
    def startTimer(self):
        self.startTime = time.time()
        
    def updateCompileLevel(self):
        timeElapsed = time.time()-self.startTime
        self.compileLevel = int(timeElapsed//5)
    
    def drawOrder(self):
        x = app.width//2 - 120
        y = app.height//2 - 140
        width = 190
        height = 240
        drawRect(x, y, width, height, fill='white')
        
        lines = str(self).splitlines()
        for i in range(len(lines)):
            line = lines[i]
            drawLabel(line, x+width/2, y-5+width/5+i*width//6, size=width//10)
        
    def addCodeItem(self, item):
        self.codeItems.append(item)
    
    def increaseCompileLevel(self):
        self.compileLevel += 1
    
    def updateNameItems(self, num):
        if num == 0:
            #update name
            currentName = self.nameItems.get('Name',None)
            if currentName == None:
                self.nameItems['Name'] = app.fileNames[0]
            elif currentName == app.fileNames[-1]:
                self.nameItems.pop('Name')
            else:
                index = app.fileNames.index(currentName)
                self.nameItems['Name'] = app.fileNames[index+1]
            
        elif num == 1:
            #update file size
            currentSize = self.nameItems.get('Size',None)
            if currentSize == None:
                self.nameItems['Size'] = app.fileSizes[0]
            elif currentSize == app.fileSizes[-1]:
                self.nameItems.pop('Size')
            else:
                index = app.fileSizes.index(currentSize)
                self.nameItems['Size'] = app.fileSizes[index+1]
        elif num == 2:
            #update style
            currentStyle = self.nameItems.get('Style',None)
            if currentStyle == None:
                self.nameItems['Style'] = app.fileStyles[0]
            elif currentStyle == app.fileStyles[-1]:
                self.nameItems.pop('Style')
            else:
                index = app.fileStyles.index(currentStyle)
                self.nameItems['Style'] = app.fileStyles[index+1]
    
    def __eq__(self, other):
        if not isinstance(other, Order): return False
        return self.items == other.items
    
    def __repr__(self):
        s = f"""Order with items:"""
        for item in self.codeItems:
            s += '\n'+item

        s += f'\nCompile Level: {self.compileLevel}'
        
        for key in self.nameItems:
            s += f'\n{key}: {self.nameItems[key]}'
        return s
    
    def __hash__(self):
        return hash(str(self))