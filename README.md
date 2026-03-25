# <Insert Cool Hub Name>

This project aims to build a stylized game hub with a game menu and 3-4 turn based two player games.

## Project Overview

<The cool project name> is a two player based themed game hub built using pygame, where a pixel-art character navigates the menus. The hub allows players to:

* Select a theme(Futuristic, Medieval, Cavemen)
* Select a character for both players which will be displayed while the characters are competing in a game
* Choose a themed version of the following games:
  * TicTacToes
  * Othello
  * Connect4
  * (Inscryption Maybe - Just an outreach)

The main.sh ensures users data storage and encryption of passwords and hence, authentication to start the game-hub. The game.py along with supporting py files contain the menu navigation logic and base classes for games. The leaderboard.sh is used to maintain the history of scores. (You need to know who is the best)

## Execution Flow

<pre>main.sh --> game.py --> leaderboard.sh<br>
             ^                    |<br>
             |                    |<br>
             |____________________|( idea taken from doc directory structure)</pre>

Game.py contains
* Game-menu (Includes pixel art character pygame code and settings which include theme selection, audio and more settings(thinking))
* Gameplay (Base class for two player theme based games)
* Post game analytics (Matplotlib)

## Major Features

### Pixel Art Game Based Menu

* Pixel art character controlled by player which actions trigger selection of menu buttons
* Each theme has different character ( Can I use AI for making pixel art character ? )

### Theme System 

Three Themes:

#### Medieval

* Wooden 
* Knight / Archer Character
* Sword Slash action
* Stone Boards

#### Futuristic

* Neon
* Cyborg / Holo Robot Character
* Lightsaber (Join the dark side)
* Holographic Boards

#### Cavemen

* Rock
* Cavemen / Hunter Character
* Club/Bone
* Dirt Boards

The theme will affect the following features:

* Menu visuals
* Character sprites ( Also the player character )
* Game Boards
* Tokens ( Eg. O might look like a crown from above in tictactoe )
* Background audio
* (Sound effects - Thinking of Adding)
* (Animations?? - Too much work)

### Class Structure ( that i believe we will add )

1. class Menu
2. class Menu character
3. class Theme
4. class BaseGame

### Execution Flow and Implemention Plan

#### Step 1 - main.sh

Ensures authentication and storing new data about users for firing up game-hub.

#### Step 2 - game.py

Menu UI pops up. A random character selected from the themes is displayed and used to select the Start Game, Settings or Quit button.

1.Start Game - Takes you to game selection menu, the rules of the game can be displayed by a button between game selection button.
2.Settings - Includes Audio selection, Theme selection, Character Selection for Player 1 and 2.
3. Quit - (Bruh what do you expect)

#### Step 3 - Leaderboard.sh

Manages handling for scores tracking.

#### Step 4 - Game.py (Again?? but its for analytics woohoooo)

Shows analytics of the game you just played.

#### Optional Step 5 if you continue playing (Pls do, it will be addicting)

Loops to Step 2

### Directory Structure

<pre>hub/
│
├── main.sh
├── game.py
├── leaderboard.sh
│
├── assets/
│   ├── medieval/
│   │   ├── characters/
│   │   ├── ui/
│   │   └── boards/
│   │
│   ├── futuristic/
│   │   ├── characters/
│   │   ├── ui/
│   │   └── boards/
│   │
│   └── cavemen/
│       ├── characters/
│       ├── ui/
│       └── boards/
│
├── games/
│   ├── tictactoe.py
│   ├── othello.py
│   └── connect4.py
│
└──(more py files maybe in a folder for object oriented and easy code management)</pre>

### Final comments by writer

Please give 10 cgpa, I am in a tech event and writing this T_T

















