from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero
from direct.gui.DirectGui import DirectButton, DirectLabel, DirectFrame
from panda3d.core import TransparencyAttrib
import sys
from random import randint

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager(self)  # Передаємо об'єкт ShowBase до Mapmanager
        self.camLens.setFov(90)  # Встановлюємо поле огляду камери
        self.land.loadLand("land.txt")
        self.hero = Hero((10,1,1),self.land)
        self.land.textureon =False
        self.previous_num=None

        self.ui_visible = True
        self.bg_frame = DirectFrame(image='BG.png',scale=(1.35, 1, 1), sortOrder=0)
        self.SinglePlayer=DirectFrame(image='singleplayer.png',scale=(0.8, 1, 0.07), sortOrder=4,pos=(0, 0, -0.3))
        self.Options=DirectFrame(image='options.png',scale=(0.4, 1, 0.07), sortOrder=4,pos=(-0.397, 0, -0.45))
        self.Quit_Game=DirectFrame(image='Quit_Game.png',scale=(0.4, 1, 0.07), sortOrder=4,pos=(0.4, 0, -0.45))
        self.MinecraftText=DirectFrame(image='minecraft_title.png',scale=(0.9, 1, 0.15), sortOrder=5,pos=(0, 0, 0.8))
        self.MinecraftText.setTransparency(TransparencyAttrib.MAlpha)

        self.SinglePlayer_button = DirectButton(scale=(8, 1, 0.7), pos=(0, 0, -0.3), command=self.toggle_ui, sortOrder=3, frameColor=(1, 1, 1, 1))
        self.options_button = DirectButton(scale=(4, 1, 0.7), pos=(-0.397, 0, -0.45), command=self.options,sortOrder=3, frameColor=(1, 1, 1, 1))
        self.exit_button = DirectButton(scale=(4, 1, 0.7), pos=(0.4, 0, -0.45), command=self.exit_game,sortOrder=3, frameColor=(1, 1, 1, 1))
    def exit_game(self):
        sys.exit()

    def toggle_ui(self):
        if self.ui_visible:    
            self.bg_frame.hide()
            self.SinglePlayer_button.hide()
            self.SinglePlayer.hide()
            self.MinecraftText.hide()
            self.Options.hide()
            self.options_button.hide()
            self.exit_button.hide()
            self.Quit_Game.hide()
            self.hotbar=DirectFrame(image='Hotbar.png',scale=(1, 1, 0.12), sortOrder=4,pos=(0, 0, -0.87))
    def options(self):
        num = randint(1, 5)  
        while num == self.previous_num:
            num = randint(1, 5)

        self.previous_num = num 
        # num=randint(3,3)
        self.Options.hide()
        self.options_button.hide()
        if num==1:
            pos_num=(-0.8, 0, 0.4)
        elif num==2:
            pos_num=(0.6, 0, -0.8)
        elif num==3:
            pos_num=(-0.5, 0, 0)
        elif num==4:
            pos_num=(0.7, 0, 0.4)
        elif num==5:
            pos_num=(-0.6, 0, -0.7)
        self.options_button = DirectButton(scale=(4, 1, 0.7), pos=(pos_num), command=self.options,sortOrder=3, frameColor=(1, 1, 1, 1))
        self.Options=DirectFrame(image='options.png',scale=(0.4, 1, 0.07), sortOrder=4,pos=(pos_num))


game = Game()
game.run()