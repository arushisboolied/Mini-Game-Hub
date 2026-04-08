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
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from game import Game

class Connect4(Game):
    def __init__(self,game_name="Connect4", players=("Mohit","Arush"), Resolution=(1280,720), theme="medieval", Characters=(0,1)):
        super().__init__(game_name,players, Resolution, theme, Characters)      
        self.Board=np.ones(49,dtype=int).reshape(7,7)*(-1)

    def win_check(self):
        x,y=self.current_move
        checker=np.ones(4,dtype=int)*(self.current_player)
        if (self.Board[x,0:4]==checker).all() or (self.Board[x,1:5]==checker).all() or (self.Board[x,2:6]==checker).all() or (self.Board[x,3:7]==checker).all():
            return True
        if (self.Board[0:4,y]==checker).all() or (self.Board[1:5,y]==checker).all() or (self.Board[2:6,y]==checker).all() or (self.Board[3:7,y]==checker).all():
            return True
        Diag1=np.diagonal(self.Board,offset=y-x)
        Board2=np.fliplr(self.Board)
        Diag2=np.diagonal(Board2,offset=6-x-y)

        if (len(Diag1[0:4])==4 and (Diag1[0:4]==checker).all()) or (len(Diag1[1:5])==4 and (Diag1[1:5]==checker).all()) or (len(Diag1[2:6])==4 and (Diag1[2:6]==checker).all()) or (len(Diag1[3:7])==4 and (Diag1[3:7]==checker).all()) or (len(Diag2[0:4])==4 and (Diag2[0:4]==checker).all()) or (len(Diag2[1:5])==4 and (Diag2[1:5]==checker).all()) or (len(Diag2[2:6])==4 and (Diag2[2:6]==checker).all()) or (len(Diag2[3:7])==4 and (Diag2[3:7]==checker).all()):
            return True
        
        return False
    
    def update_board(self):
        x=self.current_move[0]
        col = self.Board[x, :]
        empty = np.where(col == -1)[0]
        if empty.size > 0:
            self.Board[x, empty[-1]] = self.current_player
            self.current_move[1] = empty[-1]
            self.redraw_tokens()
            Checker=np.ones(49,dtype="int").reshape(7,7)*(-1)
                
            if self.win_check():
                self.running=False
            elif not((self.Board==Checker).any()):
                self.running=False
                self.tie=True
            else:
                self.switch_turns()
        
    
    def event_handler(self, event):
        if event.type==pygame.MOUSEBUTTONDOWN:
            self.current_move=list(pygame.mouse.get_pos())
            x, y = self.current_move
            y_min,y_max=self.assets.y
            y_min=y_min*self.Resolution[1]/720
            y_max=y_max*self.Resolution[1]/720
            x_min, x_max = self.assets.x
            x_min=x_min*self.Resolution[0]/1280
            x_max=x_max*self.Resolution[0]/1280

            if y_min <= y < y_max and x_min <= x < x_max:
                col_width = (x_max - x_min) / 7
                self.current_move[0] = int((x - x_min) / col_width)
                self.update_board()
                 
if __name__=="__main__":
    Connect4(theme="dune").run()          