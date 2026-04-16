import pygame
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import time
import pathlib
import subprocess
import datetime
import random

def read_history():
    data = []
    with open("./hub/history.csv", "r") as f:
        for line in f:
            values = [v.strip() for v in line.split(",")]
            if len(values) != 4:
                continue
            data.append({
                "Winner": values[0],
                "Loser": values[1],
                "Date": values[2],
                "Game": values[3]
            })
    return data

def stat_calculation(data):
    wins = {}
    games = []
    for row in data:
        winner = row["Winner"]
        game = row["Game"]
        if winner not in wins:
            wins[winner] = 0
        wins[winner] += 1
        games.append(game)
    return wins, games

def graphs(wins, games):
    sorted_players = sorted(wins.items(), key=lambda x: x[1], reverse=True)[:5]
    players = [p[0] for p in sorted_players]
    win_counts = [p[1] for p in sorted_players]

    game_counts = {}
    for g in games:
        game_counts[g] = game_counts.get(g, 0) + 1

    game_labels = list(game_counts.keys())
    game_values = list(game_counts.values())

    fig, axs = plt.subplots(2, 1, figsize=(6, 6))
    fig.patch.set_alpha(0)

    for ax in axs:
        ax.set_facecolor((0, 0, 0, 0))

    axs[0].bar(players, win_counts)
    axs[0].set_title("Top Players", color="black")
    axs[0].tick_params(colors='black')

    wedges, texts, autotexts = axs[1].pie(
        game_values,
        labels=game_labels,
        autopct='%1.1f%%',
        textprops={'color': 'black'}
    )
    for text in texts:
        text.set_fontsize(10)

    for autotext in autotexts:
        autotext.set_fontsize(10)
        autotext.set_color('black')

    axs[1].set_title("Games", color="black")

    plt.tight_layout()
    plt.savefig("./hub/Assets/Images/Leaderboard.png", transparent=True, bbox_inches='tight', pad_inches=0)
    plt.close()

def main():
    data = read_history()
    wins, games = stat_calculation(data)
    graphs(wins, games)

    pygame.init()

    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.RESIZABLE)
    pygame.display.set_caption("Leaderboard")

    background = pygame.image.load("./hub/Assets/Images/Background.jpeg").convert()
    leaderboard = pygame.image.load("./hub/Assets/Images/Leaderboard.png").convert_alpha()
    new_btn = pygame.image.load("./hub/Assets/Images/NextGlow.png").convert_alpha()

    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    leaderboard = pygame.transform.scale(leaderboard, (580, 380))

    new_btn = pygame.transform.scale(new_btn, (100,88))

    leaderboard_rect = leaderboard.get_rect(center=(WIDTH//2, HEIGHT//2 - 30))

    new_rect = new_btn.get_rect(topleft=(700,299))
    col_rect = pygame.Rect(725,323,51,34)
    
    running = True
    screen.blit(background, (0, 0))
    screen.blit(leaderboard, leaderboard_rect)
    bg_btn=screen.subsurface(new_rect).copy()
    while running:
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                if new_rect.collidepoint(event.pos):
                    subprocess.Popen(["python", "menu.py"])
                    running = False

            if col_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(new_btn, new_rect)
            else:
                screen.blit(bg_btn, new_rect)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()