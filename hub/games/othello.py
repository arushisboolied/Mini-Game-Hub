import pygame
import numpy as np
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from game import Game



class Othello(Game):

    #################### INITIALIZATION OF BOARD ####################
    def __init__(self, game_name="Othello", players=("Player1", "Player2"), theme="medieval", Characters=(0, 1)):

        ##### Initialize the base Game class with the provided parameters #####
        super().__init__(game_name, players=players, theme=theme, Characters=Characters)

        ##### Create an 8x8 board initialized with -1 (indicating empty spaces) #####
        self.Board = np.full((8, 8), -1, dtype=int)

        ##### Set up the initial four pieces in the center of the board #####
        self.Board[3][3] = 0
        self.Board[3][4] = 1
        self.Board[4][3] = 1
        self.Board[4][4] = 0

        ##### Initialize game state variables #####
        self.end = False

        ##### Define the 8 possible directions for checking valid moves and flipping pieces #####
        self.directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        ##### Stores last move played #####
        self.current_move = [-1, -1]

        ##### Initialize board update #####
        self.update_board()



    #################### LEGAL MOVE CHECKER ####################

    def is_on_board(self, x, y):

        ##### Check if the given coordinates (x, y) are within the bounds of the 8x8 board #####
        return 0 <= x < 8 and 0 <= y < 8

    def check_valid(self, x, y, player):

        ##### Move must be on an empty cell of the board #####
        if self.Board[x][y] != -1:
            return False
        
        opponent = 1 - player

        ##### Check all directions #####
        for dx, dy in self.directions:
            nx, ny = x + dx, y + dy
            found_opponent = False

            ##### Traverse in direction while we find opponent pieces #####
            while self.is_on_board(nx, ny) and self.Board[nx][ny] == opponent:
                nx += dx
                ny += dy
                found_opponent = True
            
            ##### If we found at least one opponent piece and ended on a player's piece, it's a valid move(sandwiched pieces) #####
            if found_opponent and self.is_on_board(nx, ny) and self.Board[nx][ny] == player:
                return True

        return False
    

    
    #################### ALL VALID MOVES FOR CURRENT PLAYER ####################
    def valid_moves(self, player):
        moves = []

        ##### Scale token size for screen resolution ##### 
        token_size=list(np.array(self.assets.token_size)*np.array(self.Resolution)/np.array([1280,720]))

        ##### Draw board #####
        self.generate_board()

        ##### Check every cell on the board for valid moves for the current player #####
        for y in range(8):
            for x in range(8):
                if self.check_valid(x, y, player):
                    coin=pygame.transform.scale(self.assets.token3,token_size)
                    self.screen.blit(coin,(self.assets.start_pos[0]*self.Resolution[0]/1280-self.assets.token_size[0]*self.Resolution[0]/2560+self.assets.tokengap[0]*x*self.Resolution[0]/1280,self.assets.start_pos[1]*self.Resolution[1]/720-self.assets.token_size[1]*self.Resolution[1]/720/2+self.assets.tokengap[1]*y*self.Resolution[1]/720))
    
    def redraw_tokens(self):

        ##### Show valid moves for the current player #####
        self.valid_moves(self.current_player)

        ##### Draw the current state of the board with tokens #####
        super().redraw_tokens()
        
        ##### Update the piece counters on the screen #####
        self.counter()
        
    #################### FLIP OPPONENT'S PIECES ####################
    def flip_pieces(self, x, y, player):
        opponent = 1 - player

        ##### Check all 8 directions for opponent pieces to flip #####
        for dx, dy in self.directions:
            nx, ny = x + dx, y + dy
            pieces_to_flip = []

            ##### Traverse in the direction while we find opponent pieces #####
            while self.is_on_board(nx, ny) and self.Board[nx][ny] == opponent:
                pieces_to_flip.append((nx, ny))
                nx += dx
                ny += dy

            ##### If we found opponent pieces and ended on a player's piece, flip all the opponent pieces in between #####
            if pieces_to_flip and self.is_on_board(nx, ny) and self.Board[nx][ny] == player:
                for fx, fy in pieces_to_flip:
                    self.Board[fx][fy] = player

        ##### Place the player's piece on the board at the chosen location #####
        self.Board[x][y] = player



    #################### CHECK FOR WIN CONDITIONS ####################
    def has_valid_moves(self, player):
        for y in range(8):
            for x in range(8):
                if self.check_valid(x, y, player):
                    return True
        return False

    def win_check(self):

        ##### Check if the board is full or if neither player has valid moves, which would end the game #####
        if np.all(self.Board != -1) or not (self.has_valid_moves(0) or self.has_valid_moves(1)):
            self.end = True




    #################### UPDATE BOARD AFTER A MOVE ####################
    def update_board(self):

        x, y = self.current_move
        player = self.current_player

        ##### If the move is valid, flip the opponent's pieces and update the board state #####
        if self.check_valid(x, y, player):
            self.flip_pieces(x, y, player)

            ##### Switch turns to the other player #####
            self.switch_turns()

            ##### Check if the next player has any valid moves; if not, switch back to the original player. If neither player has valid moves, end the game in a tie. #####
            if not self.has_valid_moves(self.current_player):
                self.switch_turns()
                if not self.has_valid_moves(self.current_player):
                    self.tie = True
                    self.end = True
                    self.running = False

            ##### After updating the board and switching turns, check for win conditions #####
            self.win_check()



    #################### HANDLE MOUSE CLICK EVENTS ####################
    def event_handler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_x, mouse_y = pygame.mouse.get_pos()

            ##### Scale the board coordinates based on the screen resolution #####
            y_min, y_max = self.assets.y
            x_min, x_max = self.assets.x

            y_min=y_min*self.Resolution[1]/720
            y_max=y_max*self.Resolution[1]/720
            x_min, x_max = self.assets.x
            x_min=x_min*self.Resolution[0]/1280
            x_max=x_max*self.Resolution[0]/1280


            ##### Check if the mouse click is within the bounds of the board #####
            if y_min <= mouse_y < y_max and x_min <= mouse_x < x_max:
                
                ##### Calculate which grid cell was clicked based on the mouse position and the scaled board coordinates #####
                col_width = (x_max - x_min) / 8
                row_height = (y_max - y_min) / 8

                grid_x = int((mouse_x - x_min) / col_width)
                grid_y = int((mouse_y - y_min) / row_height)

                ##### Store move and update board #####
                self.current_move = [grid_x, grid_y]
                self.update_board()
    


    #################### COUNTER DISPLAY FUNCTION ####################
    def counter(self):

        ##### Count the number of pieces for each player on the board #####
        counter1=str(np.sum(self.Board==0))
        counter2=str(np.sum(self.Board==1))

        ##### Scale the timer box for the current screen resolution and position it for the players' counter #####
        box=pygame.transform.scale(self.assets.resign,(self.assets.Counter_1_size[0]*self.Resolution[0]/1280,self.assets.Counter_1_size[1]*self.Resolution[1]/720))
        rect=box.get_rect()
        Counter1center=list(np.array(self.assets.Counter_1_center)*np.array(self.Resolution)/np.array([1280,720]))
        rect.center=Counter1center
        counter1=self.assets.text.render(counter1,True,(255,255,255))
        text_center=(rect.center[0],rect.center[1]+5)
        text_rect=counter1.get_rect(center=text_center)
        self.screen.blit(box,rect)        
        self.screen.blit(counter1,text_rect)

        Counter2center=list(np.array(self.assets.Counter_2_center)*np.array(self.Resolution)/np.array([1280,720]))
        rect.center=Counter2center
        counter2=self.assets.text.render(counter2,True,(255,255,255))
        text_center=(rect.center[0],rect.center[1]+5)
        text_rect=counter2.get_rect(center=text_center)
        self.screen.blit(box,rect)        
        self.screen.blit(counter2,text_rect)

#Testing
if __name__ == "__main__":
    Othello(theme="dune").run()