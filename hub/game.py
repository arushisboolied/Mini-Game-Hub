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

class Game:

    def __init__(self,name,resolution=(800,600),customization=None):
        pygame.init()
        pygame.font.init()
        self.FONT=pygame.font.Font(None,32)
        self.name = name
        self.resolution = resolution
        self.customization = customization
        self.screen = pygame.display.set_mode(self.resolution)
        self.clock = pygame.time.Clock()
        self.running = False
        self.events={}
        self.turn=1
    
    def win_check(self):
        return True
    
    def display_score(self):
        for event in pygame.event.get():
            if event.type == "":
                Menu.start()

    def start(self):
        self.running = True

        while self.running:
            self.clock.tick(60) 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                if event.type in self.events:
                    self.events[event.type](event)
            
            if self.win_check():
                self.display_score()
                self.running = False


class Menu(Game):
    
    def __init__(self,name=None,resolution=(800,600),customization=None):
        super().__init__(name,resolution,customization)

    def buttons(self):        
        Start=pygame.Rect(300,200,200,50)
        Settings=pygame.Rect(300,300,200,50)
        Quit=pygame.Rect(300,400,200,50)
        pygame.draw.rect(self.screen,(0,255,0),Start)
        pygame.draw.rect(self.screen,(255,255,0),Settings)
        pygame.draw.rect(self.screen,(255,0,0),Quit)
        
        Start_text=self.FONT.render("Start",True,(255,255,255))
        self.screen.blit(Start_text,Start)
        Settings_text=self.FONT.render("Settings",True,(255,255,255))
        self.screen.blit(Settings_text,Settings)
        Quit_text=self.FONT.render("Quit",True,(255,255,255))
        self.screen.blit(Quit_text,Quit)

        
        pygame.display.update()

    def start(self):
        self.running = True

        while self.running:
            self.clock.tick(60) 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type in self.events:
                    self.events[event.type](event)

            self.buttons()
        

Menu().start()