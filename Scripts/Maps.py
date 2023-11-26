from tkinter import *
import Var

#This contains the map 
map_matrix=[
    [],[],[],[],[],
    [],[],[],[],[],
    [],[],[],[],[]] 

#Map argument in the following functions = Day_or_Night obj.
#Loads or refreshes the images
def Refresh(map):
    for i in range(0,17):
        for j in range(0,15):
            match map_matrix[j][i].cget("text"):
                case Var.Border:
                    map_matrix[j][i].config(image=map.Border_image)
                case Var.Border1:
                    map_matrix[j][i].config(image=map.Border_image1)
                case Var.Torch:
                    map_matrix[j][i].config(image=map.Torch_image)
                case Var.Obstacle:
                    map_matrix[j][i].config(image=map.Obstacle_image)
                case Var.Space:
                    map_matrix[j][i].config(image=map.Space_image)
                case Var.Goal:
                    map_matrix[j][i].config(image=map.Goal_image)
                case Var.CoS:
                    map_matrix[j][i].config(image=map.Chest_space_image)
                case Var.CoG:
                    map_matrix[j][i].config(image=map.Chest_goal_image)
                case Var.Player:
                    map_matrix[j][i].config(image=map.Player_image)

    

#Place the player, the obstacles, the goals and the boxes
def Maps_order(player, map):
    Which_Level[player.level](map_matrix, player, map)
    map.Left_Spots=map.Boxes
    map_matrix[player.X][player.Y].config(text=Var.Player)
    Refresh(map)


#Standard map - generates the borders and the empty space 
def Standard_map(window):    
    columns=[0]*17 #17 because the top and bottom walls are double
    for j in range(0,15):
        for i in range (0,17): 
            map_matrix[j].append(columns[i])
            ##Makes the outter borders
            if ((j==0 and i<15) 
                    or (j==14 and i<15) 
                    or i==0 or i==15):  
                map_matrix[j][i]=Label(
                    window, height=30, width=30, 
                    text=Var.Border, highlightthickness=0)
                map_matrix[j][i].grid(row=i, column=j)

            
            ##Makes the bottom layer. (Bottom layer)
            elif((i==16)):
                map_matrix[j][i]=Label(
                    window, height=30, width=30, 
                    highlightthickness=0)
                map_matrix[j][i].grid(row=i, column=j)
                if j%2!=0:
                    map_matrix[j][i].config(text=Var.Torch)
                else:
                    map_matrix[j][i].config(text=Var.Border1)
                        
            ##Makes the empty space
            else:                                                   
                map_matrix[j][i]=Label(
                    window, height=30, width=30, 
                    text=Var.Space, highlightthickness=0)
                map_matrix[j][i].grid(row=i, column=j)

                
  


    
#First tutorial map
def Map1(matrix, player, map):
    player.X=5
    player.Y=8
    map.Boxes=1
    for j in range(1,14):
        for i in range (1,15): 
            #border
            if (i==1):
                if j%2!=0:
                    map_matrix[j][i].config(text=Var.Torch)
                else:
                    map_matrix[j][i].config(text=Var.Border1)
            elif (i==8 and 4<j<10):
                matrix[j][i].config(text=Var.Space)
            else:
                matrix[j][i].config(text=Var.Obstacle) 
    matrix[9][8].config(
        text=Var.Goal, 
        image=map.Goal_image)
    matrix[8][8].config(text=Var.CoS) 
    player.step_over=0

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
                matrix[i][j].config(text=Var.Space)
            else:
                matrix[i][j].config(text=Var.Obstacle) 
    matrix[10][7].config(text=Var.Goal)
    matrix[10][8].config(text=Var.Goal)
    matrix[5][7].config(text=Var.CoS) 
    matrix[5][8].config(text=Var.CoS)
    player.step_over=0
#Orders the maps
Which_Level={1:Map1,2:Map2,3:Map1,4:Map2,5:Map1,}



        