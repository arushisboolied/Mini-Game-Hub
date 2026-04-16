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
    axs[0].set_title("Top Players", color="white")
    axs[0].tick_params(colors='white')

    wedges, texts, autotexts = axs[1].pie(
        game_values,
        labels=game_labels,
        autopct='%1.1f%%',
        textprops={'color': 'white'}
    )
    for text in texts:
        text.set_fontsize(10)

    for autotext in autotexts:
        autotext.set_fontsize(10)
        autotext.set_color('white')

    axs[1].set_title("Games", color="white")

    plt.tight_layout()
    plt.savefig("./hub/Assets/Images/Leaderboard.png", transparent=True, bbox_inches='tight', pad_inches=0)
    plt.close()

def main():
    data = read_history()
    wins, games = stat_calculation(data)
    graphs(wins, games)

    pygame.init()

    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Leaderboard")

    background = pygame.image.load("./hub/Assets/Images/Background.png").convert()
    leaderboard = pygame.image.load("./hub/Assets/Images/Leaderboard.png").convert_alpha()

    quit_btn = pygame.image.load("./hub/Assets/Images/Quit.png").convert_alpha()
    new_btn = pygame.image.load("./hub/Assets/Images/Next.png").convert_alpha()

    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    leaderboard = pygame.transform.smoothscale(leaderboard, (580, 380))

    quit_btn = pygame.transform.smoothscale(quit_btn, (110, 90))
    new_btn = pygame.transform.smoothscale(new_btn, (110, 90))

    leaderboard_rect = leaderboard.get_rect(center=(WIDTH//2, HEIGHT//2 - 30))

    quit_rect = quit_btn.get_rect(bottomleft=(50, HEIGHT - 20))
    new_rect = new_btn.get_rect(bottomright=(WIDTH - 50, HEIGHT - 20))

    overlay = pygame.Surface((600, 400), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 140))
    overlay_rect = overlay.get_rect(center=leaderboard_rect.center)

    running = True
    while running:
        screen.blit(background, (0, 0))

        screen.blit(overlay, overlay_rect)
        screen.blit(leaderboard, leaderboard_rect)

        screen.blit(quit_btn, quit_rect)
        screen.blit(new_btn, new_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if quit_rect.collidepoint(event.pos):
                    running = False

                if new_rect.collidepoint(event.pos):
                    subprocess.Popen(["python", "menu.py"])
                    running = False

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()