import pygame
import sys,os

sys.path.append(os.path.join(os.path.dirname(__file__), 'games/'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'Menu_Assets/Codes/'))

from Level import Level
from Support import *

from tictactoe import TicTacToe
from othello import Othello
from connect4 import Connect4

##### Takes in Users as arguements #####
User1=sys.argv[1]
User2=sys.argv[2]

class Menu:

    ##### Setting up a resizable pygame display #####
    def __init__(self,Resolution=(1280,720)):
        pygame.init()
        pygame.font.init()
        self.Resolution=Resolution
        self.character=0
        self.screen=pygame.display.set_mode(Resolution,pygame.RESIZABLE)        # Resizability
        self.clock=pygame.time.Clock()                                          # Controls frame rate
        self.level=Level()                                                      # Loads the menu level (UI, Player, Settings etc.)
    
    ##### Handle Keyboard Inputs - E to interact #####
    def event_handler(self,event):
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_e and self.level.player.check_zones():
                self.level.settings_toggle()

    ##### Main Game Loop #####
    def run(self):
        running=True
        
        while running:
            self.clock.tick(60) #60FPS 
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                    pygame.quit()
                    sys.exit()
                else:
                    self.event_handler(event)

            ##### Clear Screen #####
            self.screen.fill("black")

            ##### Run the current menu level #####
            self.level.run()

            ##### To check if a game has been selected #####
            if self.level.settings.current_game!=None:
                
                ##### Launch TicTacToe #####
                if self.level.settings.current_game=="Tictactoe":
                    TicTacToe(theme=Theme_mapping[self.level.game_theme],Characters=(self.level.User1_selection,self.level.User2_selection),players=(User1,User2)).run()

                ##### Launch Connect4 #####
                elif self.level.settings.current_game=="Connect4":
                    Connect4(theme=Theme_mapping[self.level.game_theme],Characters=(self.level.User1_selection,self.level.User2_selection),players=(User1,User2)).run()

                ##### Launch Othello #####
                elif self.level.settings.current_game=="Othello":
                    Othello(theme=Theme_mapping[self.level.game_theme],Characters=(self.level.User1_selection,self.level.User2_selection),players=(User1,User2)).run()

                ##### Leaderboard (After game ends) #####
                elif self.level.settings.current_game=="Leaderboard":
                    print("Leaderboard called")
                
                ##### Exit Game #####
                elif self.level.settings.current_game=="Exit":
                    running=False
                    pygame.quit()
                    sys.exit()

                ##### After game ends, reset selections #####
                self.level.settings.current_game=None
                self.level.game_paused=False

            ##### Independent trigger for leaderboard #####
            if self.level.call_leaderboard:
                print("Leaderboard called")
                self.level.call_leaderboard=False
            pygame.display.update()
            

##### Enjoy :) #####
Menu().run() 