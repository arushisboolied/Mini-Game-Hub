import csv
import os
#Defining paths
BASE_DIR=os.path.join(os.path.dirname(__file__), "..")
IMAGES_DIR=os.path.join(BASE_DIR, "Images")
CSV_DIR=os.path.join(BASE_DIR, "Csv_Files")
FONT_DIR=os.path.join(BASE_DIR, "Fonts")

#Loading all files
Map_Boundary_file=os.path.join(CSV_DIR, "Map_Boundary.csv")
Map_Regions_file=os.path.join(CSV_DIR, "Map_Regions.csv")
Boundary_image_path=os.path.join(IMAGES_DIR, "Boundary.png")
Character_Selection_image_path=os.path.join(IMAGES_DIR, "Character_Selection.png")
Interaction_Exit_image_path=os.path.join(IMAGES_DIR, "Interaction_Exit.png")
Settings_Text_image_path=os.path.join(IMAGES_DIR, "Settings_Text.png")
Game_Title_image_path=os.path.join(IMAGES_DIR, "Game_Title.png")
TicTacToe_Rules_image_path=os.path.join(IMAGES_DIR, "TicTacToe_Rules.png")
Connect4_Rules_image_path=os.path.join(IMAGES_DIR, "Connect4_Rules.png")
Othello_Rules_image_path=os.path.join(IMAGES_DIR, "Othello_Rules.png")
Leaderboard_text_path=os.path.join(IMAGES_DIR, "Leaderboard_Text.png")
Map_image_path=os.path.join(IMAGES_DIR, "Map.png")
Interaction_prompt_image_path=os.path.join(IMAGES_DIR, "Interaction_Interaction.png")
Spawn_Banner_image_path=os.path.join(IMAGES_DIR, "Spawn_Banner.png")
Settings_Banner_image_path=os.path.join(IMAGES_DIR, "Settings_Banner.png")
Game_Selection_image_path=os.path.join(IMAGES_DIR, "Game_Selection.png")
Hinterland_image_path=os.path.join(IMAGES_DIR, "Hinterlands.png")
Character_Selection_image_parent_path=IMAGES_DIR

Text_font_path=os.path.join(FONT_DIR, "Righteous.ttf")

#Loading Boundary from csv file
with open(Map_Boundary_file,"r") as f:
    reader=csv.reader(f)

    Obstacle_Map=list(reader)

#Loading Regions Boundary
with open(Map_Regions_file,"r") as f:
    reader=csv.reader(f)
    Region_Map=list(reader)

#For early testing
Test_Map=[
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ','p',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ','x',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x']
]


Theme_mapping={0: "Kingdom of \nHeaven", 1: "Blade Runner\n2049", 2: "Dune"}

#Defines interactive zones where user can press E
Interactive=[

    {"Zone":"Speed","pos":(1088,1296),"size":(96,96)},
    {"Zone":"Menu_Char","pos":(1088,1488),"size":(96,96)},
    {"Zone":"User1_Char","pos":(1088,1680),"size":(96,96)},
    {"Zone":"User2_Char","pos":(1088,1888),"size":(96,96)},
    {"Zone":"Theme","pos":(1088,2096),"size":(96,96)},
    {"Zone":"Tictactoe_game","pos":(2832,192),"size":(208,160)},
    {"Zone":"Connect4_game","pos":(3392,192),"size":(256,160)},
    {"Zone":"Othello_game","pos":(4048,176),"size":(240,176)},
    {"Zone":"Leaderboard","pos":(4832,144),"size":(144,80)}
    
    ]