from tkinter import *
import Maps
Player_dRGoal=[] #The sprites for moving to the right (day)
Player_dLGoal=[] #The sprites for moving to the left (day)
def strings_in_lists(name, container):   
    for i in range(0,8): 
        for j in range (0,3):    
            frame=name+"%s.png"%(i)
            container.append(frame)
    print(len(Player_dRGoal))

strings_in_lists("Sprites/Player_dRGoal", Player_dRGoal) 
strings_in_lists("Sprites/Player_dLGoal", Player_dLGoal) 

        


def Orientation(Day_or_Night, player, i):
    match player.Button_Pressed:
        case "Up":
            Day_or_Night.Player_goal_image=PhotoImage(file=Player_dRGoal[i])
        case "Left":
            Day_or_Night.Player_goal_image=PhotoImage(file=Player_dLGoal[i])
        case "Down":
            Day_or_Night.Player_goal_image=PhotoImage(file=Player_dRGoal[i])
        case _:    
            Day_or_Night.Player_goal_image=PhotoImage(file=Player_dRGoal[i])
    
    return Day_or_Night.Player_goal_image

def Animation_Player(root, Day_or_Night, player, i):
    print(i)
    if(i<23): 
        frame=Orientation(Day_or_Night, player, i)

        if (player.step_over==0):
            Maps.map_matrix[player.current_x][player.current_y].config(image=frame)

        elif (player.step_over==1):
            Maps.map_matrix[player.current_x][player.current_y].config(image=frame)
   
    else:
        i=0
    i += 1
    root.after(20, Animation_Player, root, Day_or_Night, player, i)

