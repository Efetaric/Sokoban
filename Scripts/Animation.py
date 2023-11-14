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
    for i in range(0,8):  #First 24 frames = standard animation
        for j in range (0,3):    
            frame=PhotoImage(file=name+"%s.png"%(i))
            container.append(frame)

    
    for i in range(0,4): #25,26,27 and 28 are for inbetweens
        frame=PhotoImage(file=name+"_Inb%s.png"%(i))
        container.append(frame)
        print(frame)

#strings_in_lists("Sprites/Player_dRSpace", Player_dRSpace) 
#strings_in_lists("Sprites/Player_dRGoal", Player_dRGoal) 
#strings_in_lists("Sprites/Player_dLSpace", Player_dLSpace) 
#strings_in_lists("Sprites/Player_dLGoal", Player_dLGoal) 
def Initialise_images():
    strings_in_lists("Sprites/Player_dUSpace", Player_dUSpace)
    strings_in_lists("Sprites/Player_dUGoal", Player_dUGoal) 
    strings_in_lists("Sprites/Player_dLSpace", Player_dLSpace) 
    strings_in_lists("Sprites/Player_dLGoal", Player_dLGoal) 
    strings_in_lists("Sprites/Player_dRSpace", Player_dRSpace) 
    strings_in_lists("Sprites/Player_dRGoal", Player_dRGoal) 


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
    #print(Day_or_Night.Player_image)
    return Day_or_Night.Player_image

def inb_short(Day_or_Night, player, X_coordonate, Y_coordonate, Player_Up, Player_Left, Player_Down, Player_Right, i ):
        frame=Orientation(Day_or_Night, player, Player_Up, Player_Left, Player_Down, Player_Right, i)
        Maps.map_matrix[player.current_x+(X_coordonate)][player.current_y+(Y_coordonate)].config(image=frame)

def erased(player, X_coordonate, Y_coordonate, old_area):
    Maps.map_matrix[player.current_x+(X_coordonate)][player.current_y+(Y_coordonate)].config(image=old_area)

def Animation_inbetween(root, Day_or_Night, player, X_coordonate, Y_coordonate, Player_Up, Player_Left, Player_Down, Player_Right, old_area):

        root.after(0, inb_short, Day_or_Night, player, X_coordonate, Y_coordonate, Player_Up, Player_Left, Player_Down, Player_Right, 24)
        root.after(10, inb_short, Day_or_Night, player, X_coordonate, Y_coordonate, Player_Up, Player_Left, Player_Down, Player_Right, 25)
        root.after(10,inb_short, Day_or_Night, player, 0, 0, Player_Up, Player_Left, Player_Down, Player_Right, 26)
        root.after(30, inb_short, Day_or_Night, player, 0, 0, Player_Up, Player_Left, Player_Down, Player_Right, 27)
        root.after(30, erased, player, X_coordonate, Y_coordonate, old_area)

def Inbetween_Order(root, Day_or_Night, player, Player_Up, Player_Left, Player_Down, Player_Right, old_area):
    match player.Button_Pressed:
        case "Up":
            Animation_inbetween(root, Day_or_Night, player, 0, 1, Player_Up, Player_Left, Player_Down, Player_Right, old_area)
        case "Left":
            Animation_inbetween(root, Day_or_Night, player, 1, 0, Player_Up, Player_Left, Player_Down, Player_Right, old_area)
        case "Down":
            Animation_inbetween(root, Day_or_Night, player, 0, -1, Player_Up, Player_Left, Player_Down, Player_Right, old_area)
        case "Right":
            Animation_inbetween(root, Day_or_Night, player, -1, 0, Player_Up, Player_Left, Player_Down, Player_Right, old_area)


def Animation_Player(root, Day_or_Night, player, i):
    if (player.inbetween==0):
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

        
        
