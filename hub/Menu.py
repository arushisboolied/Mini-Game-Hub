import pygame
import sys,os

sys.path.append(os.path.join(os.path.dirname(__file__), 'games/'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'Menu_Assets/Codes/'))

from Level import Level
from Support import *

from tictactoe import TicTacToe
from othello import Othello
from connect4 import Connect4

User1=sys.argv[1]
User2=sys.argv[2]

class Menu:
    def __init__(self,Resolution=(1280,720)):
        pygame.init()
        pygame.font.init()
        self.Resolution=Resolution
        self.character=0
        self.screen=pygame.display.set_mode(Resolution,pygame.RESIZABLE)
        self.clock=pygame.time.Clock()
        self.level=Level()
        

    def event_handler(self,event):
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_e and self.level.player.check_zones():
                self.level.settings_toggle()

    def run(self):
        running=True
        
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                    pygame.quit()
                    sys.exit()
                else:
                    self.event_handler(event)

            self.screen.fill("black")
            self.level.run()
            if self.level.settings.current_game!=None:

                if self.level.settings.current_game=="Tictactoe":
                    TicTacToe(theme=Theme_mapping[self.level.game_theme],Characters=(self.level.User1_selection,self.level.User2_selection),players=(User1,User2)).run()

                elif self.level.settings.current_game=="Connect4":
                    Connect4(theme=Theme_mapping[self.level.game_theme],Characters=(self.level.User1_selection,self.level.User2_selection),players=(User1,User2)).run()
                    
                elif self.level.settings.current_game=="Othello":
                    Othello(theme=Theme_mapping[self.level.game_theme],Characters=(self.level.User1_selection,self.level.User2_selection),players=(User1,User2)).run()

                elif self.level.settings.current_game=="Leaderboard":
                    print("Leaderboard called")
                elif self.level.settings.current_game=="Exit":
                    running=False
                    pygame.quit()
                    sys.exit()

                self.level.settings.current_game=None
                self.level.game_paused=False

            if self.level.call_leaderboard:
                print("Leaderboard called")
                self.level.call_leaderboard=False
            pygame.display.update()
            

Menu().run()