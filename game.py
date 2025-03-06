from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero
from direct.gui.DirectGui import DirectButton, DirectLabel, DirectFrame
from panda3d.core import TransparencyAttrib

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager(self)  # Передаємо об'єкт ShowBase до Mapmanager
        self.camLens.setFov(90)  # Встановлюємо поле огляду камери
        self.land.loadLand("land.txt")
        self.hero = Hero((10,1,1),self.land)
        self.land.textureon =False

        self.ui_visible = True
        self.bg_frame = DirectFrame(image='BG.png',scale=(1.35, 1, 1), sortOrder=0)
        self.ButtonPhoto=DirectFrame(image='button.png',scale=(0.6, 1, 0.07), sortOrder=4,pos=(0, 0, -0.3))
        self.MinecraftText=DirectFrame(image='minecraft_title.png',scale=(0.9, 1, 0.15), sortOrder=5,pos=(0, 0, 0.8))
        self.MinecraftText.setTransparency(TransparencyAttrib.MAlpha)

        self.hide_button = DirectButton(scale=(6, 1, 0.7), pos=(0, 0, -0.3), command=self.toggle_ui, sortOrder=3, frameColor=(1, 1, 1, 1))

    def toggle_ui(self):
        if self.ui_visible:    
            self.bg_frame.hide()
            self.hide_button.hide()
            self.ButtonPhoto.hide()
            self.MinecraftText.hide()
            self.hotbar=DirectFrame(image='Hotbar.png',scale=(1, 1, 0.12), sortOrder=4,pos=(0, 0, -0.87))
    def options(self):
        pass


game = Game()
game.run()