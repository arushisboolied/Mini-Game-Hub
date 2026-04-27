import pygame,os
from Test import *




class Player(pygame.sprite.Sprite):
    def __init__(self,pos,group,obstacles,regions):
        super().__init__(group)
        self.character_selection=0
        self.character=[
        [
            [[i,pygame.transform.scale(pygame.image.load(r"./Tiny_Swords/Units/Blue_Units/Warrior/Warrior_Idle/row-1-column-"+str(i)+r".png").convert_alpha(),(192,192))] for i in range(1,9)],
            [[i,pygame.transform.scale(pygame.image.load(r"./Tiny_Swords/Units/Blue_Units/Warrior/Warrior_Run/row-1-column-"+str(i)+r".png").convert_alpha(),(192,192))] for i in range(1,7)]
        ],
        [
            [[i,pygame.transform.scale(pygame.image.load(r"./Tiny_Swords/Units/Red_Units/Warrior/Warrior_Idle/row-1-column-"+str(i)+r".png").convert_alpha(),(192,192))] for i in range(1,9)],
            [[i,pygame.transform.scale(pygame.image.load(r"./Tiny_Swords/Units/Red_Units/Warrior/Warrior_Run/row-1-column-"+str(i)+r".png").convert_alpha(),(192,192))] for i in range(1,7)]
        ]
        ]
        
        self.animation_index=0
        self.image=self.character[self.character_selection][0][int(self.animation_index)%8][1]
        self.rect=self.image.get_rect(topleft=pos).copy()
        self.hitbox=self.rect.inflate(-144,-160)
        self.hitbox.y+=32
        self.direction=pygame.math.Vector2()
        self.speed=5
        self.status='right'

        self.obstacles=obstacles
        self.regions=regions

        self.Region="Spawn"

        self.zone=None

    def input(self):
        keys=pygame.key.get_pressed()

        self.direction.y=int((keys[pygame.K_DOWN] or keys[pygame.K_s])-(keys[pygame.K_UP] or keys[pygame.K_w]))
        self.direction.x=int((keys[pygame.K_RIGHT] or keys[pygame.K_d])-(keys[pygame.K_LEFT] or keys[pygame.K_a]))

    def get_status(self):
        if self.direction.x==1:
            self.status='right'
        elif self.direction.x==-1:
            self.status='left'
        if self.direction.magnitude()==0:
            if 'idle' not in self.status:
                if 'move' in self.status:
                    self.status=self.status.replace('move','idle')
                else:
                    self.status+='_idle'
        else:
            if 'move' not in self.status:
                if 'idle' in self.status:
                    self.status=self.status.replace('idle','move')
                else:
                    self.status+='_move'

    def collisions(self,hitbox):
        for sprite in self.obstacles:
            if pygame.rect.Rect.colliderect(hitbox,sprite.rect):
                return True
             
    def region_change(self,hitbox):
        
        for sprite in self.regions[0]:
            if pygame.rect.Rect.colliderect(hitbox,sprite.rect):
                self.Region="Spawn"
                return 0
        for sprite in self.regions[1]:
            if pygame.rect.Rect.colliderect(hitbox,sprite.rect):
                self.Region="Settings"
                return 0
        for sprite in self.regions[2]:
            if pygame.rect.Rect.colliderect(hitbox,sprite.rect):
                self.Region="Game_Selection"
                return 0
        for sprite in self.regions[3]:
            if pygame.rect.Rect.colliderect(hitbox,sprite.rect):
                self.Region="Hinterland"
                return 0                   

    def move(self,speed):

        if self.direction.magnitude()!=0:
            self.direction_speed=self.direction.normalize()
        else:
            self.direction_speed=self.direction
        
        new_rect=self.hitbox.copy()
        new_rect.center+=self.direction_speed*speed
        if self.collisions(new_rect):
            pass
        else:
            self.rect.center+=self.direction_speed*speed
            self.hitbox.center+=self.direction_speed*speed

    def animate(self):
        self.animation_index=self.animation_index+0.15
        if self.status=='right_move':
            self.image=self.character[self.character_selection][1][int(self.animation_index)%6][1]
        elif self.status=='left_move':
            self.image=self.character[self.character_selection][1][int(self.animation_index)%6][1]
            self.image=pygame.transform.flip(self.image,flip_x=True,flip_y=False)
        elif self.status=='left_idle':
            self.image=self.character[self.character_selection][0][int(self.animation_index)%8][1]
            self.image=pygame.transform.flip(self.image,flip_x=True,flip_y=False)
        elif self.status=='right_idle':
            self.image=self.character[self.character_selection][0][int(self.animation_index)%8][1]
        
        self.rect=self.image.get_rect(center=self.hitbox.center)
        self.rect.y-=32

    def check_zones(self):
        for zone in Interactive:
            x, y = zone["pos"]
            w, h = zone["size"]
            zone_rect = pygame.Rect(x, y, w, h)

            if self.hitbox.colliderect(zone_rect):
                self.zone=zone
                return True
        return False

    def update(self):

        self.input()
        self.move(self.speed)
        self.region_change(self.hitbox)        
        self.get_status()
        self.animate()

        