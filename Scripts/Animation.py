from tkinter import *
import Maps
#up
Player_dUSpace=[] #The sprites for moving to the left (day)
Player_dUGoal=[] #The sprites for moving to the left (day)
#left
Player_dLGoal=[] #The sprites for moving to the left (day)
Player_dLSpace=[] #The sprites for moving to the left (day)
#right
Player_dRSpace=[] #The sprites for moving to the right (day)
Player_dRGoal=[] #The sprites for moving to the right (day)



def strings_in_lists(name, container):   
    for i in range(0,8): 
        for j in range (0,3):    
            frame=name+"%s.png"%(i)
            container.append(frame)

#strings_in_lists("Sprites/Player_dRSpace", Player_dRSpace) 
#strings_in_lists("Sprites/Player_dRGoal", Player_dRGoal) 
#strings_in_lists("Sprites/Player_dLSpace", Player_dLSpace) 
#strings_in_lists("Sprites/Player_dLGoal", Player_dLGoal) 

def Orientation(Day_or_Night, player, up, left, down, right, i):
    match player.Button_Pressed:
        case "Up":
            Day_or_Night.Player_image=up[i]
        case "Left":
            Day_or_Night.Player_image=left[i]
        case "Down":
            Day_or_Night.Player_image=down[i]
        case _:    
            Day_or_Night.Player_image=right[i]
    
    print(Day_or_Night.Player_image)
    
    return Day_or_Night.Player_image


def Animation_Player(root, Day_or_Night, player, i):
    if(i<23): 
        

        if (player.step_over==0):
            frame=Orientation(Day_or_Night, player, Player_dUSpace, Player_dLSpace, Player_dRSpace, Player_dRSpace, i)
            Maps.map_matrix[player.current_x][player.current_y].config(image=frame)

        elif (player.step_over==1):
            frame=Orientation(Day_or_Night, player, Player_dUGoal, Player_dLGoal, Player_dRGoal, Player_dRGoal, i)
            Maps.map_matrix[player.current_x][player.current_y].config(image=frame)
   
    else:
        i=0
    i += 1
    root.after(20, Animation_Player, root, Day_or_Night, player, i)