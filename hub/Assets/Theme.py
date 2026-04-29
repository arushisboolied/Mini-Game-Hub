import pygame
import numpy as np
import os
import sys

def path(file):
    return os.path.join(os.path.dirname(__file__), file)

def image_load(file):
    return pygame.image.load(path(file)).convert_alpha()

def image_load_scale(file, size):
    return pygame.transform.scale(image_load(file), size)


class Theme:
    def __init__(self, name, game, players):

        # if elif block used to load only necessary resources for the selected theme and game, to save memory and loading time
        #Theme specific assets
        if name == "medieval":

            #Background
            self.background=pygame.image.load(path("./Images/Connect4_medieval.png")).convert()

            #Resign button
            self.resign=image_load_scale("./Images/Timer_medieval.png",(218,120))
            self.resign_size=(218,120)
            self.resign_pos=(531,0)
            self.resign_text_pos=(640,65)

            #Text
            self.text=pygame.font.Font(path("./the-golden-blade.regular.ttf"),50)
            self.text_colour=(230,200,120)
            
            #Character positions
            self.character_1_pos, self.character_2_pos=(150,390),(990,390)

            characters=[
                            image_load_scale("./Images/Sprite0_0_medieval.png",(140,180)),
                            image_load_scale("./Images/Sprite0_1_medieval.png",(140,180)),
                            image_load_scale("./Images/Sprite1_0_medieval.png",(140,180)),
                            image_load_scale("./Images/Sprite1_1_medieval.png",(140,180)),
                        ]
            self.character0_0size, self.character0_1size=(140,180),(140,180)
            self.character1_0size, self.character1_1size=(140,180),(140,180)
            
            #Game_Name Textbox
            self.textboxsize=(400,150)
            self.frame_center=(640,635)
            
            self.game_name_center=(640,640)

            #Game specific assets
            if game == "Connect4":

                #Board
                self.boardscreen=image_load_scale("./Images/Connect4_Board_medieval.png",(600,600))
                self.boardpos,self.boardsize=(340,60),(600,600)

                #Start position of the first token and the gap between tokens (used to calculate token positions on the board)
                self.start_pos,self.tokengap=(465,210),(58.5,50.5)

                #Range of x and y coordinates for mouseclicks to be registered as valid moves (used in event handler)
                self.x,self.y=(432,843),(184,543)

                #Token size and images
                self.token_size=(55,50)
                self.token1=image_load_scale("./Images/Coin1_medieval.png",self.token_size)
                self.token2=image_load_scale("./Images/Coin2_medieval.png",self.token_size)

            elif game == "TicTacToe":

                #Board
                self.boardscreen=image_load_scale("./Images/TicTacToe_Board_medieval.png", (700, 900))
                self.boardpos,self.boardsize=(290,-60),(700,900)

                #Start position of the first token and the gap between tokens (used to calculate token positions on the board)
                self.start_pos,self.tokengap=(441,179),(44.2,35.4)

                #Range of x and y coordinates for mouseclicks to be registered as valid moves (used in event handler)
                self.x,self.y=(420,863),(165,517)

                #Token size and images
                self.token_size=(55,40)
                self.token1=image_load_scale("./Images/Cross_Medieval.png",self.token_size)
                self.token2=image_load_scale("./Images/Circle_Medieval.png",self.token_size)

            elif game == "Othello":
                #Board
                self.boardscreen=image_load_scale("./Images/Othello_Board_medieval.png",(600,600))
                self.boardpos,self.boardsize=(340,60),(600,600)

                #Start position of the first token and the gap between tokens (used to calculate token positions on the board)
                self.start_pos,self.tokengap=(464,194),(50.14,48.28)

                #Range of x and y coordinates for mouseclicks to be registered as valid moves (used in event handler)
                self.x,self.y=(445,837),(184,543)

                #Token size and images
                self.token_size=(50,50)
                self.token1=image_load_scale("./Images/Othello1_medieval.png",self.token_size)
                self.token2=image_load_scale("./Images/Othello2_medieval.png",self.token_size)
                self.token3=image_load_scale("./Images/Othello3_medieval.png",self.token_size)

                #token3 is used to indicate valid moves for the current player in Othello, it is a transparent version of the current player's token
                self.token3.set_alpha(200)

                #Positions and size for no. of pieces for each player in Othello
                self.Counter_1_center=(220,200)
                self.Counter_2_center=(1060,200)                
                self.Counter_1_size=(200,100)
                self.Counter_2_size=(200,100)

        elif name == "futuristic":
            #Background
            self.background=pygame.image.load(path("./Images/Connect4_Future.png")).convert()

            #Resign button
            self.resign=image_load_scale("./Images/Timer_Future.png",(400,120))
            self.resign_size=(600,180)
            self.resign_pos=(340,-30)
            self.resign_text_pos=(640,55)

            #Text
            self.text=pygame.font.Font(path("blade_runner.ttf"),50)
            self.text_colour=(3,216,243)

            #Character positions
            self.character_1_pos, self.character_2_pos=(145,390),(985,390)

            characters=[
                            image_load_scale("./Images/Sprite0_0_Future.png",(140,180)),
                            image_load_scale("./Images/Sprite0_1_Future.png",(140,180)),
                            image_load_scale("./Images/Sprite1_0_Future.png",(140,180)),
                            image_load_scale("./Images/Sprite1_1_Future.png",(140,180)),
                        ]
            
            self.character0_0size,self.character0_1size=(140,180),(140,180)
            self.character1_0size,self.character1_1size=(140,180),(140,180)

            #Game_Name Textbox
            self.textboxsize=(600,200)
            self.frame_center=(640,635)            
            self.game_name_center=(640,630)

            if game == "Connect4":

                #Board
                self.boardscreen=image_load_scale("./Images/Connect4_Board_Future.png",(550,600))
                self.boardpos,self.boardsize=(317,60),(650,600)

                #Start position of the first token and the gap between tokens (used to calculate token positions on the board)
                self.start_pos,self.tokengap=(444,176),(66.2,58.8)

                #Range of x and y coordinates for mouseclicks to be registered as valid moves (used in event handler)
                self.x,self.y=(407,878),(146,556)

                #Token size and images
                self.token_size=(50,50)
                self.token1=image_load_scale("./Images/Coin1_Future.png", self.token_size)
                self.token2=image_load_scale("./Images/Coin2_Future.png", self.token_size)

            elif game == "TicTacToe":

                #Board
                self.boardscreen=image_load_scale("./Images/TicTacToe_Board_Future.png", (700, 600))
                self.boardpos,self.boardsize=(290,40),(700,600)

                #Start position of the first token and the gap between tokens (used to calculate token positions on the board)
                self.start_pos,self.tokengap=(405,153),(52.3,43.8)

                #Range of x and y coordinates for mouseclicks to be registered as valid moves (used in event handler)
                self.x,self.y=(375,898),(131,566)

                #Token size and images
                self.token_size=(55,40)
                self.token1=image_load_scale("./Images/Cross_Future.png",self.token_size)
                self.token2=image_load_scale("./Images/Circle_Future.png",self.token_size)

            elif game == "Othello":
                #Board
                self.boardscreen=image_load_scale("./Images/Othello_Board_Future.png",(600,600))
                self.boardpos,self.boardsize=(340,35),(600,600)

                #Start position of the first token and the gap between tokens (used to calculate token positions on the board)
                self.start_pos,self.tokengap=(449,163),(53,52.57)

                #Range of x and y coordinates for mouseclicks to be registered as valid moves (used in event handler)
                self.x,self.y=(421,845),(140,557)

                #Token size and images
                self.token_size=(50,50)
                self.token1=image_load_scale("./Images/Othello1_Future.png",self.token_size)
                self.token2=image_load_scale("./Images/Othello2_Future.png",self.token_size)
                self.token3=image_load_scale("./Images/Othello3_Future.png",self.token_size)

                #token3 is used to indicate valid moves for the current player in Othello, it is a transparent version of the current player's token
                self.token3.set_alpha(100)

                #Positions for no. of pieces for each player in Othello
                self.Counter_1_center=(220,200)
                self.Counter_2_center=(1060,200)
                self.Counter_1_size=(300,150)
                self.Counter_2_size=(300,150)

        elif name == "dune":
            #Background
            self.background=pygame.image.load(path("./Images/Connect4_Dune.png")).convert()

            #Resign button
            self.resign=image_load_scale("./Images/Timer_Dune.png",(500,100))
            self.resign_size=(500,100)
            self.resign_pos=(390,0)
            self.resign_text_pos=(640, 58)

            #Text
            self.text= pygame.font.Font(path("./Dune Rise 400.ttf"), 40)
            self.text_colour= (233, 203, 142)

            #Character positions
            self.character_1_pos,self.character_2_pos = (165, 390), (975, 390)

            characters=[
                            image_load_scale("./Images/Sprite0_0_Dune.png", (140,180)),
                            image_load_scale("./Images/Sprite0_1_Dune.png", (140,180)),
                            image_load_scale("./Images/Sprite1_0_Dune.png", (140,180)),
                            image_load_scale("./Images/Sprite1_1_Dune.png", (140,180)),
                        ]
            self.character0_0size,self.character0_1size=(140,180),(140,180)
            self.character1_0size,self.character1_1size=(140,180),(140,180)

            #Game_Name Textbox
            self.textboxsize=(750,150)
            self.frame_center=(640,635)
            self.game_name_center=(640,630)

            if game == "Connect4":

                #Board
                self.boardscreen = image_load_scale("./Images/Connect4_Board_Dune.png", (650,650))
                self.boardpos,self.boardsize=(315,10),(650,650)

                #Start position of the first token and the gap between tokens (used to calculate token positions on the board)
                self.start_pos,self.tokengap=(455,165),(60.5,55.2)

                #Range of x and y coordinates for mouseclicks to be registered as valid moves (used in event handler)
                self.x,self.y=(420,849),(135,525)

                #Token size and images
                self.token_size=(60,60)
                self.token1=image_load_scale("./Images/Coin1_Dune.png", self.token_size)
                self.token2=image_load_scale("./Images/Coin2_Dune.png", self.token_size)

            elif game == "TicTacToe":

                #Board
                self.boardscreen=image_load_scale("./Images/TicTacToe_Board_Dune.png", (600, 600))
                self.boardpos,self.boardsize=(365,65),(550,550)

                #Start position of the first token and the gap between tokens (used to calculate token positions on the board)
                self.start_pos,self.tokengap=(440,146),(44.22,43.77)

                #Range of x and y coordinates for mouseclicks to be registered as valid moves (used in event handler)
                self.x,self.y=(420,859),(125,561)

                #Token size and images
                self.token_size=(40,40)
                self.token1=image_load_scale("./Images/Cross_Dune.png",self.token_size)
                self.token2=image_load_scale("./Images/Circle_Dune.png",self.token_size)

            elif game == "Othello":
                #Board
                self.boardscreen=image_load_scale("./Images/Othello_Board_Dune.png",(600,600))
                self.boardpos,self.boardsize=(365,60),(550,520)

                #Start position of the first token and the gap between tokens (used to calculate token positions on the board)
                self.start_pos,self.tokengap=(451,146),(54.14,49.86)

                #Range of x and y coordinates for mouseclicks to be registered as valid moves (used in event handler)
                self.x,self.y=(422,854),(123,520)

                #Token size and images
                self.token_size=(45,45)
                self.token1=image_load_scale("./Images/Othello1_Dune.png",self.token_size)
                self.token2=image_load_scale("./Images/Othello2_Dune.png",self.token_size)
                self.token3=image_load_scale("./Images/Othello3_Dune.png",self.token_size)

                #token3 is used to indicate valid moves for the current player in Othello, it is a transparent version of the current player's token
                self.token3.set_alpha(200)

                #Positions for no. of pieces for each player in Othello
                self.Counter_1_center=(220,200)
                self.Counter_2_center=(1060,200)
                self.Counter_1_size=(300,100)
                self.Counter_2_size=(300,100)

        #Common things for all themes and games

        #Character assets stored in a tuple of tuples for easy access in game files
        self.character=((characters[0],characters[1]),(characters[2],characters[3]))

        #Player name text and token positions 
        p1center,p2center=(220,280),(1060,280)
        self.Player1=self.text.render(str(players[0]),True,(255,255,255))
        self.text_rect1=self.Player1.get_rect(center=p1center)
        self.tokenloc1=(p1center[0]-55/2,p1center[1]+25)

        self.Player2=self.text.render(str(players[1]),True,(255,255,255))
        self.text_rect2=self.Player2.get_rect(center=p2center)
        self.tokenloc2=(p2center[0]-55/2,p2center[1]+25)

        #Game name text
        self.game_name=self.text.render(str(game),True,self.text_colour)
        self.game_name_rect=self.game_name.get_rect(center=self.game_name_center)