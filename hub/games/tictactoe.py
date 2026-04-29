import pygame
import numpy as np
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from game import Game

class TicTacToe(Game):

    ####################### INITIALIZATION OF THE BOARD #######################

    def __init__(self,game_name="TicTacToe", players=("Player1","Player2"), theme="medieval", Characters=(0,1)):
        super().__init__(game_name, Resolution=(1280, 720), players=players, theme=theme, Characters=Characters)
        self.Board=np.ones(100,dtype=int).reshape(10,10)*(-1)



    ####################### CHECK FOR WIN CONDITIONS #######################
    
    def win_check(self):

        ##### READ THE LAST MOVE #####

        x,y=self.current_move

        ##### CHECK FOR 5 IN A ROW COLUMN DIAGONAL OR ANTI DIAGONAL #####

        checker=np.ones(5,dtype=int)*(self.current_player)

        if (self.Board[x,0:5]==checker).all() or (self.Board[x,1:6]==checker).all() or (self.Board[x,2:7]==checker).all() or (self.Board[x,3:8]==checker).all() or (self.Board[x,4:9]==checker).all() or (self.Board[x,5:10]==checker).all():
            return True
        if (self.Board[0:5,y]==checker).all() or (self.Board[1:6,y]==checker).all() or (self.Board[2:7,y]==checker).all() or (self.Board[3:8,y]==checker).all() or (self.Board[4:9,y]==checker).all() or (self.Board[5:10,y]==checker).all():
            return True
        Diag1=np.diagonal(self.Board,offset=y-x)
        Board2=np.fliplr(self.Board)
        Diag2=np.diagonal(Board2,offset= 9-x-y)
        if (len(Diag1[0:5])==5 and (Diag1[0:5]==checker).all()) or (len(Diag1[1:6])==5 and (Diag1[1:6]==checker).all()) or (len(Diag1[2:7])==5 and (Diag1[2:7]==checker).all()) or (len(Diag1[3:8])==5 and (Diag1[3:8]==checker).all()) or (len(Diag1[4:9])==5 and (Diag1[4:9]==checker).all()) or (len(Diag1[5:10])==5 and (Diag1[5:10]==checker).all()) or (len(Diag2[0:5])==5 and (Diag2[0:5]==checker).all()) or (len(Diag2[1:6])==5 and (Diag2[1:6]==checker).all()) or (len(Diag2[2:7])==5 and (Diag2[2:7]==checker).all()) or (len(Diag2[3:8])==5 and (Diag2[3:8]==checker).all()) or (len(Diag2[4:9])==5 and (Diag2[4:9]==checker).all()) or (len(Diag2[5:10])==5 and (Diag2[5:10]==checker).all()):
            return True
        
        return False
    


    ####################### UPDATE THE BOARD #######################

    def update_board(self):

        x, y = self.current_move
        if self.Board[x, y] == -1:
            self.Board[x, y] = self.current_player
            self.redraw_tokens()


            if self.win_check():
                self.running = False

            elif not (self.Board == -1).any():
                self.running = False
                self.tie = True

            else:
                self.switch_turns()
        


    ####################### REGISTER USER ACTIONS #######################

    def event_handler(self, event):

        ##### REGISTERS A CLICK AND LOCATION OF THE CLICK TO UPDATE THE BOARD #####

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            ##### BOARD BOUNDARIES TO NOT CONSIDER OUT OF BOUNDS CLICKS #####
            print(mouse_x, mouse_y)
            y_min, y_max = self.assets.y
            x_min, x_max = self.assets.x

            y_min=y_min*self.Resolution[1]/720
            y_max=y_max*self.Resolution[1]/720
            x_min, x_max = self.assets.x
            x_min=x_min*self.Resolution[0]/1280
            x_max=x_max*self.Resolution[0]/1280

            ##### CHECKING TARGET CELL #####

            if y_min <= mouse_y < y_max and x_min <= mouse_x < x_max:
                col_width = (x_max - x_min) / 10
                row_height = (y_max - y_min) / 10

                grid_x = int((mouse_x - x_min) / col_width)
                grid_y = int((mouse_y - y_min) / row_height)

                self.current_move = [grid_x, grid_y]
                self.update_board()
                 
if __name__=="__main__":
    TicTacToe(theme="dune").run()          