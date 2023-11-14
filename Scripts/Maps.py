from tkinter import *

map_matrix=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] #This contains the map (it turns into a 15x15 matrix)

#Takes the data from the custom made maps to place the player, the obstacles, the goals and the boxes
def Maps_order(player, map):
    Which_Level[player.level](map_matrix, player, map)
    map.Left_Spots=map.Boxes
    map_matrix[player.current_x][player.current_y].config(image=map.Player_image) #Places the player


#Standard map - generates the borders and the empty space 
def Standard_map(window, map):    
    columns=[0]*17 #17 because the top and bottom walls are double
    for j in range(0,15):
        for i in range (0,17): 
            map_matrix[j].append(columns[i])
            if ((j==0 and i<15) or (j==14 and i<15) or i==0 or i==15):   ##Makes the outter borders
                map_matrix[j][i]=Label(window, height=26, width=26, image=map.Border_image, highlightthickness=0)
                map_matrix[j][i].grid(row=i, column=j)
            
            elif((i==1 and 0<j<14) or (i==16)):    ##Makes the bottom layer. First condition is for top and second for bottom.
                map_matrix[j][i]=Label(window, height=26, width=26, image=map.Border_image2, highlightthickness=0)
                map_matrix[j][i].grid(row=i, column=j)

            else:                                                   ##Makes the empty space
                map_matrix[j][i]=Label(window, height=26, width=26, image=map.Space_image, highlightthickness=0)
                map_matrix[j][i].grid(row=i, column=j)
                
  


    
#First tutorial map
def Map1(matrix, player, map):
    player.current_x=5
    player.current_y=8
    map.Boxes=1
    for j in range(1,14):
        for i in range (1,15): 
            if (i==1):
                matrix[j][i].config(image=map.Border_image2)
            elif (i==8 and 4<j<10):
                matrix[j][i].config(image=map.Space_image)
            else:
                matrix[j][i].config(image=map.Obstacle_image) 
    matrix[9][8].config(image=map.Goal_image)
    matrix[8][8].config(image=map.Chest_space_image) 

def Map2(matrix, player, map):
    player.current_x=4
    player.current_y=7
    map.Boxes=2
    for j in range(1,14):
        for i in range (1,14): 
            if ((j==5 and 2<i<12) or (j==6 and 2<i<12) or (j==7 and 2<i<12) or (j==8 and 2<i<12) or (j==9 and 2<i<12)):
                matrix[i][j].config(image=map.Space_image)
            else:
                matrix[i][j].config(image=map.Obstacle_image) 
    matrix[10][7].config(image=map.Goal_image)
    matrix[10][8].config(image=map.Goal_image)
    matrix[5][7].config(image=map.Chest_space_image) 
    matrix[5][8].config(image=map.Chest_space_image)


Which_Level={1:Map1,2:Map2,3:Map1,4:Map2,5:Map1,}#This dictionary orders the maps



        