import pygame
import os,sys

from Test import *

class Settings:
    def __init__(self):
        self.display_surface=pygame.display.get_surface()
    
    def display(self):
        Width=self.display_surface.get_size()[0]
        Height=self.display_surface.get_size()[1]
        image=pygame.image.load("./Character_Selection.png").convert_alpha()
        image=pygame.transform.scale(image,(Width*0.8,Height*0.8))
        rect=image.get_rect(center=(Width/2,Height/2))
        self.display_surface.blit(image,rect)