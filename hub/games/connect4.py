import pygame
import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from game import Game

class Connect4(Game):

    def __init__(self,game_name="Connect4", players=("Mohit","Arush"), theme="medieval", Characters=(0,0)):

        super().__init__(game_name,Resolution=(1280,720),players=players,theme=theme,Characters=Characters)

        ##### Initialize the board as a 7x7 grid with empty cells represented by -1 #####
        self.Board=np.ones(49,dtype=int).reshape(7,7)*(-1)


    ####################### CHECK FOR WIN CONDITIONS #######################

    def win_check(self):

        ##### Read the last move #####
        x,y=self.current_move

        ##### Create a checker array of 4 elements for comparison #####
        checker=np.ones(4,dtype=int)*(self.current_player)

        ##### Check for 4 in a row horizontally #####
        if (self.Board[x,0:4]==checker).all() or (self.Board[x,1:5]==checker).all() or (self.Board[x,2:6]==checker).all() or (self.Board[x,3:7]==checker).all():
            return True

        ##### Check for 4 in a column #####
        if (self.Board[0:4,y]==checker).all() or (self.Board[1:5,y]==checker).all() or (self.Board[2:6,y]==checker).all() or (self.Board[3:7,y]==checker).all():
            return True
        
        ##### Extract diagonals #####
        Diag1=np.diagonal(self.Board,offset=y-x)
        Board2=np.fliplr(self.Board)
        Diag2=np.diagonal(Board2,offset=6-x-y)

        ##### Check for 4 in diagonals and anti-diagonals #####
        if (len(Diag1[0:4])==4 and (Diag1[0:4]==checker).all()) or (len(Diag1[1:5])==4 and (Diag1[1:5]==checker).all()) or (len(Diag1[2:6])==4 and (Diag1[2:6]==checker).all()) or (len(Diag1[3:7])==4 and (Diag1[3:7]==checker).all()) or (len(Diag2[0:4])==4 and (Diag2[0:4]==checker).all()) or (len(Diag2[1:5])==4 and (Diag2[1:5]==checker).all()) or (len(Diag2[2:6])==4 and (Diag2[2:6]==checker).all()) or (len(Diag2[3:7])==4 and (Diag2[3:7]==checker).all()):
            return True
        
        return False
    

    ####################### UPDATE THE BOARD #######################

    def update_board(self):

        ##### Get the selected column #####
        x=self.current_move[0]

        ##### Extract the column #####
        col = self.Board[x, :]

        ##### Find empty cells in the column #####
        empty = np.where(col == -1)[0]

        ##### If the column is not full #####
        if empty.size > 0:

            ##### Place the token in the lowest empty position #####
            self.Board[x, empty[-1]] = self.current_player

            ##### Update the move with actual row position #####
            self.current_move[1] = empty[-1]

            ##### Redraw tokens on the board #####
            self.redraw_tokens()

            ##### Create an empty board checker for tie condition #####
            Checker=np.ones(49,dtype="int").reshape(7,7)*(-1)
                
            ##### Check for win #####
            if self.win_check():
                self.running=False

            ##### Check for tie #####
            elif not ((self.Board==Checker).any()):
                self.running=False
                self.tie=True

            ##### Otherwise switch turns #####
            else:
                self.switch_turns()
        
    
    ####################### HANDLE USER INPUT #######################

    def event_handler(self, event):

        ##### Detect mouse click #####
        if event.type==pygame.MOUSEBUTTONDOWN:

            ##### Get mouse position #####
            self.current_move=list(pygame.mouse.get_pos())
            x,y=self.current_move
            y_min,y_max=self.assets.y
            y_min=y_min*self.Resolution[1]/720
            y_max=y_max*self.Resolution[1]/720

            x_min, x_max = self.assets.x
            x_min=x_min*self.Resolution[0]/1280
            x_max=x_max*self.Resolution[0]/1280

            ##### Check if click is inside the board #####
            if y_min <= y < y_max and x_min <= x < x_max:

                ##### Determine which column was clicked #####
                col_width = (x_max - x_min) / 7
                self.current_move[0] = int((x - x_min) / col_width)

                ##### Update the board #####
                self.update_board()
                 

if __name__=="__main__":
    Connect4(theme="medieval").run()
