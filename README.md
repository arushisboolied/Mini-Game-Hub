# Mini Game Hub in Python using Pygame

## Mohit Agarwal and Arush Anand

### CS108 Project - Spring Semester

---

## Abstract

This readme report aims to help the reader access and use our project - "Wormhole" - easily without extensive comprehension of the source code. It covers the project's concept, design, implementation and challenges faced during the development of the game hub.

---

## Project Overview

Wormhole is a two player based themed game hub built using the pygame library in python, where a pixel-art character navigates the game menu. <br>
Players register their accounts in the Hub through the Main terminal and their ids are stored in a tsv file. Every user must have a unique username and a password. Then, we move on to the menu where we meet our knight. <br>
Our knight has access to different worlds, Kingdom of Heaven, Blade Runner 2049 and Dune, that he can spawn in and then force a battle between the two players that are competing on the games they want - Tic Tac Toe, Connect 4 or Othello. <br>
During the active play of the games, non static sprites will denote the current player. Players have the options to either make a move or resign on their turns. <br>
After the games end the players meet the Director - the one who sees the flow of the worlds. The Director using his omniscience can tell the players about their rankings across the games they play on the Hub. <br>
The Leaderboard is a terminal printed table that is sorted based on the choice the players give to the Director. <br>
Players can view stastics on popular games and the top few winners in the post match stastics, after which they enter the Knight's World again. 

---

## Modules 

External modules we used are:

- `pygame-ce` - The frequently updated pygame community edition version of Pygame is a set of Python modules designed for writing video games.
- `numpy` - NumPy is a Python library used for working with arrays in a more effective way.
- `matplotlib` - Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.
- `os` - This module provides a portable way of using operating system dependent functionality.
- `sys` - This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
- `subprocess` - The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.

---
  
## Project Structure

The structure of the project directory can be depicted as follows:

```
.
├── hub/
│   ├── Assets/
│   │   ├── Game_Over/
│   │   │   ├── Background.png
│   │   │   └── Fonts.ttf
│   │   ├── Images - In game sprites, backgrounds and boards, Histograms, Pie Charts and Next Button.
│   │   ├── Fonts - Fonts used across all games
│   │   └── Theme.py
│   ├── games/
│   │   ├── connect4.py
│   │   ├── othello.py
│   │   └── tictactoe.py
│   ├── Menu_Assets/
│   │   ├── Codes - Levels, Character, Settings, Tiles and Support codes.
│   │   ├── Csv_Files/
│   │   │   ├── Map_Boundary.csv
│   │   │   └── Map_Regions.csv
│   │   ├── Fonts - Righteous Font
│   │   └── Images - Menu game sprites and map
│   ├── Game_Over.py
│   ├── game.py
│   ├── Menu.py
│   ├── stats.py
│   ├── history.csv
│   ├── users.tsv
│   ├── leaderboard.sh
│   └── main.sh
├── Report/
│   ├── Makefile
│   ├── Report.ttx
│   ├── Bibliography.bib
│   └── Report.pdf
├── .gitignore
├── README.md
└── Requirements.txt
```

---

## Execution Pipeline

The code runs as follows: <br>
<pre>
Main.sh --> Menu.py (Supported by Codes in Menu_Assets) <--> stats.py
                ^ 
                | 
   game.py <----|----> Game_Over.py -----> Leaderboard.sh <br>
</pre>

---

## Major Features

### Medieval Fantasy Menu

* Pixel art knight controlled by player whose actions trigger selection of games, speeds and themes
* Each theme has different character that the players assume the roles of - Antagonists and Protagonists

### Theme System 

Three Themes:

#### Kingdom of Heaven

* Wooden 
* Knight / Archer Character
* Stone Boards

#### Blade Runner 2049

* Neon
* Roy / Decker Character
* Holographic Boards

#### Dune

* Rock
* Paul Atreides / Harkonnen Character
* Desert 

The theme will affect the following features:

* Menu visuals
* Character sprites ( Also the player character )
* Game Boards
* Tokens 
* Animations of the sprites themselves


## Running Instructions

### Prerequisites
* Installation of Python
* Installation of modules - NumPy, Matplotlib and Pygame

#### Setting up `venv`

If you want to set up a `python` virtual environment for the project, follow the below instructions:

```
sh
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

To run the game run the following command in the terminal:
```
bash ./hub/main.sh
```

### Player Registration
Enter details as prompted by the registration system.

### Game Menu
Control the Knight using WASD and interact with spearmen using E. <br>
Note: Did not cap speed just for fun :) You can go out of the map as well.

### Individual games
- Tic Tac Toe on a 10x10 board with 5 in a row winning condition
- Connect 4 on a 7x7 board
- Othello on an 8x8 board

You can resign if you feel lost enough

### Leaderboard
A leaderboard sorted by wins, losses or win/loss ratio that you can choose how to view through the Director.

### Stats
Player statistics for various games and game statistics based on selection frequency

## References
1. [Pygame Official Documentation](https://www.pygame.org/docs/)
2. [Pygame CE Official Documentation](https://pyga.me/docs/)
3. [NumPy Official Documentation](https://numpy.org/doc/)
4. [Matplotlib Official Documentation](https://matplotlib.org/stable/index.html)

## Extra Credits
1. [Tiny Swords Asset Pack by Pixel Frog](https://pixelfrog-assets.itch.io/tiny-swords)
2. ChatGPT and Gemini for Pixel Art generation




















