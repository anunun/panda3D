from direct.showbase.ShowBase import ShowBase

class Mapmanager():
    def __init__(self, base):
        self.base = base
        self.model = 'block.egg'  # Модель кубика
        self.texture = 'stone.png'  # Текстура кубика
        self.color = (0.2, 0.2, 0.35, 1)  # RGBA колір
        self.land = self.base.render.attachNewNode("Land")  # Створення вузла для "землі"
        self.colors = [(0.5, 0.3, 0.0, 1),
                       (0.2, 0.2, 0.3, 1),
                       (0.5, 0.5, 0.2, 1),
                       (0.0, 0.6, 0.0, 1)]

    def addBlock(self, position):
        # Завантаження моделі та текстури
        self.block = self.base.loader.loadModel(self.model)  # Використовуємо self.base.loader
        self.block.setTexture(self.base.loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.reparentTo(self.land)
        self.color = self.getColor(position[2])
        self.block.setColor(self.color)
        # self.block.setScale((4,4,4))
        # Додаємо блок до "землі"

    def startNew(self):
        # Скидання або оновлення "землі"
        self.land.removeNode()
        self.land = self.base.render.attachNewNode("Land")

    def clear(self):
        self.land.removeNode()
        self.startNew()
    
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
    
    def getColor(self, z):
        if z < len(self.colors):
            return self.colors[z]
        else:
            return self.colors[len(self.colors) - 1]