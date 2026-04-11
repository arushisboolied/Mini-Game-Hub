import pygame
import matplotlib as plt
import numpy as np
import os
import sys
import time
import pathlib
import subprocess
import datetime
import random
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from game import Game


class Othello(Game):

    def __init__(self, game_name="Othello", players=("Player1", "Player2"),
                 Resolution=(1280, 720), theme="medieval", Characters=(0, 1)):

        super().__init__(game_name, players, Resolution, theme, Characters)

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

    def draw_board(self):
        for y in range(8):
            for x in range(8):
                if self.Board[y][x] == -1:
                    continue

                coin = self.assets.token1 if self.Board[y][x] == 0 else self.assets.token2

                self.screen.blit(
                    coin,
                    (
                        self.assets.start[0] - self.assets.token_size[0] / 2 + self.assets.tokengap[0] * x,
                        self.assets.start[1] - self.assets.token_size[1] / 2 + self.assets.tokengap[1] * y
                    )
                )


    def is_on_board(self, x, y):
        return 0 <= x < 8 and 0 <= y < 8

    def check_valid(self, x, y, player):
        if not self.is_on_board(x, y) or self.Board[y][x] != -1:
            return False

        opponent = 1 - player

        for dx, dy in self.directions:
            nx, ny = x + dx, y + dy
            found_opponent = False

            while self.is_on_board(nx, ny) and self.Board[ny][nx] == opponent:
                nx += dx
                ny += dy
                found_opponent = True

            if found_opponent and self.is_on_board(nx, ny) and self.Board[ny][nx] == player:
                return True

        return False

    def flip_pieces(self, x, y, player):
        opponent = 1 - player

        for dx, dy in self.directions:
            nx, ny = x + dx, y + dy
            pieces_to_flip = []

            while self.is_on_board(nx, ny) and self.Board[ny][nx] == opponent:
                pieces_to_flip.append((nx, ny))
                nx += dx
                ny += dy

            if pieces_to_flip and self.is_on_board(nx, ny) and self.Board[ny][nx] == player:
                for fx, fy in pieces_to_flip:
                    self.Board[fy][fx] = player

        self.Board[y][x] = player

    def has_valid_moves(self, player):
        for y in range(8):
            for x in range(8):
                if self.check_valid(x, y, player):
                    return True
        return False

    def win_check(self):
        if np.all(self.Board != -1) or not (self.has_valid_moves(0) or self.has_valid_moves(1)):
            self.end = True


    def update_board(self):

        x, y = self.current_move
        player = self.current_player

        if self.is_on_board(x, y) and self.check_valid(x, y, player):
            self.flip_pieces(x, y, player)

            self.switch_turns()

            if not self.has_valid_moves(self.current_player):
                self.switch_turns()
                if not self.has_valid_moves(self.current_player):
                    self.end = True
                    self.running = False

            self.win_check()

        self.draw_board()


    def event_handler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_x, mouse_y = pygame.mouse.get_pos()

            y_min, y_max = self.assets.y
            x_min, x_max = self.assets.x

            if y_min <= mouse_y < y_max and x_min <= mouse_x < x_max:

                col_width = (x_max - x_min) / 8
                row_height = (y_max - y_min) / 8

                grid_x = int((mouse_x - x_min) / col_width)
                grid_y = int((mouse_y - y_min) / row_height)

                self.current_move = [grid_x, grid_y]
                self.update_board()


    def run(self):
        self.running = True

        while self.running:
            self.clock.tick(60)

            self.generate_board()
            self.display_player_names()
            self.display_game_name()
            self.display_time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    sys.exit()
                else:
                    self.event_handler(event)

            self.generate_players()

            self.draw_board()

            pygame.display.update()


if __name__ == "__main__":
    Othello(theme="medieval").run()