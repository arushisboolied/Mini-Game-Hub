import pygame
import numpy as np
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from game import Game



class Othello(Game):

    #################### INITIALIZATION OF BOARD ####################
    def __init__(self, game_name="Othello", players=("Player1", "Player2"), theme="medieval", Characters=(0, 1)):

        super().__init__(game_name, players, theme, Characters)

        self.Board = np.full((8, 8), -1, dtype=int)

        self.Board[3][3] = 0
        self.Board[3][4] = 1
        self.Board[4][3] = 1
        self.Board[4][4] = 0

        self.end = False

        self.directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        self.current_move = [-1, -1]
        self.update_board()



    #################### LEGAL MOVE CHECKER ####################

    def is_on_board(self, x, y):
        return 0 <= x < 8 and 0 <= y < 8

    def check_valid(self, x, y, player):
        if self.Board[x][y] != -1:
            return False
        
        opponent = 1 - player

        for dx, dy in self.directions:
            nx, ny = x + dx, y + dy
            found_opponent = False

            while self.is_on_board(nx, ny) and self.Board[nx][ny] == opponent:
                nx += dx
                ny += dy
                found_opponent = True

            if found_opponent and self.is_on_board(nx, ny) and self.Board[nx][ny] == player:
                return True

        return False
    

    
    #################### ALL VALID MOVES FOR CURRENT PLAYER ####################
    def valid_moves(self, player):
        moves = []
        token_size=list(np.array(self.assets.token_size)*np.array(self.Resolution)/np.array([1280,720]))
        self.generate_board()
        for y in range(8):
            for x in range(8):
                if self.check_valid(x, y, player):
                    coin=pygame.transform.scale(self.assets.token3,token_size)
                    self.screen.blit(coin,(self.assets.start[0]*self.Resolution[0]/1280-self.assets.token_size[0]*self.Resolution[0]/2560+self.assets.tokengap[0]*x*self.Resolution[0]/1280,self.assets.start[1]*self.Resolution[1]/720-self.assets.token_size[1]*self.Resolution[1]/720/2+self.assets.tokengap[1]*y*self.Resolution[1]/720))
    
    def redraw_tokens(self):
        self.valid_moves(self.current_player)
        super().redraw_tokens()
        
        self.counter()
        
    #################### FLIP OPPONENT'S PIECES ####################
    def flip_pieces(self, x, y, player):
        opponent = 1 - player

        for dx, dy in self.directions:
            nx, ny = x + dx, y + dy
            pieces_to_flip = []

            while self.is_on_board(nx, ny) and self.Board[nx][ny] == opponent:
                pieces_to_flip.append((nx, ny))
                nx += dx
                ny += dy

            if pieces_to_flip and self.is_on_board(nx, ny) and self.Board[nx][ny] == player:
                for fx, fy in pieces_to_flip:
                    self.Board[fx][fy] = player

        self.Board[x][y] = player



    #################### CHECK FOR WIN CONDITIONS ####################
    def has_valid_moves(self, player):
        for y in range(8):
            for x in range(8):
                if self.check_valid(x, y, player):
                    return True
        return False

    def win_check(self):
        if np.all(self.Board != -1) or not (self.has_valid_moves(0) or self.has_valid_moves(1)):
            self.end = True




    #################### UPDATE BOARD AFTER A MOVE ####################
    def update_board(self):

        x, y = self.current_move
        player = self.current_player

        if self.check_valid(x, y, player):
            self.flip_pieces(x, y, player)

            self.switch_turns()

            if not self.has_valid_moves(self.current_player):
                self.switch_turns()
                if not self.has_valid_moves(self.current_player):
                    self.tie = True
                    self.end = True
                    self.running = False

            self.win_check()



    #################### HANDLE MOUSE CLICK EVENTS ####################
    def event_handler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_x, mouse_y = pygame.mouse.get_pos()

            y_min, y_max = self.assets.y
            x_min, x_max = self.assets.x

            y_min=y_min*self.Resolution[1]/720
            y_max=y_max*self.Resolution[1]/720
            x_min, x_max = self.assets.x
            x_min=x_min*self.Resolution[0]/1280
            x_max=x_max*self.Resolution[0]/1280

            if y_min <= mouse_y < y_max and x_min <= mouse_x < x_max:

                col_width = (x_max - x_min) / 8
                row_height = (y_max - y_min) / 8

                grid_x = int((mouse_x - x_min) / col_width)
                grid_y = int((mouse_y - y_min) / row_height)

                self.current_move = [grid_x, grid_y]
                self.update_board()
    


    #################### COUNTER DISPLAY FUNCTION ####################
    def counter(self):
        counter1=str(np.sum(self.Board==1))
        counter2=str(np.sum(self.Board==0))
        box=pygame.transform.scale(self.assets.timer,(200*self.Resolution[0]/1280,100*self.Resolution[1]/720))
        rect=box.get_rect()
        Counter1center=list(np.array(self.assets.Counter1center)*np.array(self.Resolution)/np.array([1280,720]))
        rect.center=Counter1center
        counter1=self.assets.text.render(counter1,True,(255,255,255))
        text_center=(rect.center[0],rect.center[1]+5)
        text_rect=counter1.get_rect(center=text_center)
        self.screen.blit(box,rect)        
        self.screen.blit(counter1,text_rect)

        Counter2center=list(np.array(self.assets.Counter2center)*np.array(self.Resolution)/np.array([1280,720]))
        rect.center=Counter2center
        counter1=self.assets.text.render(counter2,True,(255,255,255))
        text_center=(rect.center[0],rect.center[1]+5)
        text_rect=counter1.get_rect(center=text_center)
        self.screen.blit(box,rect)        
        self.screen.blit(counter1,text_rect)

if __name__ == "__main__":
    Othello(theme="medieval").run()