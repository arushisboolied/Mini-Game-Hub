import pygame
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import sys
import subprocess



######################### CSV FILE READER #########################

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



######################### GRAPHS CREATION #########################

def graphs(wins, games):

    ##### FONTS FOR READABILITY #####

    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 12,
    })

    ##### HISTOGRAM DATA #####

    sorted_players = sorted(wins.items(), key=lambda x: x[1], reverse=True)[:5]
    players = [p[0] for p in sorted_players]
    win_counts = [p[1] for p in sorted_players]

    ##### PIE CHART DATA #####

    game_counts = {}
    for g in games:
        game_counts[g] = game_counts.get(g, 0) + 1

    game_labels = list(game_counts.keys())
    game_values = list(game_counts.values())

    ##### PLOTTING THE HISTOGRAM #####

    fig, ax = plt.subplots(figsize=(6, 3), dpi=300)
    fig.patch.set_alpha(0)
    ax.set_facecolor((0, 0, 0, 0))

    colors_bar = ["#4C72B0", "#5A8AC6", "#6BA3D6", "#7DBBE6", "#8FD3F4"]
    ax.bar(players, win_counts, color=colors_bar)

    ax.set_title("Top Players", fontsize=18, fontweight='bold', pad=10)
    ax.spines['top'].set_visible(False)
    ax.set_xlabel("Player Name", fontsize=12, color="#D0E8FF",labelpad=10)
    ax.set_ylabel("Number of Games Won", fontsize=12, color="#D0E8FF",labelpad=20)

    ax.tick_params(axis='x', labelsize=13, pad=6)
    ax.tick_params(axis='y', labelsize=11)

    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_color("#D0E8FF")
        label.set_fontsize(14)
        label.set_fontweight("normal")
        label.set_path_effects([path_effects.withStroke(linewidth=3, foreground="black")])
    plt.tight_layout()
    plt.savefig("./hub/Assets/Images/Histogram.png", transparent=True, bbox_inches='tight', pad_inches=0)
    plt.close()

    ##### PLOTTING THE PIE CHART #####

    fig, ax = plt.subplots(figsize=(4, 4), dpi=300)
    fig.patch.set_alpha(0)
    ax.set_facecolor((0, 0, 0, 0))
    colors_pie = ["#4C72B0", "#DD8452", "#55A868", "#C44E52"]
    wedges, texts, autotexts = ax.pie(
        game_values,
        labels=None,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors_pie,
        pctdistance=0.7,
        wedgeprops={'linewidth': 1, 'edgecolor': 'white'}
    )
    ax.set_title("Games", fontsize=16, fontweight='bold', pad=12)
    legend_labels = [f"{label}" for label in game_labels]
    leg = ax.legend(wedges, legend_labels, loc="center left", bbox_to_anchor=(1, 0.5), fontsize=13, frameon=False)
    for text in leg.get_texts():
        text.set_color("white")
        text.set_fontweight("bold")
        text.set_path_effects([path_effects.withStroke(linewidth=3, foreground="black")])
    for autotext in autotexts:
        autotext.set_fontsize(12)
        autotext.set_color("white")
        autotext.set_fontweight("bold")
        autotext.set_path_effects([path_effects.withStroke(linewidth=3, foreground="black")])
    plt.tight_layout()
    plt.savefig("./hub/Assets/Images/Piechart.png", transparent=True, bbox_inches='tight', pad_inches=0)
    plt.close()



######################### MAIN FUNCTION #########################

def main():
    data = read_history()
    wins, games = stat_calculation(data)
    graphs(wins, games)

    pygame.init()

    ##### PYGAME WINDOW SETUP #####

    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.RESIZABLE)
    pygame.display.set_caption("Leaderboard")

    ##### ASSETS #####

    background = pygame.image.load("./hub/Assets/Images/Background.png").convert()
    histogram = pygame.image.load("./hub/Assets/Images/Histogram.png").convert_alpha()
    piechart = pygame.image.load("./hub/Assets/Images/Piechart.png").convert_alpha()
    new_btn = pygame.image.load("./hub/Assets/Images/NextGlow.png").convert_alpha()

    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    histogram = pygame.transform.scale(histogram, (360, 230))
    piechart = pygame.transform.scale(piechart, (180, 180))

    new_btn = pygame.transform.scale(new_btn, (100,88))

    histogram_rect = histogram.get_rect(topleft=(120, 80))          
    piechart_rect = piechart.get_rect(bottomright=(680, 450))      

    new_rect = new_btn.get_rect(topleft=(700,299))
    col_rect = pygame.Rect(725,323,51,34)

    ##### MAIN LOOP #####
    
    running = True
    screen.blit(background, (0, 0))
    screen.blit(histogram, histogram_rect)
    screen.blit(piechart, piechart_rect)
    bg_btn=screen.subsurface(new_rect).copy()
    while running:
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            ##### REDIRECTION EVENT HANDLER #####

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if new_rect.collidepoint(event.pos):
                    subprocess.Popen(["python3", "./hub/Menu.py"])
                    running = False

            ##### HANDLE WINDOW RESIZE #####

            elif event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
                raw_background = pygame.image.load("./hub/Assets/Images/Background.png").convert()
                raw_histogram  = pygame.image.load("./hub/Assets/Images/Histogram.png").convert_alpha()
                raw_piechart   = pygame.image.load("./hub/Assets/Images/Piechart.png").convert_alpha()
                raw_new_btn   = pygame.image.load("./hub/Assets/Images/NextGlow.png").convert_alpha()

                background = pygame.transform.scale(raw_background, (WIDTH, HEIGHT))
                histogram  = pygame.transform.scale(raw_histogram,  (int(WIDTH * 0.45), int(HEIGHT * 0.38)))
                piechart   = pygame.transform.scale(raw_piechart,   (int(WIDTH * 0.225), int(HEIGHT * 0.30)))
                new_btn    = pygame.transform.scale(raw_new_btn,   (int(WIDTH * 0.125), int(HEIGHT * 0.147)))

                histogram_rect = histogram.get_rect(topleft=(int(WIDTH * 0.15), int(HEIGHT * 0.133)))
                piechart_rect = piechart.get_rect(bottomright=(int(WIDTH * 0.85), int(HEIGHT * 0.75)))
                new_rect = new_btn.get_rect(topleft=(int(WIDTH * 0.875), int(HEIGHT * 0.498)))
                col_rect = pygame.Rect(int(WIDTH * 0.906), int(HEIGHT * 0.538), int(WIDTH * 0.063), int(HEIGHT * 0.056))

                screen.blit(background, (0, 0))
                screen.blit(histogram, histogram_rect)
                screen.blit(piechart, piechart_rect)
                bg_btn = screen.subsurface(new_rect).copy()

            if col_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(new_btn, new_rect)
            else:
                screen.blit(bg_btn, new_rect)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()