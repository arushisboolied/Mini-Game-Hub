import pygame
import os,sys

from Test import *

class Settings:
    def __init__(self):
        self.display_surface=pygame.display.get_surface()
        
        self.Interaction_exit_prompt_image=pygame.image.load("./Interaction_Exit.png").convert_alpha()
        self.text_banner_image=pygame.image.load("./Settings_Text.png").convert_alpha()
        pygame.font.init()
        self.font=pygame.font.Font("Righteous.ttf", 30)

        self.zone=None
        self.player_speed=None
        self.character_selection=None
        self.Menu_character=None
        self.theme=None
        self.animation_index=0
    
    def run(self):

        keys=pygame.key.get_just_pressed()

        Width=self.display_surface.get_size()[0]
        Height=self.display_surface.get_size()[1]

        if "Char" in self.zone["Zone"] or "Theme" in self.zone["Zone"] or "Speed" in self.zone["Zone"]:

            image=pygame.image.load("./Character_Selection.png").convert_alpha()
            image=pygame.transform.scale(image,(Width*0.8,Height*0.8))

            rect=image.get_rect(center=(Width/2,Height*0.45))
            self.display_surface.blit(image,rect) 

            self.text_banner_image=pygame.transform.scale(self.text_banner_image,(Width*1.035,Height*0.2))
            rect=self.text_banner_image.get_rect(center=(Width/2,Height*0.09))
            self.display_surface.blit(self.text_banner_image, rect)

            if self.zone["Zone"]=="Speed":
                Text=self.font.render("Speed of Menu Character", True, "black")
                rect=Text.get_rect(center=(Width/2,Height*0.07))
                self.display_surface.blit(Text, rect)

                
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    self.player_speed+=1
                    if self.player_speed>10:
                        self.player_speed=10
                elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    self.player_speed-=1
                    if self.player_speed<1:
                        self.player_speed=1
                
                Text_speed=self.font.render(str(self.player_speed), True, "black")
                rect=Text_speed.get_rect(center=(Width/2,Height*0.45))
                self.display_surface.blit(Text_speed, rect)

            elif "Menu_Char" == self.zone["Zone"]:
                Text=self.font.render("Menu Character Selection", True, "black")
                rect=Text.get_rect(center=(Width/2,Height*0.07))
                self.display_surface.blit(Text, rect)

                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    self.character_selection+=1
                    if self.character_selection>1:
                        self.character_selection=0
                elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    self.character_selection-=1
                    if self.character_selection<0:
                        self.character_selection=1
                
                self.animation_index+=1
                image=self.Menu_character[self.character_selection][0][int(self.animation_index)%8][1]
                rect=image.get_rect(center=(Width*0.5,Height*0.45))
                self.display_surface.blit(image, rect)

            elif "User1_Char" == self.zone["Zone"]:
                Text=self.font.render("User 1 Character Selection", True, "black")
                rect=Text.get_rect(center=(Width/2,Height*0.07))
                self.display_surface.blit(Text, rect)

                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    self.User1_character_selection+=1
                    if self.User1_character_selection>1:
                        self.User1_character_selection=0
                elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    self.User1_character_selection-=1
                    if self.User1_character_selection<0:
                        self.User1_character_selection=1  
                
                Text_user1=self.font.render("Protagonist" if self.User1_character_selection == 0 else "Antagonist", True, "black")
                rect=Text_user1.get_rect(center=(Width/2,Height*0.45))
                self.display_surface.blit(Text_user1, rect)
            
            elif "User2_Char" == self.zone["Zone"]:
                Text=self.font.render("User 2 Character Selection", True, "black")
                rect=Text.get_rect(center=(Width/2,Height*0.07))
                self.display_surface.blit(Text, rect)

                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    self.User2_character_selection+=1
                    if self.User2_character_selection>1:
                        self.User2_character_selection=0
                elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    self.User2_character_selection-=1
                    if self.User2_character_selection<0:
                        self.User2_character_selection=1  
                
                Text_user2=self.font.render("Protagonist" if self.User2_character_selection == 0 else "Antagonist", True, "black")
                rect=Text_user2.get_rect(center=(Width/2,Height*0.45))
                self.display_surface.blit(Text_user2, rect)

            elif "Theme" == self.zone["Zone"]:
                Text=self.font.render("Theme Selection", True, "black")
                rect=Text.get_rect(center=(Width/2,Height*0.07))
                self.display_surface.blit(Text, rect)

                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    self.theme+=1
                    if self.theme>2:
                        self.theme=0
                elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    self.theme-=1
                    if self.theme<0:
                        self.theme=2
                
                Text_theme=self.font.render(str(Theme_mapping[self.theme]), True, "black")
                rect=Text_theme.get_rect(center=(Width/2,Height*0.45))
                self.display_surface.blit(Text_theme, rect)

        self.Interaction_exit_prompt_image=pygame.transform.scale(self.Interaction_exit_prompt_image,(Width*0.5,Height*0.6))
        rect=self.Interaction_exit_prompt_image.get_rect(center=(Width/2,Height*0.88))
        self.display_surface.blit(self.Interaction_exit_prompt_image, rect)