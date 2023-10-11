from tkinter import *
import Maps
import Control_Logic

CONTROL_buttons=[[],[],[],[]] #Stores the control buttons


def btn_pressed(button, player): #Stores the pressed button id
    player.Button_Pressed=button

def control_button(color, width, height, x, y, which_btn, player, matrix, map, hml, button, Next_btn, i): #The control buttons
     button[i] = Button(bg=color, width = width, height = height, command=lambda: [btn_pressed(which_btn, player), Control_Logic.walk(matrix, player, map, hml), Turn_Off(CONTROL_buttons, map.Left_Spots, Next_btn)])
     button[i].place(x=x, y=y)
     print(button[i])

def Turn_Off(CONTROL_buttons, Left_Spots, Next_btn): #Disables the control buttons & activates next button
    if(Left_Spots==0):
        for i in range (0,4):
            CONTROL_buttons[i].config(state=DISABLED, bg="Grey")
        Next_btn.config(state=NORMAL, bg="Yellow")

def Turn_On(Next_btn): #Activates the control buttons & disables next button
    for i in range (0,4):
        CONTROL_buttons[i].config(state=NORMAL, bg="Purple")
    Next_btn.config(state=DISABLED, bg="Grey")
        


def menu_buttons(main, canvas, Lower_Courtain, map_matrix, User, Current_Map, hml, cl, player, map, Next_btn):  
    Start = Button(text="Start", font=("Comic Sans", 20),bg="Green", width = '10', height = '1', command=lambda:[btn_pressed("Start", User), main(map_matrix, User, Current_Map),
                                                                                    hml_cl(hml,cl,player,map), Turn_On(Next_btn), canvas.pack(), Lower_Courtain.pack_forget(),
                                                                                    Start.destroy(),Instructions.destroy(),Save.destroy(),Load.destroy()])
    Start.place(x=165,y=30)
        
    Instructions = Button(text="Instructions", font=("Comic Sans", 20),bg="Green", width = '10', height = '1', command=lambda:[btn_pressed("Instructions", User),
                                                                                    Start.destroy(),Instructions.destroy(),Save.destroy(),Load.destroy()])
    Instructions.place(x=165,y=100)

    Save = Button(text="Save", font=("Comic Sans", 20),bg="Green", width = '10', height = '1', command=lambda:[btn_pressed("Save", User),
                                                                                    Start.destroy(),Instructions.destroy(),Save.destroy(),Load.destroy()])
    Save.place(x=165,y=170)

    Load = Button(text="Load", font=("Comic Sans", 20),bg="Green", width = '10', height = '1', command=lambda:[btn_pressed("Load", User),
                                                                                    Start.destroy(),Instructions.destroy(),Save.destroy(),Load.destroy()])
    Load.place(x=165,y=240)

    

def buttons(window, canvas, matrix, player, map, User, main, map_matrix, Current_Map):

    cl = Label(window, font=("MS Sans Serif", "15", "bold"), height=1, width=10, bg="Black", fg="Yellow")
    cl.place(x=40,y=385) #CL/ Current level
    hml = Label(window, font=("MS Sans Serif", "15", "bold"), height=1, width=10, bg="Black", fg="Red")
    hml.place(x=40,y=345) #HML/ How many left

    Next_btn = Button(bg="Grey", width = '10', height = '1', state=DISABLED, command=lambda: [Maps.Maps_order(matrix, player, map),hml_cl(hml, cl, player, map),
                                                                                Turn_On(Next_btn)])
    Next_btn.place(x=360,y=355)    

    Menu = Button(bg="Black", text="Menu", width = '10', height = '1', command=lambda: [btn_pressed("Menu", player), canvas.forget(),Lower_Courtain.pack(side=BOTTOM),
                                                                                menu_buttons(main, canvas, Lower_Courtain, map_matrix, User, Current_Map, hml, cl, player, map, Next_btn)])
    Menu.place(x=360,y=390)

    #Places the control buttons
    control_button("Purple", "5", "1", 226.3, 345, "Up", player, matrix, map, hml, CONTROL_buttons, Next_btn, 0)
    control_button("Purple", "5", "1", 182, 370, "Left", player, matrix, map, hml, CONTROL_buttons, Next_btn, 1)
    control_button("Purple", "5", "1", 226.3, 395, "Down", player, matrix, map, hml, CONTROL_buttons, Next_btn, 2)
    control_button("Purple", "5", "1", 270, 370, "Right", player, matrix, map, hml, CONTROL_buttons, Next_btn, 3) 

    Lower_Courtain = Canvas(bg="Darkgrey", width=500, height=73) #This canvas hides the control buttons, the labels and the next/menu buttons
    Lower_Courtain.pack(side=BOTTOM)
    menu_buttons(main, canvas, Lower_Courtain, map_matrix, User, Current_Map, hml, cl, player, map, Next_btn)



  
    

def hml_cl(hml,cl,player,map): #This turns "boxes" into "box" if the new map has only one box & changes the changes the current level sign
    cl.config(text="Level: %d"%player.level)
    if(map.Left_Spots==1):
        hml.config(text="1 box left")
    else:
        hml.config(text="%d boxes left"%map.Left_Spots)

