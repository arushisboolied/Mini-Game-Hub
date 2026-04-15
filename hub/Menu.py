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

class Menu:
    def __init__(self,character=0,Resolution=(1280,720)):
        pygame.init()
        pygame.font.init()
        self.Resolution=Resolution
        self.character=character
        self.screen=pygame.display.set_mode(Resolution,pygame.RESIZABLE)
        self.clock=pygame.time.Clock()

    def event_handler(self,event):
        pass

    def run(self):
        running=True
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                    pygame.quit()
                    sys.exit()
                else:
                    self.event_handler(event)
            pygame.display.update()
            

