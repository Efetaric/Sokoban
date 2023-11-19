from tkinter import *
import Maps
import Animation
import Var


#Movement and anti-collision function (main func in module)
def walk(root, player, map, hml):
    #every press activates the inbetweens
   
    if (map.state=="Ready"):
        player.inbetween=1 
        print(player.Button_Pressed)
        match player.Button_Pressed:
            case "Up":
                direction(root, Maps.map_matrix, player, 0, -1, map)
            case "Left":
                direction(root, Maps.map_matrix, player, -1, 0, map)
            case "Down":
                direction(root, Maps.map_matrix, player, 0, 1, map)
            case "Right":
                direction(root, Maps.map_matrix, player, 1, 0, map)

        print(map.Left_Spots)
        boxes_left(player, map, hml)
        
    player.inbetween=0





def direction(root, matrix, player, X, Y, map):
    #with a box
    ## Checks to see if there's any box ahead
    if(matrix[player.X+X ][player.Y+Y].cget("text") in Var.Chests):
        step_over_with_box(root, matrix, player, X, Y, map)

    #Without a box 
    ##Verifies if there are obstacles (1 Step)
    elif (matrix[player.X+X][player.Y+Y].cget("text") in Var.Collision):
        return
    else:
        Goal_or_Space(root, player, map)
        step_over(matrix, player, X, Y)
        player_position(player, X, Y)



#The new position of the player
def player_position(player, X, Y): 
    player.X = player.X + X
    player.Y = player.Y + Y



##Stores the type of area that's under the user
def step_over(matrix, player, X, Y):
    if (matrix[player.X+X][player.Y+Y].cget("text") in Var.Goal_T):#
        player.step_over=1
    elif (matrix[player.X+X][player.Y+Y].cget("text") in Var.Space_T):
        player.step_over=0
    print("step %d"%player.step_over)
    

def step_over_with_box(root, matrix, player, X, Y, map):
    #With a box
    ##Verifies if there are obstacles ahead(2 Steps)
    if (matrix[player.X+(X+X)][player.Y+(Y+Y)].cget("text") in Var.Collision 
            or matrix[player.X+(X+X)][player.Y+(Y+Y)].cget("text") in Var.Chests): 
        return
    else:
        Goal_or_Space(root, player, map)
        step_over(matrix, player, X, Y)
        ##Doesn't decrease left boxes when moving from goal to goal
        if (matrix[player.X+X][player.Y+Y].cget("text")==Var.CoG  
                and (matrix[player.X+(X+X)][player.Y+(Y+Y)].cget("text")==Var.Goal)):
            matrix[player.X+(X+X)][player.Y+(Y+Y)].config(
                text=Var.CoG, 
                image=str(map.Chest_goal_image)) 
            matrix[player.X+X][player.Y+Y].config(
                text=Var.Goal, 
                image=str(map.Chest_goal_image)) 
        
        ##Space to Space
        elif (matrix[player.X+X][player.Y+Y].cget("text")==Var.CoS   
                and (matrix[player.X+(X+X)][player.Y+(Y+Y)].cget("text")==Var.Space)):
            matrix[player.X+(X+X)][player.Y+(Y+Y)].config(
                text=Var.CoS, 
                image=str(map.Chest_space_image)) 
            matrix[player.X+X][player.Y+Y].config(
                text=Var.Space, 
                image=str(map.Chest_space_image)) 
        
        #Moves the box from  Space to Goal
        elif(matrix[player.X+(X+X)][player.Y+(Y+Y)].cget("text")==Var.Goal):   
            matrix[player.X+(X+X)][player.Y+(Y+Y)].config(
                text=Var.CoG, 
                image=str(map.Chest_goal_image))
            matrix[player.X+X][player.Y+Y].config(
                text=Var.Space, 
                image=str(map.Chest_goal_image)) 
            #Decreases the goal slots area when a box is over it
            map.Left_Spots -= 1 
        
        ##Moves the box from Goal to Space
        elif(matrix[player.X+(X+X)][player.Y+(Y+Y)].cget("text")==Var.Space):
            matrix[player.X+(X+X)][player.Y+(Y+Y)].config(
                text=Var.CoS, 
                image=str(map.Chest_space_image))
            matrix[player.X+X][player.Y+Y].config(
                text=Var.Goal, 
                image=str(map.Chest_goal_image)) 
            #Increases the goal area if the player pushes a box out of it
            map.Left_Spots += 1
          
        player_position(player, X, Y)



##Returns the area to normal after the user moves
def Goal_or_Space(root, player, map):

    if (player.step_over==1):
        Animation.Inbetween_Order(
            root, map, player, 
            Animation.Player_dUGoal, 
            Animation.Player_dUSpace, 
            Animation.Player_dLGoal, 
            Animation.Player_dLSpace, 
            Animation.Player_dRGoal, 
            Animation.Player_dRSpace, 
            Animation.Player_dRGoal, 
            Animation.Player_dRSpace, 
            Var.Goal, map.Goal_image)
            
    elif (player.step_over==0):
        Animation.Inbetween_Order(
            root, map, player, 
            Animation.Player_dUSpace, 
            Animation.Player_dUGoal, 
            Animation.Player_dLSpace, 
            Animation.Player_dRGoal, 
            Animation.Player_dRSpace, 
            Animation.Player_dLGoal, 
            Animation.Player_dRSpace, 
            Animation.Player_dRGoal, 
            Var.Space, map.Space_image)

#this function changes the number of boxes left
#When every box is moved to its area, the control buttons MUST BE DISABLED!
def boxes_left(player,map, hml):
    if (map.Left_Spots > 1):
        hml.config(text="%d boxes left"%map.Left_Spots)
    
    elif (map.Left_Spots == 1):
        hml.config(text="1 box left")

    else:
        hml.config(text="No boxes left")
        player.level+=1
        map.state="Not_Ready"


        
