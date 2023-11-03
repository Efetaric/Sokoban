from tkinter import *
import Maps
import Animation


#Movement and anti-collision function (it encapsulates everything from this module)
def walk(root, player, map, hml):
    print(player.Button_Pressed)
    match player.Button_Pressed:
        case "Up":
            direction(Maps.map_matrix, player, 0, -1, map)
        case "Left":
            direction(Maps.map_matrix, player, -1, 0, map)
        case "Down":
            direction(Maps.map_matrix, player, 0, 1, map)
        case "Right":
            direction(Maps.map_matrix, player, 1, 0, map)

    print(map.Left_Spots)
    #Animation.Total_Player_Ani(map, player, 0)
    boxes_left(player, map, hml)




def direction(matrix, player, X_coordonate, Y_coordonate, map):
    #with a box
    if(matrix[player.current_x+(X_coordonate) ][player.current_y+(Y_coordonate)].cget("image")==str(map.Chest_space_image) 
        or matrix[player.current_x+(X_coordonate) ][player.current_y+(Y_coordonate)].cget("image")==str(map.Chest_goal_image)): ## Checks to see if there's any box ahead
        step_over_with_box(matrix, player, X_coordonate, Y_coordonate, map)

    #Without a box 
    elif (matrix[player.current_x+(X_coordonate)][player.current_y+(Y_coordonate)].cget("image")==str(map.Border_image) 
        or matrix[player.current_x+(X_coordonate)][player.current_y+(Y_coordonate)].cget("image")==str(map.Obstacle_image )): ##Verifies if there are obstacles (1 Step)
        return
    else:
        Goal_or_Space(matrix, player, map)
        step_over(matrix, player, X_coordonate, Y_coordonate, map)
        player_position(player, X_coordonate, Y_coordonate)



#The new position of the player
def player_position(player, X_coordonate, Y_coordonate): 
    player.current_x = player.current_x + (X_coordonate)
    player.current_y = player.current_y + (Y_coordonate)



##Stores the type of area that's under the user
def step_over(matrix, player, X_coordonate, Y_coordonate, map):
    if (matrix[player.current_x+(X_coordonate)][player.current_y+(Y_coordonate)].cget("image")==str(map.Goal_image) 
        or matrix[player.current_x+(X_coordonate)][player.current_y+(Y_coordonate)].cget("image")==str(map.Chest_goal_image)):#
        player.step_over=1
    elif (matrix[player.current_x+(X_coordonate)][player.current_y+(Y_coordonate)].cget("image")!=str(map.Goal_image)):
        player.step_over=0
    print("step %d"%player.step_over)
    


def step_over_with_box(matrix, player, X_coordonate, Y_coordonate, map):
    #With a box
    if (matrix[player.current_x+(X_coordonate+X_coordonate)][player.current_y+(Y_coordonate+Y_coordonate)].cget("image")==str(map.Border_image) 
        or matrix[player.current_x+(X_coordonate+X_coordonate)][player.current_y+(Y_coordonate+Y_coordonate)].cget("image")==str(map.Obstacle_image)): ##Verifies if there are obstacles ahead(2 Steps)
        return
    else:
        Goal_or_Space(matrix, player, map)
        step_over(matrix, player, X_coordonate, Y_coordonate, map)
        if (matrix[player.current_x+(X_coordonate+X_coordonate)][player.current_y+(Y_coordonate+Y_coordonate)].cget("image")==str(map.Goal_image)):
            matrix[player.current_x+(X_coordonate+X_coordonate)][player.current_y+(Y_coordonate+Y_coordonate)].config(image=str(map.Chest_goal_image)) ##Moves the box inside goal area and transforms it
            map.Left_Spots -= 1 #Decreases the goal slots area when a box is over it
        else:
            if (matrix[player.current_x+(X_coordonate)][player.current_y+(Y_coordonate)].cget("image")==str(map.Chest_goal_image)):
                map.Left_Spots += 1 #Increases the goal area if the player pushes a box out of it
            matrix[player.current_x+(X_coordonate+X_coordonate)][player.current_y+(Y_coordonate+Y_coordonate)].config(image=str(map.Chest_space_image)) ##Moves the box on empty space
        player_position(player, X_coordonate, Y_coordonate)



##Returns the area to normal after the user moves
def Goal_or_Space(matrix, player, map):
    if (player.step_over==1):
        matrix[player.current_x][player.current_y].config(image=str(map.Goal_image))
    elif (player.step_over==0):
        matrix[player.current_x][player.current_y].config(image=str(map.Space_image))



#this function changes the number of boxes left
#IMPORTANT -> If the player can still move after every goal spot is filled, this function may crack the game. When every box is moved to its area, the control buttons MUST BE DISABLED!
def boxes_left(player,map, hml):
    if (map.Left_Spots > 1):
        hml.config(text="%d boxes left"%map.Left_Spots)
    
    elif (map.Left_Spots == 1):
        hml.config(text="1 box left")

    else:
        hml.config(text="No boxes left")
        player.level+=1


        
