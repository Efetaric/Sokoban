from tkinter import *


#this launches the first tutorial map or first start map and sets the order ov the maps
def Maps_order(window, matrix, player, map):
    Standard_map(window, matrix, map)
    if (player.Button_Pressed=="Tutorial"):    
        tutorial_Map1(matrix, player, map)
    matrix[player.current_x][player.current_y].config(bg=map.Color_Player) #Places the player
    map.Left_Spots=map.Boxes

#Standard map - generates the borders and the empty space
def Standard_map(window, matrix, map):
    columns=[0]*15
    for j in range(0,15):
        for i in range (0,15): 
            matrix[j].append(columns[i])
            matrix[j][i]=Label(window, height=1, width=3, bg=map.Color_Space, relief=RAISED)
            matrix[j][i].grid(row=i, column=j, padx=1, pady=1)
            ##Makes the outter borders
            if (j==0 or j==14 or i==0 or i==14):
                matrix[j][i].config(bg=map.Color_Border)     
    matrix[7][5].config(bg="Magenta")
    
#First tutorial map
def tutorial_Map2(matrix, player, map):
    player.current_x=5
    player.current_y=7
    map.Boxes=1
    for j in range(1,14):
        for i in range (1,14): 
            if (j==7 and 4<i<10):
                matrix[i][j].config(bg=map.Color_Space)
            else:
                matrix[i][j].config(bg=map.Color_Obstacle) 
    matrix[9][7].config(bg=map.Color_Goal)
    matrix[8][7].config(bg=map.Color_Chest) 

def tutorial_Map1(matrix, player, map):
    player.current_x=5
    player.current_y=7
    map.Boxes=8
    for j in range(1,14):
        for i in range (1,14): 
            if ((j==5 and 2<i<12) or (j==6 and 2<i<12) or (j==7 and 2<i<12) or (j==8 and 2<i<12) or (j==9 and 2<i<12)):
                matrix[i][j].config(bg=map.Color_Space)
            else:
                matrix[i][j].config(bg=map.Color_Obstacle) 
    matrix[10][7].config(bg=map.Color_Goal)
    matrix[4][7].config(bg=map.Color_Chest) 
                

        