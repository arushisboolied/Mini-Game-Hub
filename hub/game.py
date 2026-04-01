import pygame
import matplotlib
import numpy
import os
import sys
import time
import pathlib
import subprocess
import datetime
import random

"""Things I need for a tictactoe game:
    1.Board
    2.Characters/Players
    3.Way to check win
    4.Tokens
    5.Theme
    6.Size of Screen
    7.Winning Screen
    8.
"""
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
        bg=pygame.image.load("hub/Assets/Images/Background1.jpg").convert()
        bg=pygame.transform.scale(bg,Resolution)
        self.screen.blit(bg)

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
        running=True

        self.generate_board()
        self.generate_players()
        
        while running:
            
            self.clock.tick(60)
            self.time_elapsed=self.timer()

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                    sys.exit()
                else:
                    self.event_handler(event)
            pygame.display.update()

            if self.win_check():
                running=False
            else:
                self.switch_turns()


Game().run()

            










    

