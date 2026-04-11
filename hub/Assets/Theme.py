import pygame
import numpy as np
import os
import sys

class Theme:
    def __init__(self,name,game,players):
        if name=="medieval":
            self.timer=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Timer_medieval.png")).convert_alpha()
            self.timer_size=(218,120)
            self.timer=pygame.transform.scale(self.timer,self.timer_size)
            self.loc1=(531,0)
            self.text=pygame.font.Font(os.path.join(os.path.dirname(__file__),"./the-golden-blade.regular.ttf"),50)
            self.text_colour=(230,200,120)
            self.textloc=(640,65)
            self.character0_0=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Sprite0_0_medieval.png")).convert_alpha()
            self.character0_0size=(140,180)
            self.character0_0=pygame.transform.scale(self.character0_0,self.character0_0size)
            self.character0_1=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Sprite0_1_medieval.png")).convert_alpha()
            self.character0_1size=(140,180)
            self.character0_1=pygame.transform.scale(self.character0_1,self.character0_1size)
            self.character1_0=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Sprite1_0_medieval.png")).convert_alpha()
            self.character1_0size=(160,180)
            self.character1_0=pygame.transform.scale(self.character1_0,self.character1_0size)
            self.character1_1=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Sprite1_1_medieval.png")).convert_alpha()
            self.character1_1size=(200,180)
            self.character1_1=pygame.transform.scale(self.character1_1,self.character1_1size)
            self.character=((self.character0_0,self.character0_1),(self.character1_0,self.character1_1))
            self.ch1pos=(150,390)
            self.ch2pos=(990,390)

            self.Player1=self.text.render(str(players[0]),True,(255,255,255))
            self.text_rect1=self.Player1.get_rect()
            self.text_rect1.center=(220,285)
            self.tokenloc1=(220-55/2,310)

            self.Player2=self.text.render(str(players[1]),True,(255,255,255))
            self.text_rect2=self.Player2.get_rect()
            self.text_rect2.center=(1060,285)
            self.tokenloc2=(1060-55/2,310)
                
            self.game_name=self.text.render(str(game),True,self.text_colour)
            self.game_name_rect=self.game_name.get_rect()
            self.game_name_rect.center=640,640
            self.textboxsize=(400,150)
            self.frame_center=(640,635)
            if game=="Connect4":
                self.bg=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Connect4_medieval.png")).convert()
                self.boardscreen=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Connect4_Board_medieval.png")).convert_alpha()
                self.pos=(340,60)
                self.boardsize=600,600
                self.start=(465,210)
                self.tokengap=(58.5,50.5)
                self.x=432,843
                self.y=184,543

                self.token_size=55,50
                self.token1=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Coin1_medieval.png")).convert_alpha()
                self.token1=pygame.transform.scale(self.token1,self.token_size)                
                self.token2=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Coin2_medieval.png")).convert_alpha()
                self.token2=pygame.transform.scale(self.token2,self.token_size)

            if game=="TicTacToe":
                self.bg=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Connect4_medieval.png")).convert()
                self.boardscreen=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/TicTacToe_Board_medieval.png")).convert_alpha()
                self.pos=(290,-60)
                self.boardsize=700,900
                self.start=(441,179)
                self.tokengap=(44.2,35.4)
                self.x=420,863
                self.y=165,517

                self.token_size=(55,40)
                self.token1=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Cross_Medieval.png")).convert_alpha()
                self.token1=pygame.transform.scale(self.token1,self.token_size)                
                self.token2=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Circle_Medieval.png")).convert_alpha()
                self.token2=pygame.transform.scale(self.token2,self.token_size)

            if game=="Othello":
                self.bg=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Connect4_medieval.png")).convert()
                self.boardscreen=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Othello_Board_medieval.png")).convert_alpha()
                self.pos=(340,60)
                self.boardsize=600,600
                self.start=(464,194)
                self.tokengap=(50.14,48.28)
                self.x=445,837
                self.y=184,543

                self.token_size=(50,50)
                self.token1=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Othello1_medieval.png")).convert_alpha()
                self.token1=pygame.transform.scale(self.token1,self.token_size)                
                self.token2=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Othello2_medieval.png")).convert_alpha()
                self.token2=pygame.transform.scale(self.token2,self.token_size)
                self.token3=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Othello3_medieval.png")).convert_alpha()
                self.token3=pygame.transform.scale(self.token3,self.token_size)

                self.character0_0=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Sprite0_0_medieval.png")).convert_alpha()
                self.character0_0=pygame.transform.scale(self.character0_0,(140,180))
                self.character0_1=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Sprite0_1_medieval.png")).convert_alpha()
                self.character0_1=pygame.transform.scale(self.character0_1,(140,180))
                self.character1_0=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Sprite1_0_medieval.png")).convert_alpha()
                self.character1_0=pygame.transform.scale(self.character1_0,(140,180))
                self.character1_1=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Sprite1_1_medieval.png")).convert_alpha()
                self.character1_1=pygame.transform.scale(self.character1_1,(140,180))
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
            self.timer=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Timer_Future.png")).convert_alpha()
            self.timer_size=(400,120)
            self.timer=pygame.transform.scale(self.timer,self.timer_size)
            self.loc1=(440,0)
            self.text=pygame.font.Font(os.path.join(os.path.dirname(__file__),"./rostex.italic.ttf"),50)
            self.text_colour=(3, 216, 243)
            self.textloc=(640,65)
            self.character0_0=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Sprite0_0_Future.png")).convert_alpha()
            self.character0_0size=(140,180)
            self.character0_0=pygame.transform.scale(self.character0_0,self.character0_0size)
            self.character0_1=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Sprite0_1_Future.png")).convert_alpha()
            self.character0_1size=(140,180)
            self.character0_1=pygame.transform.scale(self.character0_1,self.character0_1size)
            self.character1_0=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Sprite1_0_Future.png")).convert_alpha()
            self.character1_0size=(160,180)
            self.character1_0=pygame.transform.scale(self.character1_0,self.character1_0size)
            self.character1_1=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Sprite1_1_Future.png")).convert_alpha()
            self.character1_1size=(200,180)
            self.character1_1=pygame.transform.scale(self.character1_1,self.character1_1size)
            self.character=((self.character0_0,self.character0_1),(self.character1_0,self.character1_1))
            self.ch1pos=(160,390)
            self.ch2pos=(970,390)

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
            if game=="Connect4":
                self.bg=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Connect4_Future.png")).convert()
                self.boardscreen=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Connect4_Board_Future.png")).convert_alpha()
                self.pos=(192,60)
                self.boardsize=900,600
                self.start=(449,161)
                self.tokengap=(63.6,57.6)
                self.x=416,866
                self.y=133,530

                self.token_size=(71,71)
                self.token1=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Coin1_Future.png")).convert_alpha()
                self.token1=pygame.transform.scale(self.token1,self.token_size)                
                self.token2=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Coin2_Future.png")).convert_alpha()
                self.token2=pygame.transform.scale(self.token2,self.token_size)

                
        elif name=="dune":
            self.timer=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Timer_Dune.png")).convert_alpha()
            self.timer_size=(400,100)
            self.timer=pygame.transform.scale(self.timer,self.timer_size)
            self.loc1=(435,0)
            self.text=pygame.font.Font(os.path.join(os.path.dirname(__file__),"./Dune Rise 400.ttf"),50)
            self.text_colour=(233,203,142)
            self.textloc=(640,58)
            self.character0_0=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Sprite0_0_Dune.png")).convert_alpha()
            self.character0_0size=(140,180)
            self.character0_0=pygame.transform.scale(self.character0_0,self.character0_0size)
            self.character0_1=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Sprite0_1_Dune.png")).convert_alpha()
            self.character0_1size=(140,180)
            self.character0_1=pygame.transform.scale(self.character0_1,self.character0_1size)
            self.character1_0=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Sprite1_0_Dune.png")).convert_alpha()
            self.character1_0size=(160,180)
            self.character1_0=pygame.transform.scale(self.character1_0,self.character1_0size)
            self.character1_1=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Sprite1_1_Dune.png")).convert_alpha()
            self.character1_1size=(200,180)
            self.character1_1=pygame.transform.scale(self.character1_1,self.character1_1size)
            self.character=((self.character0_0,self.character0_1),(self.character1_0,self.character1_1))
            self.ch1pos=(165,390)
            self.ch2pos=(975,390)
            self.Player1=self.text.render(str(players[0]),True,(255,255,255))
            self.text_rect1=self.Player1.get_rect()
            self.text_rect1.center=(220,285)
            self.tokenloc1=(220-55/2,310)

            self.Player2=self.text.render(str(players[1]),True,(255,255,255))
            self.text_rect2=self.Player2.get_rect()
            self.text_rect2.center=(1060,285)
            self.tokenloc2=(1060-55/2,310)
            self.text.bold=True
            self.game_name=self.text.render(str(game),True,self.text_colour)
            self.game_name_rect=self.game_name.get_rect()
            self.game_name_rect.center=(640,640)
            self.textboxsize=(750,150)
            self.frame_center=(640,635)

            if game=="Connect4":
                self.bg=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Connect4_Dune.png")).convert()
                self.boardscreen=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Connect4_Board_Dune.png")).convert_alpha()
                self.pos=(315,10)
                self.boardsize=(650,650)
                self.start=(455,165)
                self.tokengap=(60.5,55.2)
                self.x=(420,849)
                self.y=(135,525)

                self.token_size=(60,60)
                self.token1=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Coin1_Dune.png")).convert_alpha()
                self.token1=pygame.transform.scale(self.token1,self.token_size)                
                self.token2=pygame.image.load(os.path.join(os.path.dirname(__file__),"./Images/Coin2_Dune.png")).convert_alpha()
                self.token2=pygame.transform.scale(self.token2,self.token_size)

                
                
        