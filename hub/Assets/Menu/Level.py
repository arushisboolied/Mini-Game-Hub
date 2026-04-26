import pygame
from Test import *
from TileMap import Tile
from Character import Player
from debug import debug
from Settings import Settings

class Level:
    def __init__(self):

        self.display_surface=pygame.display.get_surface()

        self.boundaries=pygame.sprite.Group()

        self.spawn=pygame.sprite.Group()
        self.settings_area=pygame.sprite.Group()
        self.game_selection_area=pygame.sprite.Group()
        self.hinterland=pygame.sprite.Group()
        self.regions=[self.spawn,self.settings_area,self.game_selection_area,self.hinterland]

        self.Player=pygame.sprite.Group()
        
        self.map=pygame.image.load("./Map.png").convert()

        self.width=self.display_surface.get_size()[0]
        self.height=self.display_surface.get_size()[1]  

        self.game_paused=False

        self.settings=Settings()

        self.create_boundary()
        self.create_regions()

        self.Interaction_prompt_image=pygame.image.load("./Interaction.png").convert_alpha()

        self.banners={"Spawn": pygame.image.load("./Spawn_Banner.png").convert_alpha(),
                      "Settings": pygame.image.load("./Settings_Banner.png").convert_alpha(),
                      "Game_Selection": pygame.image.load("./Game_Selection.png").convert_alpha(),
                      "Hinterland": pygame.image.load("./Hinterlands.png").convert_alpha()}   

    def check_zones(self):
        for zone in Interactive:
            x, y = zone["pos"]
            w, h = zone["size"]
            zone_rect = pygame.Rect(x, y, w, h)

            if self.player.hitbox.colliderect(zone_rect):
                return True

    def create_boundary(self):

        self.player=Player((1600,2200),self.Player,self.boundaries,self.regions)

        for row in range(len(Obstacle_Map)):
            for col in range(len(Obstacle_Map[0])):
                x=col*16
                y=row*16
                if Obstacle_Map[row][col]!='-1':
                    Tile((x,y),self.boundaries)

    def create_regions(self):
        for row in range(len(Region_Map)):
            for col in range(len(Region_Map[0])):
                x=col*16
                y=row*16
                if Region_Map[row][col]=='0':
                    Tile((x,y),self.spawn)
                elif Region_Map[row][col]=='1':
                    Tile((x,y),self.settings_area)
                elif Region_Map[row][col]=='2':
                    Tile((x,y),self.game_selection_area)
                elif Region_Map[row][col]=='3':
                        Tile((x,y),self.hinterland)
        
    def camera_draw(self,group):
        self.width=self.display_surface.get_size()[0]
        self.height=self.display_surface.get_size()[1] 
       
        self.offset=[self.player.rect.centerx-self.width/2,self.player.rect.centery-self.height/2]
        self.offset[0]=min(max(self.offset[0],0),4*1280-self.width)
        self.offset[1]=min(max(self.offset[1],0),720*4-self.height)
        self.display_surface.blit(self.map,(-self.offset[0],-self.offset[1]))

        for sprite in group:
            offset_pos=(sprite.rect.topleft[0]-self.offset[0],sprite.rect.topleft[1]-self.offset[1])
            self.display_surface.blit(sprite.image,offset_pos)
        
    def settings_toggle(self):
        self.game_paused=not self.game_paused

    def run(self):

        self.camera_draw(self.boundaries)

        self.camera_draw(self.regions[0])
        self.camera_draw(self.regions[1])
        self.camera_draw(self.regions[2])
        self.camera_draw(self.regions[3])
        self.camera_draw(self.Player)

        
          
        if not self.game_paused:     
            if self.check_zones():
                self.Interaction_prompt_image=pygame.transform.scale(self.Interaction_prompt_image,(self.width*0.5,self.height*0.6))
                rect=self.Interaction_prompt_image.get_rect(center=(self.width/2,self.height*0.85))
                self.display_surface.blit(self.Interaction_prompt_image, rect) 
            
            Banner=self.banners[self.player.Region]
            Banner=pygame.transform.scale(Banner,(self.width*1,self.height*1))
            rect=Banner.get_rect(center=(self.width/2,self.height*0.15))
            self.display_surface.blit(Banner, rect)

            self.Player.update()
            self.offset=self.player.rect.center
            debug(self.player.Region)

        else:
            self.settings.display()