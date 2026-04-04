import pygame
import numpy as np
import os
import sys

class Theme:
    def __init__(self,name,game,players):
        if name=="medieval":
            self.timer=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Timer.png")).convert()
            self.timer=pygame.transform.scale(self.timer,(218,120))
            self.timer.set_colorkey((0,0,0))
            self.loc1=(531,0)
            self.text=pygame.font.Font(os.path.join(os.path.dirname(__file__),"./the-golden-blade.regular.ttf"),50)
            self.text_colour=(230,200,120)
            self.textloc=(580,38)
            if game=="Connect4":
                self.bg=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Connect4.png")).convert()
                self.boardscreen=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Connect4_Board.png")).convert()
                self.boardscreen.set_colorkey((0,0,0))
                self.pos=(340,60)
                self.boardsize=600,600
                self.start=(464,210)
                self.tokengap=(58.5,50,5)
                self.x=432,843
                self.y=184,543

                self.token_size=(55,50)
                self.token1=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Coin1.png")).convert()
                self.token1.set_colorkey((0,0,0))
                self.token1=pygame.transform.scale(self.token1,self.token_size)                
                self.token2=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Coin2.png")).convert()
                self.token2.set_colorkey((0,0,0))
                self.token2=pygame.transform.scale(self.token2,self.token_size)

                self.character0_0=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Sprite0_0.png")).convert()
                self.character0_0=pygame.transform.scale(self.character0_0,(140,180))
                self.character0_0.set_colorkey((0,0,0))
                self.character0_1=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Sprite0_1.png")).convert()
                self.character0_1=pygame.transform.scale(self.character0_1,(140,180))
                self.character0_1.set_colorkey((0,0,0))
                self.character1_0=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Sprite1_0.png")).convert()
                self.character1_0=pygame.transform.scale(self.character1_0,(140,180))
                self.character1_0.set_colorkey((0,0,0))
                self.character1_1=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Sprite1_1.png")).convert()
                self.character1_1=pygame.transform.scale(self.character1_1,(140,180))
                self.character1_1.set_colorkey((0,0,0))
                self.character=((self.character0_0,self.character0_1),(self.character1_0,self.character1_1))
                self.ch1pos=(150,390)
                self.ch2pos=(990,390)

                self.Player1=self.text.render(str(players[0]),True,(255,255,255))
                self.text_rect1=self.Player1.get_rect()
                self.text_rect1.center=220,285
                self.tokenloc1=(220-55/2,310)

                self.Player2=self.text.render(str(players[1]),True,(255,255,255))
                self.text_rect2=self.Player2.get_rect()
                self.text_rect2.center=1060,285
                self.tokenloc2=(1060-55/2,310)
                
                self.game_name=self.text.render(str(game),True,self.text_colour)
                self.game_name_rect=self.game_name.get_rect()
                self.game_name_rect.center=640,640
                self.textboxsize=(400,150)
                self.frame_center=(640,635)
        elif name=="futuristic":
            self.timer=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Timer_Future.png")).convert()
            self.timer=pygame.transform.scale(self.timer,(400,120))
            self.timer.set_colorkey((0,0,0))
            self.loc1=(440,0)
            self.text=pygame.font.Font(os.path.join(os.path.dirname(__file__),"./rostex.italic.ttf"),50)
            self.text_colour=(3, 216, 243)
            self.textloc=(535,38)
            if game=="Connect4":
                self.bg=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Connect4_Future.png")).convert()
                self.boardscreen=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Connect4_Board_Future.png")).convert()
                self.boardscreen.set_colorkey((0,0,0))
                self.pos=(192,60)
                self.boardsize=900,600
                self.start=(449,161)
                self.tokengap=(63.6,57.6)
                self.x=416,866
                self.y=133,530

                self.token_size=(60,60)
                self.token1=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Coin1_Future.png")).convert()
                self.token1.set_colorkey((0,0,0))
                self.token1=pygame.transform.scale(self.token1,self.token_size)                
                self.token2=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Coin2_Future.png")).convert()
                self.token2.set_colorkey((0,0,0))
                self.token2=pygame.transform.scale(self.token2,self.token_size)

                self.character0_0=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Sprite0_0_Future.png")).convert()
                self.character0_0=pygame.transform.scale(self.character0_0,(140,180))
                self.character0_0.set_colorkey((0,0,0))
                self.character0_1=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Sprite0_1_Future.png")).convert()
                self.character0_1=pygame.transform.scale(self.character0_1,(140,180))
                self.character0_1.set_colorkey((0,0,0))
                self.character1_0=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Sprite1_0_Future.png")).convert()
                self.character1_0=pygame.transform.scale(self.character1_0,(160,180))
                self.character1_0.set_colorkey((0,0,0))
                self.character1_1=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Sprite1_1_Future.png")).convert()
                self.character1_1=pygame.transform.scale(self.character1_1,(200,180))
                self.character1_1.set_colorkey((0,0,0))
                self.character=((self.character0_0,self.character0_1),(self.character1_0,self.character1_1))
                self.ch1pos=(150,390)
                self.ch2pos=(990,390)

                self.Player1=self.text.render(str(players[0]),True,(255,255,255))
                self.text_rect1=self.Player1.get_rect()
                self.text_rect1.center=220,285
                self.tokenloc1=(220-55/2,310)

                self.Player2=self.text.render(str(players[1]),True,(255,255,255))
                self.text_rect2=self.Player2.get_rect()
                self.text_rect2.center=1060,285
                self.tokenloc2=(1060-55/2,310)
                
                self.game_name=self.text.render(str(game),True,self.text_colour)
                self.game_name_rect=self.game_name.get_rect()
                self.game_name_rect.center=640,640
                self.textboxsize=(600,150)
                self.frame_center=(640,635)
        