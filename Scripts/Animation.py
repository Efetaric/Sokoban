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


def Pstrings_in_lists(name, container):
    for i in range(0,8):  #First 24 frames = standard animation
        for j in range (0,3):    
            frame=PhotoImage(file=name+"%s.png"%(i))
            container.append(frame)

    
    for i in range(0,4): #25,26,27 and 28 are for inbetweens
        frame=PhotoImage(file=name+"_Inb%s.png"%(i))
        container.append(frame)
        print(frame)

def Mstrings_in_lists(name, container):
    for i in range(0,4):  #First 24 frames = standard animation
        frame=PhotoImage(file=name+"%s.png"%(i))
        container.append(frame)
    

def Initialise_images():
    Pstrings_in_lists("Sprites/Player_dUSpace", Player_dUSpace)
    Pstrings_in_lists("Sprites/Player_dUGoal", Player_dUGoal) 
    Pstrings_in_lists("Sprites/Player_dLSpace", Player_dLSpace) 
    Pstrings_in_lists("Sprites/Player_dLGoal", Player_dLGoal) 
    Pstrings_in_lists("Sprites/Player_dRSpace", Player_dRSpace) 
    Pstrings_in_lists("Sprites/Player_dRGoal", Player_dRGoal)
    
    Mstrings_in_lists("Sprites/Wall_nTorch", Player_nTorch) 


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

def inb_short(
        Day_or_Night, player, X, 
        Y, Player_Up, Player_Left, 
        Player_Down, Player_Right, i):
    frame=Orientation(
        Day_or_Night, player, 
        Player_Up, Player_Left, 
        Player_Down, Player_Right, i)
    Maps.map_matrix[player.X+X][player.Y+Y].config(image=frame)

#Returns the old space to normal 
def erased(player, X, Y, old_text, old_area):
    Maps.map_matrix[player.X+X][player.Y+Y].config(image=old_area)

    
def S2S_G2G(
        root, Day_or_Night, player, 
        X, Y, Player_Up, Player_Left, 
        Player_Down, Player_Right, 
        old_text, old_area):


    #Old box frame
    root.after(
        10, inb_short, Day_or_Night, player, 
        X, Y, Player_Up, Player_Left, 
        Player_Down, Player_Right, 25) 
    
    root.after(
        10,erased, player, X, Y, old_text, old_area)
    
    #New box frame1
    root.after(
        10, inb_short, Day_or_Night, player, 
        0, 0, Player_Up, Player_Left, 
        Player_Down, Player_Right, 26)


def S2G_G2S(
        root, Day_or_Night, player, X, Y, 
        Player_Up1, Player_Up2, Player_Left1, 
        Player_Left2, Player_Down1, Player_Down2, 
        Player_Right1, Player_Right2, old_text, 
        old_area):
    root.after(
        0, inb_short, Day_or_Night, player, 
        X, Y, Player_Up1, Player_Left1, 
        Player_Down1, Player_Right1, 24)
    root.after(
        10, inb_short, Day_or_Night, player, 
        X, Y, Player_Up1, Player_Left1, 
        Player_Down1, Player_Right1, 25)
    root.after(
        10, erased, player, 
        X, Y, old_text, old_area)
    root.after(
        10,inb_short, Day_or_Night, player, 
        0, 0, Player_Up2, Player_Left2, 
        Player_Down2, Player_Right2, 26)
    root.after(
        30, inb_short, Day_or_Night, player, 
        0, 0, Player_Up2, Player_Left2, 
        Player_Down2, Player_Right2, 27)

    
#Space to goal or goal to space (player)
#Happens in Goal_Space function (Control_Logic module). 
# =>Step_over is one step behind since the function's called after.
def Animation_Inbetweens(
        root, Day_or_Night, player, 
        X, Y, Player_Up1, Player_Up2, 
        Player_Left1, Player_Left2, 
        Player_Down1, Player_Down2, 
        Player_Right1, Player_Right2, 
        old_text, old_area):

    #Space to goal - Box
    if(player.step_over==0 
            and  Maps.map_matrix[player.X-X][player.Y-Y].cget("text")==Var.CoG):
        S2G_G2S(
            root, Day_or_Night, player, X, Y, 
            Player_Up1, Player_Up2, Player_Left1, 
            Player_Left2, Player_Down1, Player_Down2, 
            Player_Right1, Player_Right2, old_text, old_area)
        print("cbaba %s"%player.step_over)

    #Goal to space - Box
    elif(player.step_over==1 
            and Maps.map_matrix[player.X-X][player.Y-Y].cget("text")==Var.CoS):
        S2G_G2S(
            root, Day_or_Night, player, X, Y, 
            Player_Up1, Player_Up2, 
            Player_Left1, Player_Left2, 
            Player_Down1, Player_Down2, 
            Player_Right1, Player_Right2, 
            old_text, old_area)
        print("cmama %s"%player.step_over)  

    #Space to goal - No box
    elif(player.step_over==0 
            and Maps.map_matrix[player.X-X][player.Y-Y].cget("text")==Var.Goal): 
        S2G_G2S(
            root, Day_or_Night, player, X, Y, 
            Player_Up1, Player_Up2, 
            Player_Left1, Player_Left2, 
            Player_Down1, Player_Down2, 
            Player_Right1, Player_Right2, 
            old_text, old_area)
        print("baba %s"%player.step_over)
    #Space to goal - No box
    elif(player.step_over==1 
            and Maps.map_matrix[player.X-X][player.Y-Y].cget("text")==Var.Space):
        S2G_G2S(
            root, Day_or_Night, player, X, Y, 
            Player_Up1, Player_Up2, 
            Player_Left1, Player_Left2, 
            Player_Down1, Player_Down2, 
            Player_Right1, Player_Right2, 
            old_text, old_area)
        print("mama %s"%player.step_over)    
    #Space to Space or Goal to Goal - No box
    else:                                                                                                                                      
        S2S_G2G(
            root, Day_or_Night, player, X, Y, 
            Player_Up1, Player_Left1, 
            Player_Down1, Player_Right1, 
            old_text, old_area)    
        print("sda")

#Inbetween for player
def Inbetween_Order(
        root, Day_or_Night, player, 
        Player_Up1, Player_Up2, 
        Player_Left1, Player_Left2, 
        Player_Down1, Player_Down2, 
        Player_Right1, Player_Right2, 
        old_text, old_area):
    match player.Button_Pressed:
        case "Up":
            Animation_Inbetweens(
                root, Day_or_Night, player, 
                0, 1, Player_Up1, Player_Up2, 
                Player_Left1, Player_Left2, 
                Player_Down1, Player_Down2, 
                Player_Right1, Player_Right2, 
                old_text, old_area)
        case "Left":
            Animation_Inbetweens(
                root, Day_or_Night, player, 
                1, 0, Player_Up1, Player_Up2, 
                Player_Left1, Player_Left2, 
                Player_Down1, Player_Down2, 
                Player_Right1, Player_Right2, 
                old_text, old_area)
        case "Down":
            Animation_Inbetweens(
                root, Day_or_Night, player, 
                0, -1, Player_Up1, Player_Up2, 
                Player_Left1, Player_Left2, 
                Player_Down1, Player_Down2, 
                Player_Right1, Player_Right2, 
                old_text, old_area)
        case "Right":
            Animation_Inbetweens(
                root, Day_or_Night, player, 
                -1, 0, Player_Up1, Player_Up2, 
                Player_Left1, Player_Left2, 
                Player_Down1, Player_Down2, 
                Player_Right1, Player_Right2, 
                old_text, old_area)


def Animation_Player(root, Day_or_Night, player, cf):
    if (player.inbetween==0):
        if(cf<23): 

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

            
    root.after(10, Animation_Player, root, Day_or_Night, player, cf)

def Animation_Map(root, Day_or_Night, cf):
    if (Day_or_Night.mode==0):
        if(cf<4):
            for i in range(1,17):
                for j in range (1,15): 
                    if (Maps.map_matrix[j][i].cget("text")==Var.Torch):
                        Maps.map_matrix[j][i].config(image=Player_nTorch[cf])
                    if (Maps.map_matrix[j][i].cget("text")==Var.Goal):
                        Maps.map_matrix[j][i].config(image=Player_nTorch[cf])
            cf += 1
        else:
            cf=0
    root.after(100,Animation_Map, root, Day_or_Night, cf)
        
        



        
        
