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
"""442 209
498 211
554 213
611 213
670 213
722 214
778 215
836 214
442 520"""
class Game:
    def __init__(self,players=(0,0),Resolution=(1280,720),Theme="medieval",Characters=(1,2)):
        pygame.init()
        pygame.font.init()
        self.players=players
        self.Resolution=Resolution
        self.Theme=Theme
        self.Characters=Characters
        self.screen=pygame.display.set_mode(Resolution)
        self.current_player=0
        self.clock=pygame.time.Clock()
        self.current_move=[-1,-1]

    def win_check(self):
        pass

    def switch_turns(self):
        self.current_player=(self.current_player+1)%2

    def generate_board(self):
        pass

    def generate_players(self):
        pass

    def timer(self):
        return int(pygame.time.get_ticks()//1000)
    
    def event_handler(self,event):
        pass

    def update_board(self):
        pass

    def run(self):
        self.running=True

        self.generate_board()
        self.generate_players()
        
        while self.running:
            
            self.clock.tick(60)
            self.time_elapsed=self.timer()

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                    sys.exit()
                else:
                    self.event_handler(event)
            
            pygame.display.update()

            

class Connect4(Game):
    def __init__(self, players=(0,0), Resolution=(1280,720), Theme="medieval", Characters=(1,2)):
        super().__init__(players, Resolution, Theme, Characters)
        self.Board_screen=None

    def win_check(self):
        x,y=self.current_move
        checker=np.ones(4,dtype=int)*(self.current_player)
        if (self.Board[x,0:4]==checker).all() or (self.Board[x,1:5]==checker).all() or (self.Board[x,2:6]==checker).all() or (self.Board[x,3:7]==checker).all():
            return True
        if (self.Board[0:4,y]==checker).all() or (self.Board[1:5,y]==checker).all() or (self.Board[2:6,y]==checker).all() or (self.Board[3:7,y]==checker).all():
            return True
        Diag1=np.diagonal(self.Board,offset=x-y)
        Board2=np.fliplr(self.Board)
        Diag2=np.diagonal(Board2,offset=y-x)

        if (len(Diag1[0:4])==4 and (Diag1[0:4]==checker).all()) or (len(Diag1[1:5])==4 and (Diag1[1:5]==checker).all()) or (len(Diag1[2:6])==4 and (Diag1[2:6]==checker).all()) or (len(Diag1[3:7])==4 and (Diag1[3:7]==checker).all()) or (len(Diag2[0:4])==4 and (Diag2[0:4]==checker).all()) or (len(Diag2[1:5])==4 and (Diag2[1:5]==checker).all()) or (len(Diag2[2:6])==4 and (Diag2[2:6]==checker).all()) or (len(Diag2[3:7])==4 and (Diag2[3:7]==checker).all()):
            return True
        
        return False
    
    def generate_board(self):
        self.Board=np.ones(49,dtype=int).reshape(7,7)*(-1)
        image=pygame.image.load("hub/Assets/Images/Connect4.png").convert()
        image2=pygame.image.load("hub/Assets/Images/Connect4_Board.png").convert()
        image2.set_colorkey((255,255,255))
        image=pygame.transform.scale(image,self.Resolution)
        image2=pygame.transform.scale(image2,(600,600))
        self.screen.blit(image,(0,0))
        self.screen.blit(image2,(340,60))
    
    def update_board(self):
        x=self.current_move[0]
        col = self.Board[x, :]
        empty = np.where(col == -1)[0]
        if empty.size > 0:
            self.Board[x, empty[-1]] = self.current_player
            self.current_move[1] = empty[-1]
            print(self.Board)
            if self.win_check():
                self.running=False
                    
                print(self.current_player,"WON")
            else:
                self.switch_turns()

        
    
    def event_handler(self, event):
        if event.type==pygame.MOUSEBUTTONDOWN:
            self.current_move=list(pygame.mouse.get_pos())
            x,y=self.current_move
            if 209<=y<520 and 443<=x<836:
                if 442<=x<498:
                    self.current_move[0]=0
                elif 498<=x<554:
                    self.current_move[0]=1
                elif 554<=x<611:
                    self.current_move[0]=2
                elif 611<=x<670:
                    self.current_move[0]=3
                elif 670<=x<722:
                    self.current_move[0]=4
                elif 722<=x<778:
                    self.current_move[0]=5
                elif 778<=x<836:
                    self.current_move[0]=6

                self.update_board()
                
                
                
                

Connect4().run()          