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
        self.game_name=game_name
        self.players=players
        self.Resolution=Resolution
        self.theme=theme
        self.Characters=Characters
        self.screen=pygame.display.set_mode(Resolution,pygame.RESIZABLE)
        self.current_player=0
        self.clock=pygame.time.Clock()
        self.current_move=[-1,-1]
        self.assets=Theme(self.theme,game_name,players)
        self.tie=False

    def win_check(self):
        pass

    def switch_turns(self):
        self.current_player=(self.current_player+1)%2

    def generate_background(self):
        image=self.assets.bg
        image=pygame.transform.scale(image,self.Resolution)
        self.screen.blit(image,(0,0))
        self.frame1=self.screen.subsurface(pygame.Rect(self.assets.ch1pos[0]*self.Resolution[0]/1280,self.assets.ch1pos[1]*self.Resolution[1]/720,200*self.Resolution[0]/1280,180*self.Resolution[1]/720)).copy()
        self.frame2=self.screen.subsurface(pygame.Rect(self.assets.ch2pos[0]*self.Resolution[0]/1280,self.assets.ch2pos[1]*self.Resolution[1]/720,200*self.Resolution[0]/1280,180*self.Resolution[1]/720)).copy()

    def generate_board(self):
        image2=self.assets.boardscreen
        boardsize=list(np.array(self.assets.boardsize)*np.array(self.Resolution)/np.array([1280,720]))
        image2=pygame.transform.scale(image2,boardsize)
        pos=list(np.array(self.assets.pos)*np.array(self.Resolution)/np.array([1280,720]))
        self.screen.blit(image2,pos)


    def generate_players(self):
        character0_0=pygame.transform.scale(self.assets.character[self.Characters[0]][0],(self.assets.character0_0size[0]*self.Resolution[0]/1280,self.assets.character0_0size[1]*self.Resolution[1]/720))
        character0_1=pygame.transform.scale(self.assets.character[self.Characters[0]][1],(self.assets.character0_1size[0]*self.Resolution[0]/1280,self.assets.character0_1size[1]*self.Resolution[1]/720))
        character1_0=pygame.transform.scale(self.assets.character[self.Characters[1]][0],(self.assets.character1_0size[0]*self.Resolution[0]/1280,self.assets.character1_0size[1]*self.Resolution[1]/720))
        character1_1=pygame.transform.scale(self.assets.character[self.Characters[1]][1],(self.assets.character1_1size[0]*self.Resolution[0]/1280,self.assets.character1_1size[1]*self.Resolution[1]/720))
        character1_0=pygame.transform.flip(character1_0,flip_x=True,flip_y=False)
        character1_1=pygame.transform.flip(character1_1,flip_x=True,flip_y=False)
        ch2pos=list(np.array(self.assets.ch2pos)*np.array(self.Resolution)/np.array([1280,720]))
        ch1pos=list(np.array(self.assets.ch1pos)*np.array(self.Resolution)/np.array([1280,720]))
        if self.current_player==0:            
            self.screen.blit(self.frame2,ch2pos)
            self.screen.blit(character1_0,ch2pos)
            if (self.timer())%2==0:
                self.screen.blit(self.frame1,ch1pos)
                self.screen.blit(character0_0,ch1pos)
            if (self.timer())%2==1:
                self.screen.blit(self.frame1,ch1pos)
                self.screen.blit(character0_1,ch1pos)
        if self.current_player==1:
            self.screen.blit(self.frame1,ch1pos)
            self.screen.blit(character0_0,ch1pos)
            if (self.timer())%2==0:
                self.screen.blit(self.frame2,ch2pos)
                self.screen.blit(character1_0,ch2pos)
            if (self.timer())%2==1:
                self.screen.blit(self.frame2,ch2pos)
                self.screen.blit(character1_1,ch2pos)
        

    def timer(self):
        return int(pygame.time.get_ticks()//250)

    def display_time(self):
        timer_size=list(np.array(self.assets.timer_size)*np.array(self.Resolution)/np.array([1280,720]))
        frame=pygame.transform.scale(self.assets.timer,timer_size)
        self.time_elapsed=pygame.time.get_ticks()//1000
        mins=self.time_elapsed//60
        seconds=self.time_elapsed%60
        Time=f"{mins:02}:{seconds:02}"
        loc1=list(np.array(self.assets.loc1)*np.array(self.Resolution)/np.array([1280,720]))
        self.screen.blit(frame,loc1)
        text=self.assets.text
        text=text.render(Time,True,self.assets.text_colour)
        timertextrect=text.get_rect()
        timertextrect.center=list(np.array(self.assets.textloc)*np.array(self.Resolution)/np.array([1280,720]))
        self.screen.blit(text,timertextrect)
    
    def display_player_names(self):

        Player1=self.assets.Player1
        text_rect1=self.assets.text_rect1.copy()
        text_rect1.center=list(np.array(self.assets.text_rect1.center)*np.array(self.Resolution)/np.array([1280,720]))
        self.screen.blit(Player1,text_rect1)
        Player2=self.assets.Player2
        text_rect2=self.assets.text_rect2.copy()
        text_rect2.center=list(np.array(self.assets.text_rect2.center)*np.array(self.Resolution)/np.array([1280,720]))
        self.screen.blit(Player2,text_rect2)
        token_size=list(np.array(self.assets.token_size)*np.array(self.Resolution)/np.array([1280,720]))
        tokenloc1=list(np.array(self.assets.tokenloc1)*np.array(self.Resolution)/np.array([1280,720]))
        coin=pygame.transform.scale(self.assets.token1,token_size)
        self.screen.blit(coin,tokenloc1)
        tokenloc2=list(np.array(self.assets.tokenloc2)*np.array(self.Resolution)/np.array([1280,720]))
        coin=pygame.transform.scale(self.assets.token2,token_size)
        self.screen.blit(coin,tokenloc2)

    def display_game_name(self):
        timer_size=list(np.array(self.assets.timer_size)*np.array(self.Resolution)/np.array([1280,720]))
        frame=pygame.transform.scale(self.assets.timer,timer_size)
        textboxsize=list(np.array(self.assets.textboxsize)*np.array(self.Resolution)/np.array([1280,720]))
        frame=pygame.transform.scale(frame,textboxsize)
        frame_rect=frame.get_rect()
        frame_rect.center=list(np.array(self.assets.frame_center)*np.array(self.Resolution)/np.array([1280,720]))
        self.screen.blit(frame,frame_rect)
        game_name=self.assets.game_name
        game_name_rect=self.assets.game_name_rect.copy()
        game_name_rect.center=list(np.array(self.assets.game_name_rect.center)*np.array(self.Resolution)/np.array([1280,720]))
        game_name_rect.size=list(np.array(self.assets.game_name_rect.size)*np.array(self.Resolution)/np.array([1280,720]))
        self.screen.blit(game_name,game_name_rect)
        
    def event_handler(self,event):
        pass

    def update_board(self):
        pass

    def redraw_tokens(self):
        token_size=list(np.array(self.assets.token_size)*np.array(self.Resolution)/np.array([1280,720]))
        for x in range(len(self.Board)):
            for y in range(len(self.Board)):
                pos=self.Board[x,y]
                if pos==0:
                    coin=pygame.transform.scale(self.assets.token1,token_size)
                    self.screen.blit(coin,(self.assets.start[0]*self.Resolution[0]/1280-self.assets.token_size[0]*self.Resolution[0]/2560+self.assets.tokengap[0]*x*self.Resolution[0]/1280,self.assets.start[1]*self.Resolution[1]/720-self.assets.token_size[1]*self.Resolution[1]/720/2+self.assets.tokengap[1]*y*self.Resolution[1]/720))
                elif pos==1:
                    coin=pygame.transform.scale(self.assets.token2,token_size)
                    self.screen.blit(coin,(self.assets.start[0]*self.Resolution[0]/1280-self.assets.token_size[0]*self.Resolution[0]/2560+self.assets.tokengap[0]*x*self.Resolution[0]/1280,self.assets.start[1]*self.Resolution[1]/720-self.assets.token_size[1]*self.Resolution[1]/720/2+self.assets.tokengap[1]*y*self.Resolution[1]/720))
    def run(self):
        self.running=True

        self.generate_background()
        self.generate_board()
        self.display_player_names()
        self.display_game_name()
        
        while self.running:
            
            self.clock.tick(60)
            self.redraw_tokens()  
            self.display_time()  
            self.display_game_name()      

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                    sys.exit()
                elif event.type == pygame.VIDEORESIZE:    
                    self.Resolution = event.size
                    self.screen = pygame.display.set_mode(self.Resolution, pygame.RESIZABLE)
                    self.generate_background()
                    self.generate_board()
                    self.display_player_names()
                    self.display_game_name()
                    self.redraw_tokens()
                    
                else:
                    self.event_handler(event)

            
            self.generate_players()            
            pygame.display.update()




            










    

