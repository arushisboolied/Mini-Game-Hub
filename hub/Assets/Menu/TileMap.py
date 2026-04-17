import os
import pygame
import sys

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)

        self.image=pygame.image.load("./Boundary.png").convert()
        self.image.set_alpha(0)
        self.rect=self.image.get_rect(topleft=pos)

