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

class TicTacToe(Game):
    def __init__(self,game_name="Othello", players=("Player1","Player2"), Resolution=(1280,720), theme="medieval", Characters=(0,1)):
        super().__init__(game_name,players, Resolution, theme, Characters)      
        self.Board=np.ones(100,dtype=int).reshape(10,10)*(-1)

    def win_check(self):
        pass

    def update_board(self):
        pass
        
    def event_handler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            y_min, y_max = self.assets.y
            x_min, x_max = self.assets.x

            if y_min <= mouse_y < y_max and x_min <= mouse_x < x_max:
                col_width = (x_max - x_min) / 10
                row_height = (y_max - y_min) / 10

                grid_x = int((mouse_x - x_min) / col_width)
                grid_y = int((mouse_y - y_min) / row_height)

                self.current_move = [grid_x, grid_y]
                self.update_board()
                 
if __name__=="__main__":
    Othello(theme="medieval").run()          