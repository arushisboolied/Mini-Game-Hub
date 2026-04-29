import pygame
import os
import sys
import subprocess


HERE = os.path.dirname(os.path.abspath(__file__))
COLUMNS = ["TIC TAC TOE","CONNECT 4","OTHELLO","ALL GAMES"]
ROWS = ["WINS","LOSSES","W/L RATIO"]
KEYS = ["1 1", "1 2", "1 3", "2 1", "2 2", "2 3", "3 1", "3 2", "3 3", "4 1", "4 2", "4 3"]


class Game_Over:
    def __init__(self, condition, winner, loser, game_name, history_csv:str="history.csv", leaderboard_csv:str="leaderboard.csv", resolution=(1280, 720)):
        self.condition = condition
        self.winner = winner
        self.loser = loser
        self.game_name = game_name
        self.history_csv = history_csv
        self.leaderboard_csv = leaderboard_csv
        self.W, self.H = resolution
        self.cells = []
        self.selection = None

        if not pygame.get_init():
            pygame.init()
            pygame.font.init()

        self.screen = pygame.display.set_mode((self.W, self.H), pygame.RESIZABLE)
        pygame.display.set_caption("GAME OVER")
        self.clock  = pygame.time.Clock()
        self.load_assets()

    def load_assets(self):
        self.background = pygame.image.load(os.path.join(HERE, "Assets/Game_Over/Background.png"))
        f = os.path.join(HERE, "Assets/Game_Over/Fonts.ttf")
        self.f_message = pygame.font.Font(f, 25)
        self.f_header = pygame.font.Font(f, 18)
        self.f_cell = pygame.font.Font(f, 21)
        self.f_button = pygame.font.Font(f, 22)
        self.f_hint = pygame.font.Font(f, 14)

    def wraptext(self, font, text, max_w):
        words, lines, line = text.split(), [], ""
        for w in words:
            t = (line + " " + w).strip()
            if font.size(t)[0] <= max_w:
                line = t
            else:
                if line: lines.append(line)
                line = w
        if line: lines.append(line)
        return lines
        
    def draw(self):
        self.screen.blit(pygame.transform.scale(self.background, (self.W, self.H)), (0, 0))
        bubble = pygame.Rect(0.20*self.W, 0.04*self.H, 0.77*self.W, 0.67*self.H)
        mx, my = pygame.mouse.get_pos()

        message_height = bubble.height*0.3
        message_pad = 32
        
        if self.condition:
            if self.condition == "win":
                message = f"Congratulations {self.winner}! You have won the game. Better luck next time, {self.loser}!"
            elif self.condition == "draw":
                message = f"It's a draw between {self.winner} and {self.loser}! Well played to both of you!"
        else:
            message = f"Choose Sort Criterion for the Leaderboard"
        
        lines = self.wraptext(self.f_message, message, bubble.width - 2*message_pad)
        line_height = self.f_message.get_linesize()
        total_text_height = line_height * len(lines)
        start_y = bubble.y + (message_height - total_text_height) // 2

        for line in lines:
            self.screen.blit(self.f_message.render(line, True, (10,10,10)), (bubble.x + message_pad, start_y))
            start_y += line_height
            
        pygame.draw.line(self.screen, (160,155,145), (bubble.x+20, bubble.y+message_height), (bubble.x+bubble.width-20, bubble.y+message_height), 1)

        grid_x = bubble.x + 12
        grid_y = bubble.y + message_height + 10
        grid_width = bubble.width - 24
        grid_height = bubble.bottom - grid_y - 10

        header_height   = 28
        cell_width = grid_width // 4
        cell_height  = (grid_height - header_height) // 3
        self.screen.blit(self.f_hint.render("Sort leaderboard by:", True, (80,80,80)), (grid_x + 4, grid_y))

        for i, col in enumerate(COLUMNS):
            cell_x = grid_x + i*cell_width + cell_width//2

            cell_header = self.f_header.render(col, True, (10,10,10))
            self.screen.blit(cell_header, cell_header.get_rect(center=(cell_x, grid_y + header_height // 2 + 8)))

            pygame.draw.line(self.screen, (0,0,0), (grid_x + i*cell_width + 8, grid_y + header_height + 4), (grid_x + (i + 1)*cell_width - 9, grid_y + header_height + 4), 1)

            for j, row in enumerate(ROWS):
                idx = i*3 + j

                row_x = grid_x + i*cell_width + 6
                row_y = grid_y + header_height + 6 + j*cell_height
                row_width = cell_width - 12
                row_height = cell_height - 8
                rect = pygame.Rect(row_x, row_y, row_width, row_height)
                self.cells.append((rect, idx))

                is_selected = (self.selection == idx)
                is_hovered = rect.collidepoint(mx, my)

                if is_selected:
                    pygame.draw.rect(self.screen, (10,10,10),  rect, border_radius=8)
                    text_colour = (235,230,220)
                    border_width = 0
                    
                else:
                    pygame.draw.rect(self.screen, (235,230,220), rect, border_radius=8)
                    text_colour = (10,10,10)
                    border_width  = 3 if is_hovered else 1
                    border_colour  = (10,10,10) if is_hovered else (160,155,145)
                    pygame.draw.rect(self.screen, border_colour, rect, border_width, border_radius=8)
                    
                cell_name = self.f_cell.render(row, True, text_colour)
                self.screen.blit(cell_name, cell_name.get_rect(center=rect.center))

        #button width is 220, height is 44, gap of 20

        button_x = (self.W - 460) // 2
        button_y = self.H - 60
        leaderboard_rectangle = pygame.Rect(button_x, button_y, 220, 44)
        self.button_leaderboard = leaderboard_rectangle
        leaderboard_background = (10,10,10) if self.selection is not None else (190,185,175)
        pygame.draw.rect(self.screen, leaderboard_background, leaderboard_rectangle, border_radius=8)
        leaderboard_label = self.f_button.render("SHOW", True, (235,230,220) if self.selection is not None else (120, 115, 105))
        self.screen.blit(leaderboard_label, leaderboard_label.get_rect(center=leaderboard_rectangle.center))

        quit_rectangle = pygame.Rect(button_x + 240, button_y, 220, 44)
        self.button_quit = quit_rectangle
        quit_hover = quit_rectangle.collidepoint(mx, my)
        pygame.draw.rect(self.screen,(40, 40, 40) if quit_hover else (10,10,10),quit_rectangle, border_radius=8)
        pygame.draw.rect(self.screen, (100, 100, 100), quit_rectangle, 1, border_radius=8)
        quit_label = self.f_button.render("Quit", True, (235,230,220))
        self.screen.blit(quit_label, quit_label.get_rect(center=quit_rectangle.center))

    def call(self, key):
        subprocess.run(["bash", "./hub/leaderboard.sh", "./hub/history.csv", "./hub/users.tsv",key[0], key[1], "TicTacToe", "Connect4", "Othello"], check = False)

    def run(self):

        running = True
        while running:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.VIDEORESIZE:
                    self.W, self.H = event.size
                    self.screen = pygame.display.set_mode((self.W, self.H), pygame.RESIZABLE)

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    for rect, idx in self.cells:
                        if rect.collidepoint(mx, my):
                            self.selection = idx
                        
                    if self.button_leaderboard.collidepoint(mx, my) and self.selection is not None:
                            key = KEYS[self.selection]
                            self.call(key)
                            return key
                        
                    if self.button_quit.collidepoint(mx, my):
                            running = False
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_RETURN and self.selection is not None:
                        key = KEYS[self.selection]
                        self.call(key)
                        return key
            
            self.draw()
            pygame.display.flip()
                    
if __name__ == "__main__":
    result = Game_Over(None, "Mohit", "Arush", "Connect4").run()
    pygame.quit()

