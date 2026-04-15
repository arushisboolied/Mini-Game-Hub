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
from matplotlib.widgets import Button

def read_history():
    data = []
    with open("history.txt","r") as f:
        lines = f.readlines()
    
    if(len(lines) <= 1):
        return data

    headers = lines[0].strip().split(",")
    for line in lines[1:]:
        values = line.strip().split(",")
        row = dict(zip(headers, values))
        data.append(row)
    
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
        if g not in game_counts:
            game_counts[g] = 0
        game_counts[g] += 1

    game_labels = list(game_counts.keys())
    game_values = list(game_counts.values())

    fig, axs = plt.subplots(2, 1, figsize=(12, 6))
    plt.subplots_adjust(bottom=0.25)

    axs[0].bar(players, win_counts)
    axs[0].set_title("Top 5 Players by Wins")
    axs[0].set_xlabel("Players")
    axs[0].set_ylabel("Wins")

    axs[1].pie(game_values, labels=game_labels, autopct='%1.1f%%')
    axs[1].set_title("Most Played Games")

    ax_next = plt.axes([0.2, 0.05, 0.25, 0.1])
    ax_quit = plt.axes([0.55, 0.05, 0.25, 0.1])

    btn_next = Button(ax_next, "Next Game")
    btn_quit = Button(ax_quit, "Quit")

    def next_game(event):
        plt.close(fig)
        subprocess.call([sys.executable, "game.py"])

    def quit_game(event):
        plt.close(fig)
        sys.exit()

    btn_next.on_clicked(next_game)
    btn_quit.on_clicked(quit_game)

    plt.show()


def main():
    data = read_history()
    if not data:
        return

    wins, games = stat_calculation(data)
    graphs(wins, games)
