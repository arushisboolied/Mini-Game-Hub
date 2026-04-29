import os,sys
import pygame
from Support import *


class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)

        self.image=pygame.image.load(Boundary_image_path).convert()
        self.image.set_alpha(0)
        self.rect=self.image.get_rect(topleft=pos)

