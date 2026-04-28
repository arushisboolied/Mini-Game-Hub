import pygame
import os,sys

from Support import *

class Settings:
    def __init__(self):
        self.display_surface=pygame.display.get_surface()
        
        self.image=pygame.image.load(Character_Selection_image_path).convert_alpha()        
        self.Interaction_exit_prompt_image=pygame.image.load(Interaction_Exit_image_path).convert_alpha()
        self.text_banner_image=pygame.image.load(Settings_Text_image_path).convert_alpha()
        self.game_title_image=pygame.image.load(Game_Title_image_path).convert_alpha()
        self.tictactoe_rules_image=pygame.image.load(TicTacToe_Rules_image_path).convert_alpha()
        self.connect4_rules_image=pygame.image.load(Connect4_Rules_image_path).convert_alpha()
        self.othello_rules_image=pygame.image.load(Othello_Rules_image_path).convert_alpha()
        self.leaderboard_text=pygame.image.load(Leaderboard_text_path).convert_alpha()
        pygame.font.init()
        self.font=pygame.font.Font(Text_font_path, 30)

        self.zone=None
        self.player_speed=None
        self.character_selection=None
        self.Menu_character=None
        self.theme=None
        self.animation_index=0

        self.current_game=None
    
    def run(self):

        keys=pygame.key.get_just_pressed()

        Width=self.display_surface.get_size()[0]
        Height=self.display_surface.get_size()[1]

        if "Char" in self.zone["Zone"] or "Theme" in self.zone["Zone"] or "Speed" in self.zone["Zone"]:

            self.image=pygame.transform.scale(self.image,(Width*0.8,Height*0.8))

            rect=self.image.get_rect(center=(Width/2,Height*0.45))
            self.display_surface.blit(self.image,rect) 

            self.text_banner_image=pygame.transform.scale(self.text_banner_image,(Width*1.035,Height*0.2))
            rect=self.text_banner_image.get_rect(center=(Width/2,Height*0.09))
            self.display_surface.blit(self.text_banner_image, rect)

            if self.zone["Zone"]=="Speed":
                Text=self.font.render("Speed of Menu Character", True, "black")
                rect=Text.get_rect(center=(Width/2,Height*0.07))
                self.display_surface.blit(Text, rect)

                
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    self.player_speed+=1
                elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    self.player_speed-=1
                
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
                
                self.animation_index+=0.15
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

        elif "game" in self.zone["Zone"]:
            self.game_title_image=pygame.transform.scale(self.game_title_image,(Width*0.8,Height*0.4))
            rect=self.game_title_image.get_rect(center=(Width/2,Height*0.09))
            self.display_surface.blit(self.game_title_image, rect)

            if "Tictactoe" in self.zone["Zone"]:
                Text=self.font.render("Tictactoe", True, "black")
                rect=Text.get_rect(center=(Width/2,Height*0.07))
                self.display_surface.blit(Text, rect)

                self.tictactoe_rules_image=pygame.transform.scale(self.tictactoe_rules_image,(Width*1.3,Height*1.3))
                rect=self.tictactoe_rules_image.get_rect(center=(Width/2,Height*0.41))
                self.display_surface.blit(self.tictactoe_rules_image, rect)    

                if keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER]:
                    self.current_game="Tictactoe"            
                                                        
            elif "Connect4" in self.zone["Zone"]:
                Text=self.font.render("Connect 4", True, "black")
                rect=Text.get_rect(center=(Width/2,Height*0.07))
                self.display_surface.blit(Text, rect)

                self.connect4_rules_image=pygame.transform.scale(self.connect4_rules_image,(Width*1.3,Height*1.3))
                rect=self.connect4_rules_image.get_rect(center=(Width/2,Height*0.41))
                self.display_surface.blit(self.connect4_rules_image, rect) 

                if keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER]:
                    self.current_game="Connect4"  
    
            elif "Othello" in self.zone["Zone"]:
                Text=self.font.render("Othello", True, "black")
                rect=Text.get_rect(center=(Width/2,Height*0.07))
                self.display_surface.blit(Text, rect)

                self.othello_rules_image=pygame.transform.scale(self.othello_rules_image,(Width*1.3,Height*1.3))
                rect=self.othello_rules_image.get_rect(center=(Width/2,Height*0.41))
                self.display_surface.blit(self.othello_rules_image, rect) 

                if keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER]:
                    self.current_game="Othello"

        elif "Leaderboard" in self.zone["Zone"]:
            self.game_title_image=pygame.transform.scale(self.game_title_image,(Width*0.8,Height*0.4))
            rect=self.game_title_image.get_rect(center=(Width/2,Height*0.09))
            self.display_surface.blit(self.game_title_image, rect)

            Text=self.font.render("Leaderboard and Exit", True, "black")
            rect=Text.get_rect(center=(Width/2,Height*0.07))
            self.display_surface.blit(Text, rect)

            self.leaderboard_text=pygame.transform.scale(self.leaderboard_text,(Width*1.3,Height*1.3))
            rect=self.leaderboard_text.get_rect(center=(Width/2,Height*0.41))
            self.display_surface.blit(self.leaderboard_text, rect) 

            if keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER]:
                self.current_game="Leaderboard"
            elif keys[pygame.K_ESCAPE]:
                self.current_game="Exit"





        self.Interaction_exit_prompt_image=pygame.transform.scale(self.Interaction_exit_prompt_image,(Width*0.5,Height*0.6))
        rect=self.Interaction_exit_prompt_image.get_rect(center=(Width/2,Height*0.88))
        self.display_surface.blit(self.Interaction_exit_prompt_image, rect)