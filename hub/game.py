import pygame
import matplotlib as plt
import numpy as np
import os
import sys
import time
import pathlib
import subprocess
import datetime
import random

sys.path.append(os.path.join(os.path.dirname(__file__),'./Assets'))
from Theme import Theme

"""Things I need for a tictactoe game:
    ~1.Board~
    ~2.Characters/Players~
    ~3.Way to check win~
    ~4.Tokens~
    ~5.Theme~
    6.Size of Screen
    7.Winning Screen
    8.
"""
class Game:
    def __init__(self,game_name,players=("Mohit","Arush"),Resolution=(1280,720),theme="medieval",Characters=(0,1)):
        pygame.init()
        pygame.font.init()
        self.players=players
        self.Resolution=Resolution
        self.theme=theme
        self.Characters=Characters
        self.screen=pygame.display.set_mode(Resolution)
        self.current_player=0
        self.clock=pygame.time.Clock()
        self.current_move=[-1,-1]
        self.assets=Theme(self.theme,game_name,players)
        self.tie=False

    def win_check(self):
        pass

    def switch_turns(self):
        self.current_player=(self.current_player+1)%2

    def generate_board(self):
        image=self.assets.bg
        image2=self.assets.boardscreen
        image=pygame.transform.scale(image,self.Resolution)
        image2=pygame.transform.scale(image2,self.assets.boardsize)
        self.screen.blit(image,(0,0))
        self.screen.blit(image2,self.assets.pos)
        self.frame1=self.screen.subsurface(pygame.Rect(150,390,200,180)).copy()
        self.frame2=self.screen.subsurface(pygame.Rect(990,390,200,180)).copy()

    def generate_players(self):
        character0_0=self.assets.character[self.Characters[0]][0]
        character0_1=self.assets.character[self.Characters[0]][1]
        character1_0=self.assets.character[self.Characters[1]][0]
        character1_1=self.assets.character[self.Characters[1]][1]
        if self.current_player==0:
            self.screen.blit(self.frame2,self.assets.ch2pos)
            self.screen.blit(character1_0,self.assets.ch2pos)
            if (self.timer())%2==0:
                self.screen.blit(self.frame1,self.assets.ch1pos)
                self.screen.blit(character0_0,self.assets.ch1pos)
            if (self.timer())%2==1:
                self.screen.blit(self.frame1,self.assets.ch1pos)
                self.screen.blit(character0_1,self.assets.ch1pos)
        if self.current_player==1:
            self.screen.blit(self.frame1,self.assets.ch1pos)
            self.screen.blit(character0_0,self.assets.ch1pos)
            if (self.timer())%2==0:
                self.screen.blit(self.frame2,self.assets.ch2pos)
                self.screen.blit(character1_0,self.assets.ch2pos)
            if (self.timer())%2==1:
                self.screen.blit(self.frame2,self.assets.ch2pos)
                self.screen.blit(character1_1,self.assets.ch2pos)
        

    def timer(self):
        return int(pygame.time.get_ticks()//250)

    def display_time(self):
        frame=self.assets.timer
        self.time_elapsed=pygame.time.get_ticks()//1000
        mins=self.time_elapsed//60
        seconds=self.time_elapsed%60
        Time=f"{mins:02}:{seconds:02}"
        self.screen.blit(frame,self.assets.loc1)
        text=self.assets.text
        text=text.render(Time,True,self.assets.text_colour)
        self.screen.blit(text,self.assets.textloc)
    
    def display_player_names(self):

        Player1=self.assets.Player1
        text_rect=self.assets.text_rect1
        self.screen.blit(Player1,text_rect)
        Player2=self.assets.Player2
        text_rect=self.assets.text_rect2
        self.screen.blit(Player2,text_rect)
        self.screen.blit(self.assets.token1,self.assets.tokenloc1)
        self.screen.blit(self.assets.token2,self.assets.tokenloc2)

    def display_game_name(self):
        frame=self.assets.timer
        frame=pygame.transform.scale(frame,self.assets.textboxsize)
        frame_rect=frame.get_rect()
        frame_rect.center=self.assets.frame_center
        self.screen.blit(frame,frame_rect)
        game_name=self.assets.game_name
        game_name_rect=self.assets.game_name_rect
        self.screen.blit(game_name,game_name_rect)

        
    def event_handler(self,event):
        pass

    def update_board(self):
        pass

    def run(self):
        self.running=True

        self.generate_board()
        self.display_player_names()
        self.display_game_name()
        
        while self.running:
            
            self.clock.tick(60)
            self.display_time()            

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                    sys.exit()
                else:
                    self.event_handler(event)

            
            self.generate_players()            
            pygame.display.update()




            










    

