import csv
import os

Map_Boundary_file=os.path.join(os.path.dirname(__file__), "../Csv_Files/Map_Boundary.csv")
Map_Regions_file=os.path.join(os.path.dirname(__file__), "../Csv_Files/Map_Regions.csv")
Boundary_image_path=os.path.join(os.path.dirname(__file__), "../Images/Boundary.png")
Character_Selection_image_path=os.path.join(os.path.dirname(__file__), "../Images/Character_Selection.png")
Interaction_Exit_image_path=os.path.join(os.path.dirname(__file__), "../Images/Interaction_Exit.png")
Settings_Text_image_path=os.path.join(os.path.dirname(__file__), "../Images/Settings_Text.png")
Game_Title_image_path=os.path.join(os.path.dirname(__file__), "../Images/Game_Title.png")
TicTacToe_Rules_image_path=os.path.join(os.path.dirname(__file__), "../Images/TicTacToe_Rules.png")
Connect4_Rules_image_path=os.path.join(os.path.dirname(__file__), "../Images/Connect4_Rules.png")
Othello_Rules_image_path=os.path.join(os.path.dirname(__file__), "../Images/Othello_Rules.png")
Map_image_path=os.path.join(os.path.dirname(__file__), "../Images/Map.png")
Interaction_prompt_image_path=os.path.join(os.path.dirname(__file__), "../Images/Interaction_Interaction.png")
Spawn_Banner_image_path=os.path.join(os.path.dirname(__file__), "../Images/Spawn_Banner.png")
Settings_Banner_image_path=os.path.join(os.path.dirname(__file__), "../Images/Settings_Banner.png")
Game_Selection_image_path=os.path.join(os.path.dirname(__file__), "../Images/Game_Selection.png")
Hinterland_image_path=os.path.join(os.path.dirname(__file__), "../Images/Hinterlands.png")
Character_Selection_image_parent_path=os.path.join(os.path.dirname(__file__), "../Images/")

Text_font_path=os.path.join(os.path.dirname(__file__), "../Fonts/Righteous.ttf")


with open(Map_Boundary_file,"r") as f:
    reader=csv.reader(f)

    Obstacle_Map=list(reader)

with open(Map_Regions_file,"r") as f:
    reader=csv.reader(f)
    Region_Map=list(reader)

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
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],]

Theme_mapping={0: "medieval", 1: "futuristic", 2: "dune"}

Interactive=[

    {"Zone":"Speed","pos":(1088,1296),"size":(96,96)},
    {"Zone":"Menu_Char","pos":(1088,1488),"size":(96,96)},
    {"Zone":"User1_Char","pos":(1088,1680),"size":(96,96)},
    {"Zone":"User2_Char","pos":(1088,1888),"size":(96,96)},
    {"Zone":"Theme","pos":(1088,2096),"size":(96,96)},
    {"Zone":"Tictactoe_game","pos":(2832,192),"size":(208,160)},
    {"Zone":"Connect4_game","pos":(3392,192),"size":(256,160)},
    {"Zone":"Othello_game","pos":(4048,176),"size":(240,176)},
    {"Zone":"Exit","pos":(4832,144),"size":(144,80)}
    
    ]