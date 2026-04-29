import pygame
from Support import *
from Tile import Tile
from Character import Player
from debug import debug
from Settings import Settings

class Level:
    def __init__(self):
        #Creates interaction between map and player
        self.display_surface=pygame.display.get_surface()
        #Boundary for player
        self.boundaries=pygame.sprite.Group()
        #Regions
        self.spawn=pygame.sprite.Group()
        self.settings_area=pygame.sprite.Group()
        self.game_selection_area=pygame.sprite.Group()
        self.hinterland=pygame.sprite.Group()
        self.regions=[self.spawn,self.settings_area,self.game_selection_area,self.hinterland]

        self.Player=pygame.sprite.Group()
        
        self.map=pygame.image.load(Map_image_path).convert() #Map image

        self.width=self.display_surface.get_size()[0]
        self.height=self.display_surface.get_size()[1]  

        #To display other games and leaderboard and settings
        self.game_paused=False

        self.settings=Settings()

        #Create the tiles of boundary
        self.create_boundary()
        self.create_regions()

        #Press E to interact
        self.Interaction_prompt_image=pygame.image.load(Interaction_prompt_image_path).convert_alpha()

        #Displays regions you are in
        self.banners={
                    "Spawn": pygame.image.load(Spawn_Banner_image_path).convert_alpha(),
                    "Settings": pygame.image.load(Settings_Banner_image_path).convert_alpha(),
                    "Game_Selection": pygame.image.load(Game_Selection_image_path).convert_alpha(),
                    "Hinterland": pygame.image.load(Hinterland_image_path).convert_alpha()
                    }
        #Game themes
        self.game_theme=0   
        #User character selection
        self.User1_selection=0
        self.User2_selection=0

        self.call_leaderboard=False

    #Creates tile group for boundary
    def create_boundary(self):

        self.player=Player((1600,2200),self.Player,self.boundaries,self.regions)

        for row in range(len(Obstacle_Map)):
            for col in range(len(Obstacle_Map[0])):
                x=col*16
                y=row*16
                if Obstacle_Map[row][col]!='-1':
                    Tile((x,y),self.boundaries)
    #Creates regions boundary so to get transitions between regionss
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

    #To draw with offset so that player is in center and map follows him  
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
    
    #If the user is in a setting
    def settings_toggle(self):
        self.game_paused=not self.game_paused

    def run(self):
        #Blitting them on screen
        self.camera_draw(self.boundaries)
        self.camera_draw(self.regions[0])
        self.camera_draw(self.regions[1])
        self.camera_draw(self.regions[2])
        self.camera_draw(self.regions[3])
        self.camera_draw(self.Player)

        
        #If player not in setting, continue regular execution. else stop taking user input for player control
        if not self.game_paused:     
            if self.player.check_zones():
                self.Interaction_prompt_image=pygame.transform.scale(self.Interaction_prompt_image,(self.width*0.5,self.height*0.6))
                rect=self.Interaction_prompt_image.get_rect(center=(self.width/2,self.height*0.88))
                self.display_surface.blit(self.Interaction_prompt_image, rect) 
            
            Banner=self.banners[self.player.Region]
            Banner=pygame.transform.scale(Banner,(self.width*1,self.height*1))
            rect=Banner.get_rect(center=(self.width/2,self.height*0.15))
            self.display_surface.blit(Banner, rect)

            self.Player.update()
            self.offset=self.player.rect.center

        else:
            #Return variables from settings selection to level class
            self.settings.zone=self.player.zone
            self.settings.player_speed=self.player.speed
            self.settings.character_selection=self.player.character_selection
            self.settings.Menu_character=self.player.character
            self.settings.theme=self.game_theme
            self.settings.User1_character_selection=self.User1_selection
            self.settings.User2_character_selection=self.User2_selection
            self.settings.run()
            self.User1_selection=self.settings.User1_character_selection
            self.User2_selection=self.settings.User2_character_selection
            self.game_theme=self.settings.theme
            self.player.speed=self.settings.player_speed
            self.player.character_selection=self.settings.character_selection