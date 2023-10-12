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


def menu_buttons(main, canvas, inst, Lower_Courtain, map_matrix, User, Current_Map, hml, cl, player, map, Next_btn):  
    Start = Button(text="Start", font=("Comic Sans", 20),bg="Green", width = '10', height = '1', command=lambda:[btn_pressed("Start", User), main(map_matrix, User, Current_Map),
                                                                                    hml_cl(hml,cl,player,map), Turn_On(Next_btn), canvas.pack(), Lower_Courtain.pack_forget(),
                                                                                    Start.destroy(),Instructions.destroy(),Save.destroy(),Load.destroy()])
    Start.place(x=165,y=30)
        
    Instructions = Button(text="Instructions", font=("Comic Sans", 20),bg="Green", width = '10', height = '1', command=lambda:[btn_pressed("Instructions", User),
                                                                                    inst_menu(main, canvas, inst, Lower_Courtain, map_matrix, User, Current_Map, hml, cl, player, map, Next_btn),
                                                                                    inst.pack(), canvas.forget(),Start.destroy(),Instructions.destroy(),Save.destroy(),Load.destroy()])
    Instructions.place(x=165,y=100)

    Save = Button(text="Save", font=("Comic Sans", 20),bg="Green", width = '10', height = '1', command=lambda:[btn_pressed("Save", User),
                                                                                    Start.destroy(),Instructions.destroy(),Save.destroy(),Load.destroy()])
    Save.place(x=165,y=170)

    Load = Button(text="Load", font=("Comic Sans", 20),bg="Green", width = '10', height = '1', command=lambda:[btn_pressed("Load", User),
                                                                                    Start.destroy(),Instructions.destroy(),Save.destroy(),Load.destroy()])
    Load.place(x=165,y=240)


def inst_label(inst, text, size, bold, height, width, bg, fg, x, y):
    hml = Label(inst, text=text,font=("MS Sans Serif", size, bold), height=height, width=width, bg=bg, fg=fg)
    hml.place(x=x,y=y) #HML/ How many left


def buttons(window, canvas, inst, matrix, player, map, User, main, map_matrix, Current_Map):


    instructions(inst)

    ###############LOWER SIDE
    cl = Label(window, font=("MS Sans Serif", "15", "bold"), height=1, width=10, bg="Black", fg="Yellow")
    cl.place(x=40,y=385) #CL/ Current level
    hml = Label(window, font=("MS Sans Serif", "15", "bold"), height=1, width=10, bg="Black", fg="Red")
    hml.place(x=40,y=345) #HML/ How many left
    
    Next_btn = Button(bg="Grey", fg="Black", text="Next", width = '10', height = '1', state=DISABLED, command=lambda: [Maps.Maps_order(matrix, player, map),hml_cl(hml, cl, player, map),
                                                                                Turn_On(Next_btn)])
    Next_btn.place(x=360,y=355)    

    Menu = Button(bg="Black", fg="White", text="Menu", width = '10', height = '1', command=lambda: [btn_pressed("Menu", player), canvas.forget(),Lower_Courtain.pack(side=BOTTOM),
                                                                                menu_buttons(main, canvas, inst, Lower_Courtain, map_matrix, User, Current_Map, hml, cl, player, map, Next_btn)])
    Menu.place(x=360,y=390)

    #Places the control buttons
    control_button("Purple", "5", "1", 226.3, 345, "Up", player, matrix, map, hml, CONTROL_buttons, Next_btn, 0)
    control_button("Purple", "5", "1", 182, 370, "Left", player, matrix, map, hml, CONTROL_buttons, Next_btn, 1)
    control_button("Purple", "5", "1", 226.3, 395, "Down", player, matrix, map, hml, CONTROL_buttons, Next_btn, 2)
    control_button("Purple", "5", "1", 270, 370, "Right", player, matrix, map, hml, CONTROL_buttons, Next_btn, 3) 

    Lower_Courtain = Canvas(bg="Darkgrey", width=500, height=75, highlightthickness=0) #This canvas hides the control buttons, the labels and the next/menu buttons
    Lower_Courtain.pack(side=BOTTOM)
    menu_buttons(main, canvas, inst, Lower_Courtain, map_matrix, User, Current_Map, hml, cl, player, map, Next_btn)


def hml_cl(hml,cl,player,map): #This turns "boxes" into "box" if the new map has only one box & changes the changes the current level sign
    cl.config(text="Level: %d"%player.level)
    if(map.Left_Spots==1):
        hml.config(text="1 box left")
    else:
        hml.config(text="%d boxes left"%map.Left_Spots)

#Instructions

def inst_menu(main, canvas, inst, Lower_Courtain, map_matrix, User, Current_Map, hml, cl, player, map, Next_btn):# this generates the button which returns from  instructions to menu
    inst_Menu = Button(bg="Black", fg="White", text="Menu", width = '10', height = '1', command=lambda: [btn_pressed("Menu", player), inst.forget(), inst_Menu.destroy(),
                                                                                menu_buttons(main, canvas, inst, Lower_Courtain, map_matrix, User, Current_Map, hml, cl, player, map, Next_btn)])
    inst_Menu.place(x=360,y=390)

def details(inst, number, color1, color2, color3, background, y, sign):
    inst_label(inst, number, 16, "normal", 1, 2, background, "Black", 0, y)
    inst_label(inst, "", 15, "bold", 1, 2, color1, "Black", 30, y) #box
    inst_label(inst, "+", 16, "normal", 1, 2, background, "Black", 60, y)
    inst_label(inst, "", 15, "bold", 1, 2, color2, "Black", 90, y) #box
    inst_label(inst, sign, 16, "normal", 1, 2, background, "Black", 120, y)
    inst_label(inst, "", 15, "bold", 1, 2, color3, "Black", 150, y) #box

def instructions(inst):
    
    #title
    inst_label(inst, "Instructions", 17, "bold", 1, 10,"Darkgrey", "Black", 80, 5)
    #Goal
    inst_label(inst, "Goal", 16, "bold", 1, 4, "Darkgrey", "Black", -4, 55)
    inst_label(inst, "- Turn every  ", 16, "normal", 1, 10, "Darkgrey", "Black", 0, 90)
    inst_label(inst, "", 15, "bold", 1, 2, "Magenta", "Black", 120, 90) #box
    inst_label(inst, "into", 16, "normal", 1, 3, "Darkgrey", "Black", 152, 90)
    inst_label(inst, "", 15, "bold", 1, 2, "Purple", "Black", 192, 90) #box
    #Details
    inst_label(inst, "Details", 16, "bold", 1, 5, "Darkgrey", "Black", 0, 125)
    details(inst, "1.", "Magenta", "Grey", "Magenta", "Darkgrey", 160, "=") #Chest + Space
    details(inst, "2.", "Magenta", "Lime", "Purple", "Darkgrey", 195, "=") #Chest + Goal
    details(inst, "3.", "Purple", "Grey", "Magenta", "Darkgrey", 230, "=") #Chest out of goal
    #Forbidden cases
    inst_label(inst, "222", 16, "normal", 4, 40, "Red", "Black", 0, 265)
    details(inst, "4.", "Magenta", "Midnightblue", "Black", "Red", 265, "or") #Chest out of goal()
    inst_label(inst, "Not", 16, "normal", 1, 8, "Red", "Black", 190, 265)
    details(inst, "5.", "Purple", "Midnightblue", "Black", "Red", 300, "or") #Chest out of goal()
    inst_label(inst, "allowed", 16, "normal", 1, 8, "Red", "Black", 190, 300)

