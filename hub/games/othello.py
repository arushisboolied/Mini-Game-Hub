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

class Othello(Game):

    def __init__(self,game_name="Othello", players=("Player1","Player2"), Resolution=(1280,720), theme="medieval", Characters=(0,1)):
        super().__init__(game_name,players, Resolution, theme, Characters)      
        
        self.Board=np.ones(64,dtype=int).reshape(8,8)*(-1)
        self.Board[3][3] = 0
        self.Board[3][4] = 1
        self.Board[4][3] = 1
        self.Board[4][4] = 0

        self.end = False

        self.directions = np.array([
            [-1,-1], [-1,0], [-1,1],
            [0,-1], [0,0], [0,1],
            [1,-1], [1,0], [1,1]
        ])
    

    def board_check(self,x,y):
        
        squares = np.arange(1,8) 
        dx = self.directions[:, 0][:, None]*squares
        dy = self.directions[:, 1][:, None]*squares

        xs = x + dx
        ys = y + dy

        valid = (xs >= 0) & (xs < 8) & (ys >= 0) & (ys < 8)
        xs = np.where(valid, xs, 0)
        ys = np.where(valid, ys, 0)

        vals = self.Board[ys, xs]
        vals = np.where(valid, vals, -2)

        return xs, ys, vals
       
    
    def check_valid(self, x, y, player):

        if self.Board[y, x] != -1:
            return False

        opponent = 1 - player

        _, _, line = self.board_check(x, y)

        opp = (line == opponent)
        me = (line == player)

        seen_opp = np.cumsum(opp, axis=1)

        capture = me & (seen_opp > 0)

        return np.any(capture)
    

    def flip_pieces(self,x,y,player):
        pass


    def has_valid_moves(self,player):
        pass


    def win_check(self):

        full = np.all(self.Board != -1)
        no_moves = not (self.has_valid_moves(0) or self.has_valid_moves(1))

        if full or no_moves:
            self.end = True


    def update_board(self):

        x, y = self.current_move
        player = self.current_player

        if self.check_valid(x, y, player):
            self.flip_pieces(x, y, player)
            self.switch_turns()
            self.win_check()


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