from tkinter import *
import Var

#This contains the map 
map_matrix=[
    [],[],[],[],[],
    [],[],[],[],[],
    [],[],[],[],[]] 
#Place the player, the obstacles, the goals and the boxes
def Maps_order(player, map):
    Which_Level[player.level](map_matrix, player, map)
    map.Left_Spots=map.Boxes
    map_matrix[player.X][player.Y].config(
        text=Var.Player, 
        image=map.Player_image)


#Standard map - generates the borders and the empty space 
def Standard_map(window, map):    
    columns=[0]*17 #17 because the top and bottom walls are double
    for j in range(0,15):
        for i in range (0,17): 
            map_matrix[j].append(columns[i])
            ##Makes the outter borders
            if ((j==0 and i<15) 
                    or (j==14 and i<15) 
                    or i==0 or i==15):  
                map_matrix[j][i]=Label(
                    window, height=26, width=26, text=Var.Border, 
                    image=map.Border_image, highlightthickness=0)
                map_matrix[j][i].grid(row=i, column=j)
            
            ##Makes the bottom layer. (Top/Bottom layer)
            elif((i==1 and 0<j<14) or (i==16)):    
                map_matrix[j][i]=Label(
                    window, height=26, width=26, text=Var.Border1, 
                    image=map.Border_image2, highlightthickness=0)
                map_matrix[j][i].grid(row=i, column=j)
            
            ##Makes the empty space
            else:                                                   
                map_matrix[j][i]=Label(
                    window, height=26, width=26, text=Var.Space, 
                    image=map.Space_image, highlightthickness=0)
                map_matrix[j][i].grid(row=i, column=j)
                
  


    
#First tutorial map
def Map1(matrix, player, map):
    player.X=5
    player.Y=8
    map.Boxes=1
    for j in range(1,14):
        for i in range (1,15): 
            if (i==1):
                matrix[j][i].config(
                    text=Var.Border1, 
                    image=map.Border_image2)
            elif (i==8 and 4<j<10):
                matrix[j][i].config(
                    text=Var.Space, 
                    image=map.Space_image)
            else:
                matrix[j][i].config(
                    text=Var.Obstacle, 
                    image=map.Obstacle_image) 
    matrix[9][8].config(
        text=Var.Goal, 
        image=map.Goal_image)
    matrix[8][8].config(text=Var.CoS, image=map.Chest_space_image) 

def Map2(matrix, player, map):
    player.X=4
    player.Y=7
    map.Boxes=2
    for j in range(1,14):
        for i in range (1,14): 
            if ((j==5 and 2<i<12) 
                    or (j==6 and 2<i<12) 
                    or (j==7 and 2<i<12) 
                    or (j==8 and 2<i<12) 
                    or (j==9 and 2<i<12)):
                matrix[i][j].config(
                    text=Var.Space, 
                    image=map.Space_image)
            else:
                matrix[i][j].config(
                    text=Var.Obstacle, 
                    image=map.Obstacle_image) 
    matrix[10][7].config(
        text=Var.Goal, 
        image=map.Goal_image)
    matrix[10][8].config(
        text=Var.Goal, 
        image=map.Goal_image)
    matrix[5][7].config(
        text=Var.CoS, 
        image=map.Chest_space_image) 
    matrix[5][8].config(
        text=Var.CoS, 
        image=map.Chest_space_image)

#Orders the maps
Which_Level={1:Map1,2:Map2,3:Map1,4:Map2,5:Map1,}



        