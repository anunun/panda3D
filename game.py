from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager(self)  # Передаємо об'єкт ShowBase до Mapmanager
        self.camLens.setFov(90)  # Встановлюємо поле огляду камери
        # self.land.addBlock((0, 0, 0))
        self.land.loadLand("land.txt")
        self.hero = Hero((x,y,z),self.land)

game = Game()
game.run()