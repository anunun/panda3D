from direct.showbase.ShowBase import ShowBase
from numpy import block
import pickle

class Mapmanager():
    def __init__(self, base):
        self.textureon = True
        self.base = base
        self.model = 'block.egg'  # Модель кубика
        self.texture = ['grass.png', 'stone.png', 'wood.png',
                        'coblestone.png','sand.png','andesite.png',
                        'dirt.png','granite.png','deepslate.png','gravel.png']  # Текстура кубика
        self.settexture = self.texture[1]
        self.color = (0.2, 0.2, 0.35, 1)  # RGBA колір
        self.land = self.base.render.attachNewNode("Land")  # Створення вузла для "землі"

    def SetTexture(self,number):
        self.settexture = self.texture[number]

    def addBlock(self, position):
        # Завантаження моделі та текстури
        self.block = self.base.loader.loadModel(self.model)  # Використовуємо self.base.loader
        self.text = self.getTexture(position[2])
        self.block.setTexture(self.base.loader.loadTexture(self.text))
        self.block.setHpr(0, 0, 90)
        self.block.setPos(position)
        self.block.reparentTo(self.land)
        # self.color = self.getColor(position[2])
        # self.block.setColor(self.color)
        self.block.setTag("at",str(position))
    def findBlocks(self,pos):
        return self.land.findAllMatches("=at=" +str(pos))
    def findHE(self,pos):
        x,y,z = pos
        z=1
        while not self.isEmpty((x,y,z)):
            z +=1
        return(x,y,z)
    def delBlock(self,position):
        blocks=self.findBlocks(position)
        for block in blocks:
            block.removeNode()
    def buildBlock(self,pos):
        x,y,z = pos
        new = self.findHE(pos)
        if new[2] <=z+1:
            self.addBlock(new)
    def saveMap(self):
        blocks=self.land.getChildren()
        with open('my_map.dat','wb') as fout:
            pickle.dump(len(blocks),fout)
            for block in blocks:
                x,y,z=block.getPos()
                pos = (int(x),int(y),int(z))
                pickle.dump(pos,fout)
    def loadMap(self):
        self.clear()
        with open('my_map.dat','rb') as fin:
            lenght = pickle.load(fin)
            for i in range(lenght):
                pos = pickle.load(fin)
                self.addBlock(pos)
    
    def delBlockFrom(self,pos):
        x,y,z = pos
        pos = x,y,z-1
        blocks=self.findBlocks(pos)
        for block in blocks:
            block.removeNode()
        

    def startNew(self):
        # Скидання або оновлення "землі"
        self.land.removeNode()
        self.land = self.base.render.attachNewNode("Land")

    def clear(self):
        self.land.removeNode()
        self.startNew()
    def isEmpty(self,pos):
        blocks = self.findBlocks(pos)
        if blocks:
            return False
        else:
            return True
    
    def loadLand(self, filename):
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in line:
                    for z0 in range(int(z)):
                        block = self.addBlock((x, y, z0))
                    x += 1
                y += 1
    
    # def getColor(self, z):
    #     if z < len(self.colors):
    #         return self.colors[z]
    #     else:
    #         return self.colors[len(self.colors) - 1]
    def getTexture(self,z):
        if self.textureon:    
            if z < 1:
                return self.texture[0]
            else:
                return self.texture[1]
        else:
            return self.settexture
        