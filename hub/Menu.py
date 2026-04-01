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
    def __init__(self,character=1,Resolution=(1280,720),Theme="medieval"):
        pygame.init()
        pygame.font.init()
        self.Resolution=Resolution
        self.Theme=Theme
        self.character=character
        self.screen=pygame.display.set_mode(Resolution)
        self.clock=pygame.time.Clock()
        background=pygame.image.load("./hub/Menu assets/Images/Background1.jpg").convert()
        self.background=pygame.transform.scale(background,Resolution)

    def event_handler(self,event):
        pass

    def run(self):
        running=True
        while running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                    pygame.quit()
                    sys.exit()
                else:
                    self.event_handler(event)
            self.screen.fill((0,0,0))
            self.screen.blit(self.background,(0,0))
            pygame.display.update()
            self.clock.tick(60)

Menu().run()
