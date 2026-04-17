import pygame,os
from Test import *




class Player(pygame.sprite.Sprite):
    def __init__(self,pos,group,obstacles,interactive):
        super().__init__(group)
        self.player_idle_assets=[[i,pygame.transform.scale(pygame.image.load(r"./Tiny_Swords/Units/Blue_Units/Warrior/Warrior_Idle/row-1-column-"+str(i)+r".png").convert_alpha(),(128,128))] for i in range(1,9)]
        self.player_run_assets=[[i,pygame.transform.scale(pygame.image.load(r"./Tiny_Swords/Units/Blue_Units/Warrior/Warrior_Run/row-1-column-"+str(i)+r".png").convert_alpha(),(128,128))] for i in range(1,7)]
        self.animation_index=0
        self.image=self.player_idle_assets[self.animation_index][1]
        self.image=pygame.transform.scale(self.image,(128,128))
        self.rect=self.image.get_rect(topleft=pos).copy()
        self.hitbox=self.rect.inflate(-110,-118).move(0,12)
        self.direction=pygame.math.Vector2()
        self.speed=5
        self.status='right'

        self.obstacles=obstacles
        self.interactive=interactive

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
            self.image=self.player_run_assets[int(self.animation_index)%6][1]
        elif self.status=='left_move':
            self.image=self.player_run_assets[int(self.animation_index)%6][1]
            self.image=pygame.transform.flip(self.image,flip_x=True,flip_y=False)
        elif self.status=='left_idle':
            self.image=self.player_idle_assets[int(self.animation_index)%8][1]
            self.image=pygame.transform.flip(self.image,flip_x=True,flip_y=False)
        elif self.status=='right_idle':
            self.image=self.player_idle_assets[int(self.animation_index)%8][1]
        
        self.rect=self.image.get_rect(center=self.hitbox.center)

    def update(self):
        self.input()
        self.move(self.speed)
        
        self.get_status()

        self.animate()

        