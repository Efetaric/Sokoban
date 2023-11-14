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

def S2S_G2G(root, Day_or_Night, player, X_coordonate, Y_coordonate, Player_Up, Player_Left, Player_Down, Player_Right, old_area):

    root.after(0, inb_short, Day_or_Night, player, X_coordonate, Y_coordonate, Player_Up, Player_Left, Player_Down, Player_Right, 24) #old box frame1 
    root.after(10, inb_short, Day_or_Night, player, X_coordonate, Y_coordonate, Player_Up, Player_Left, Player_Down, Player_Right, 25) #Old box fram2
    root.after(10,inb_short, Day_or_Night, player, 0, 0, Player_Up, Player_Left, Player_Down, Player_Right, 26) #New box frame1
    root.after(30, inb_short, Day_or_Night, player, 0, 0, Player_Up, Player_Left, Player_Down, Player_Right, 27) #New box frame 2
    root.after(30, erased, player, X_coordonate, Y_coordonate, old_area) #Old normal frame

def S2G_G2S(root, Day_or_Night, player, X_coordonate, Y_coordonate, Player_Up1, Player_Up2, Player_Left1, Player_Left2, Player_Down1, Player_Down2, Player_Right1, Player_Right2, old_area):
    root.after(0, inb_short, Day_or_Night, player, X_coordonate, Y_coordonate, Player_Up1, Player_Left1, Player_Down1, Player_Right1, 24)
    root.after(10, inb_short, Day_or_Night, player, X_coordonate, Y_coordonate, Player_Up1, Player_Left1, Player_Down1, Player_Right1, 25)
    root.after(10,inb_short, Day_or_Night, player, 0, 0, Player_Up2, Player_Left2, Player_Down2, Player_Right2, 26)
    root.after(30, inb_short, Day_or_Night, player, 0, 0, Player_Up2, Player_Left2, Player_Down2, Player_Right2, 27)
    root.after(30, erased, player, X_coordonate, Y_coordonate, old_area)

def Animation_Inbetweens(root, Day_or_Night, player, X_coordonate, Y_coordonate, Player_Up1, Player_Up2, Player_Left1, Player_Left2, Player_Down1, Player_Down2, Player_Right1, Player_Right2, old_area): #Space to goal or goal to space
    #This happens in Goal_Space function (Control_Logic module). Step_over is one step behind since the function's called after.
    if(player.step_over==0 and  Maps.map_matrix[player.current_x-(X_coordonate)][player.current_y-(Y_coordonate)].cget("image")==str(Day_or_Night.Chest_goal_image)): #Space to goal - Box
        S2G_G2S(root, Day_or_Night, player, X_coordonate, Y_coordonate, Player_Up1, Player_Up2, Player_Left1, Player_Left2, Player_Down1, Player_Down2, Player_Right1, Player_Right2, old_area)
        print("cbaba %s"%player.step_over)
    elif(player.step_over==1 and Maps.map_matrix[player.current_x-(X_coordonate)][player.current_y-(Y_coordonate)].cget("image")==str(Day_or_Night.Chest_space_image)): #Goal to space - Box
        S2G_G2S(root, Day_or_Night, player, X_coordonate, Y_coordonate, Player_Up1, Player_Up2, Player_Left1, Player_Left2, Player_Down1, Player_Down2, Player_Right1, Player_Right2, old_area)
        print("cmama %s"%player.step_over)  
    elif(player.step_over==0 and Maps.map_matrix[player.current_x-(X_coordonate)][player.current_y-(Y_coordonate)].cget("image")==str(Day_or_Night.Goal_image)): #Space to goal - No box
        S2G_G2S(root, Day_or_Night, player, X_coordonate, Y_coordonate, Player_Up1, Player_Up2, Player_Left1, Player_Left2, Player_Down1, Player_Down2, Player_Right1, Player_Right2, old_area)
        print("baba %s"%player.step_over)
    elif(player.step_over==1 and Maps.map_matrix[player.current_x-(X_coordonate)][player.current_y-(Y_coordonate)].cget("image")==str(Day_or_Night.Space_image)): #Space to goal - No box
        S2G_G2S(root, Day_or_Night, player, X_coordonate, Y_coordonate, Player_Up1, Player_Up2, Player_Left1, Player_Left2, Player_Down1, Player_Down2, Player_Right1, Player_Right2, old_area)
        print("mama %s"%player.step_over)    
    else:                                                                                                                                      #Space to Space or Goal to Goal - No box
        S2S_G2G(root, Day_or_Night, player, X_coordonate, Y_coordonate, Player_Up1, Player_Left1, Player_Down1, Player_Right1, old_area)    

def Inbetween_Order(root, Day_or_Night, player, Player_Up1, Player_Up2, Player_Left1, Player_Left2, Player_Down1, Player_Down2, Player_Right1, Player_Right2, old_area):
    match player.Button_Pressed:
        case "Up":
            Animation_Inbetweens(root, Day_or_Night, player, 0, 1, Player_Up1, Player_Up2, Player_Left1, Player_Left2, Player_Down1, Player_Down2, Player_Right1, Player_Right2, old_area)
        case "Left":
            Animation_Inbetweens(root, Day_or_Night, player, 1, 0, Player_Up1, Player_Up2, Player_Left1, Player_Left2, Player_Down1, Player_Down2, Player_Right1, Player_Right2, old_area)
        case "Down":
            Animation_Inbetweens(root, Day_or_Night, player, 0, -1, Player_Up1, Player_Up2, Player_Left1, Player_Left2, Player_Down1, Player_Down2, Player_Right1, Player_Right2, old_area)
        case "Right":
            Animation_Inbetweens(root, Day_or_Night, player, -1, 0, Player_Up1, Player_Up2, Player_Left1, Player_Left2, Player_Down1, Player_Down2, Player_Right1, Player_Right2, old_area)


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

        
        
