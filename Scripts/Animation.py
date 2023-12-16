from tkinter import *
import Maps
import Var
#up
Player_dUSpace=[] #The sprites for moving to the top (day)
Player_dUGoal=[] #The sprites for moving to the top (day)
#left
Player_dLGoal=[] #The sprites for moving to the left (day)
Player_dLSpace=[] #The sprites for moving to the left (day)
#right
Player_dRSpace=[] #The sprites for moving to the right (day)
Player_dRGoal=[] #The sprites for moving to the right (day)
#Wall torch
Player_nTorch=[] #Torch sprites


def strings_in_lists(name, container):
    for i in range(0,4):  #First 24 frames = standard animation   
        frame=PhotoImage(file=name+"%s.png"%(i))
        container.append(frame)

def Initialise_images():
    strings_in_lists("Sprites/Player_dUSpace", Player_dUSpace)
    strings_in_lists("Sprites/Player_dUGoal", Player_dUGoal) 
    strings_in_lists("Sprites/Player_dLSpace", Player_dLSpace) 
    strings_in_lists("Sprites/Player_dLGoal", Player_dLGoal) 
    strings_in_lists("Sprites/Player_dRSpace", Player_dRSpace) 
    strings_in_lists("Sprites/Player_dRGoal", Player_dRGoal)
    strings_in_lists("Sprites/Wall_nTorch", Player_nTorch) 


def Orientation(
        Day_or_Night, player, up, 
        left, down, right, i):
    match player.Button_Pressed:
        case "Up":
            Day_or_Night.Player_image=up[i]
        case "Left":
            Day_or_Night.Player_image=left[i]
        case "Down":
            Day_or_Night.Player_image=down[i]
        case _:    
            Day_or_Night.Player_image=right[i]
    #print(Day_or_Night.Player_image)
    return Day_or_Night.Player_image


def Animation_Player(root, Day_or_Night, player, cf):
    if(cf<4): 

        if (player.step_over==0):
            frame=Orientation(
                Day_or_Night, player, 
                Player_dUSpace, Player_dLSpace, 
                Player_dRSpace, Player_dRSpace, cf)
            Maps.map_matrix[player.X][player.Y].config(image=frame)

        elif (player.step_over==1):
            frame=Orientation(
                Day_or_Night, player, 
                Player_dUGoal, Player_dLGoal, 
                Player_dRGoal, Player_dRGoal, cf)
            Maps.map_matrix[player.X][player.Y].config(image=frame)

        cf += 1
    else:
        cf=0

            
    root.after(40, Animation_Player, root, Day_or_Night, player, cf)

def Animation_Map(root, Day_or_Night, cf):
    if (Day_or_Night.mode==0):
        if(cf<4):
            for i in range(1,17):
                for j in range (1,15): 
                    if (Maps.map_matrix[j][i].cget("text")==Var.Torch):
                        Maps.map_matrix[j][i].config(image=Player_nTorch[cf])
                    #if (Maps.map_matrix[j][i].cget("text")==Var.Space):
                    #    Maps.map_matrix[j][i].config(image=Player_nTorch[cf])
            cf += 1
        else:
            cf=0
    root.after(100,Animation_Map, root, Day_or_Night, cf)
        
        



        
        
