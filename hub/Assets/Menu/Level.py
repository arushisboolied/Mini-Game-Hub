import pygame
from Test import *
from TileMap import Tile
from Character import Player
from debug import debug

class Level:
    def __init__(self):

        self.display_surface=pygame.display.get_surface()

        self.boundaries=pygame.sprite.Group()
        self.interactive=pygame.sprite.Group()
        self.Player=pygame.sprite.Group()
        
        self.map=pygame.image.load("./Map.png").convert()

        self.width=self.display_surface.get_size()[0]
        self.height=self.display_surface.get_size()[1]  

        self.create_boundary()

    def create_boundary(self):
        self.player=Player((1624,2326),self.Player,self.boundaries,self.interactive)

        for row in range(len(Obstacle_Map)):
            for col in range(len(Obstacle_Map[0])):
                x=col*16
                y=row*16
                if Obstacle_Map[row][col]=='78':
                    Tile((x,y),self.boundaries)
        
    def camera_draw(self,group):
       
        self.offset=[self.player.rect.centerx-self.width/2,self.player.rect.centery-self.height/2]
        self.offset[0]=min(max(self.offset[0],0),1280*4-1280)
        self.offset[1]=min(max(self.offset[1],0),720*4-720)
        self.display_surface.blit(self.map,(-self.offset[0],-self.offset[1]))

        for sprite in group:
            offset_pos=(sprite.rect.topleft[0]-self.offset[0],sprite.rect.topleft[1]-self.offset[1])
            self.display_surface.blit(sprite.image,offset_pos)

    def run(self):
          
        
        self.camera_draw(self.boundaries)
        self.camera_draw(self.Player)
        self.Player.update()
        self.offset=self.player.rect.center
        debug(self.player.status)