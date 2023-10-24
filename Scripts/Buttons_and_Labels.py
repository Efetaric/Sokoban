from tkinter import *
import Maps
import Control_Logic
import Save_Load

#>>>> Buttons
CONTROL_buttons=[[],[],[],[]] #Stores the control buttons
Save_buttons=[[],[],[],[]] #Stores the save buttons
Load_buttons=[[],[],[],[]] #Stores the load buttons


def btn_pressed(button, player): #Stores the pressed button id
    player.Button_Pressed=button

    #>>>> Control buttons & the state of controls and next
def control_button(Lower_Courtain, x, y, player, map, hml, which_button, Next_btn, i): #The control buttons
    CONTROL_buttons[i]= Button(Lower_Courtain, bg="Purple", width=5, height=1, command=lambda: [btn_pressed("%s"%which_button, player), Control_Logic.walk( player, map, hml), Turn_Off(map.Left_Spots, Next_btn)])
    CONTROL_buttons[i].place(x=x, y=y)

def Turn_Off(Left_Spots, Next_btn): #Disables the control buttons & activates next button
    if(Left_Spots==0):
        for i in range (0,4):
            CONTROL_buttons[i].config(state=DISABLED, bg="Grey")
        Next_btn.config(state=NORMAL, bg="Yellow")

def Turn_On(Next_btn): #Activates the control buttons & disables next button
    for i in range (0,4):
        CONTROL_buttons[i].config(state=NORMAL, bg="Purple")
    Next_btn.config(state=DISABLED, bg="Grey")
    #Control buttons & the state of controls and next <<<<<<<<<<<<<<<<<<<<<


def menu_buttons(canvas, menu, inst, save, load, Lower_Courtain, User, Current_Map, hml, cl, player, map): #Spawn the menu buttons
    Start = Button(menu, text="Start", font=("Comic Sans", 20),bg="Green", width = '10', height = '1', command=lambda:[btn_pressed("Start", User), Maps.Maps_order(User, Current_Map),
                                                                                    hml_cl(hml,cl,player,map), canvas.pack(), Lower_Courtain.pack(side=BOTTOM), menu.forget()])
    Start.place(x=165,y=30)
    Instructions = Button(menu, text="Instructions", font=("Comic Sans", 20),bg="Green", width = '10', height = '1', command=lambda:[btn_pressed("Instructions", User),
                                                                                    isl_menu(menu, inst, player), inst.pack(), menu.forget()])
    Instructions.place(x=165,y=100)
    Save = Button(menu, text="Save", font=("Comic Sans", 20),bg="Green", width = '10', height = '1', command=lambda:[btn_pressed("Save", User), 
                                                                                    isl_menu(menu, save, player),save.pack(), menu.forget()])
    Save.place(x=165,y=170)
    Load = Button(menu, text="Load", font=("Comic Sans", 20),bg="Green", width = '10', height = '1', command=lambda:[btn_pressed("Load", User), 
                                                                                    isl_menu(menu, load, player),load.pack(), menu.forget(), Save_Load.Great_Load()])
    Load.place(x=165,y=240)
    menu.pack()#Loads the buttons



def initialize_every_button(canvas, menu, inst, save, load, Lower_Courtain, player, Current_Map, User): #the main function from this module

    #>>>> LOWER SIDE
    cl = Label(Lower_Courtain, font=("MS Sans Serif", "15", "bold"), height=1, width=10, bg="Black", fg="Yellow")
    cl.place(x=5,y=6) #CL/ Current level
    hml = Label(Lower_Courtain, font=("MS Sans Serif", "15", "bold"), height=1, width=10, bg="Black", fg="Red")
    hml.place(x=5,y=42) #HML/ How many left
    
    Next_btn = Button(Lower_Courtain, bg="Grey", fg="Black", text="Next", width = '10', height = '1', state=DISABLED, command=lambda: [Maps.Maps_order(player, Current_Map),hml_cl(hml, cl, player, Current_Map),
                                                                                Turn_On(Next_btn)])
    Next_btn.place(x=360,y=8)    

    Menu = Button(Lower_Courtain, bg="Black", fg="White", text="Menu", width = '10', height = '1', command=lambda: [btn_pressed("Menu", player),Turn_On( Next_btn), #this button returns from game to menu
                                                                                                                     canvas.forget(),Lower_Courtain.forget(), menu.pack()])
    Menu.place(x=360,y=44)
    
        #>>>> Places the control buttons
    control_button(Lower_Courtain, 227, 0, player, Current_Map, hml, "Up", Next_btn, 0)
    control_button(Lower_Courtain, 183, 25, player, Current_Map, hml, "Left", Next_btn, 1)
    control_button(Lower_Courtain, 227, 50, player, Current_Map, hml, "Down", Next_btn, 2)
    control_button(Lower_Courtain, 271, 25, player, Current_Map, hml, "Right", Next_btn, 3)
        #Places the control buttons <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    #Lower Side <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    
    instructions(inst)
    Save_Load_buttons(save, load, User, player) #Save canvas pack
    menu_buttons(canvas, menu, inst, save, load, Lower_Courtain, User, Current_Map, hml, cl, player, Current_Map)
    

def hml_cl(hml,cl,player,map): #This turns "boxes" into "box" if the new map has only one box & changes the changes the current level sign
    cl.config(text="Level: %d"%player.level)
    if(map.Left_Spots==1):
        hml.config(text="1 box left")
    else:
        hml.config(text="%d boxes left"%map.Left_Spots)
#Buttons <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#>>>> Instructions
def inst_label(inst, text, size, bold, height, width, bg, fg, x, y): #This is creates the label for instructions
    inst = Label(inst, text=text,font=("MS Sans Serif", size, bold), height=height, width=width, bg=bg, fg=fg)
    inst.place(x=x,y=y) #HML/ How many left

def isl_menu(menu, inst, player):# this generates a button which can return from instructions, save or load to main menu
    isl_menu = Button(bg="Black", fg="White", text="Menu", width = '10', height = '1', command=lambda: [btn_pressed("Menu", player), inst.forget(), isl_menu.destroy(), menu.pack()])
    isl_menu.place(x=360,y=390)

def details(inst, number, color1, color2, color3, background, y, sign): #this function makes labels witth the colors (instructions)
    inst_label(inst, number, 16, "normal", 1, 2, background, "Black", 0, y)
    inst_label(inst, "", 15, "bold", 1, 2, color1, "Black", 30, y) #box
    inst_label(inst, "+", 16, "normal", 1, 2, background, "Black", 60, y)
    inst_label(inst, "", 15, "bold", 1, 2, color2, "Black", 90, y) #box
    inst_label(inst, sign, 16, "normal", 1, 2, background, "Black", 120, y)
    inst_label(inst, "", 15, "bold", 1, 2, color3, "Black", 150, y) #box

def instructions(inst):
    inst_label(inst, "Instructions", 17, "bold", 1, 10,"Darkgrey", "Black", 80, 5) #title
    #>>>> Goal
    inst_label(inst, "Goal", 16, "bold", 1, 4, "Darkgrey", "Black", -4, 55)
    inst_label(inst, "- Turn every  ", 16, "normal", 1, 10, "Darkgrey", "Black", 0, 90)
    inst_label(inst, "", 15, "bold", 1, 2, "Magenta", "Black", 120, 90) #box
    inst_label(inst, "into", 16, "normal", 1, 3, "Darkgrey", "Black", 152, 90)
    inst_label(inst, "", 15, "bold", 1, 2, "Purple", "Black", 192, 90) #box
    #Goal <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    #>>>> Details
    inst_label(inst, "Details", 16, "bold", 1, 5, "Darkgrey", "Black", 0, 125)
    details(inst, "1.", "Magenta", "Grey", "Magenta", "Darkgrey", 160, "=") #Chest + Space
    details(inst, "2.", "Magenta", "Lime", "Purple", "Darkgrey", 195, "=") #Chest + Goal
    details(inst, "3.", "Purple", "Grey", "Magenta", "Darkgrey", 230, "=") #Chest out of goal

        #>>>> Forbidden cases
    inst_label(inst, "222", 16, "normal", 4, 40, "Red", "Black", 0, 265)
    details(inst, "4.", "Magenta", "Midnightblue", "Black", "Red", 265, "or") #Chest out of goal()
    inst_label(inst, "Not", 16, "normal", 1, 8, "Red", "Black", 190, 265)
    details(inst, "5.", "Purple", "Midnightblue", "Black", "Red", 300, "or") #Chest out of goal()
    inst_label(inst, "allowed", 16, "normal", 1, 8, "Red", "Black", 190, 300)
        # Forbidden cases <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    #Details <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#Instructions <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#>>>> Save and Load functions - I couldn't merge load with save for some reason
def save_btn(save, User, player, Slot, x, y, i):
     Save_buttons[i] = Button(save, text=Slot, font=("Comic Sans", 20),bg="Green", width = '10', height = '1', command=lambda:[btn_pressed(Slot, User), Save_Load.Save(player)])
     Save_buttons[i].place(x=x ,y=y)

def load_btn(load, User, player, Slot, x, y, i):
    Load_buttons[i] = Button(load, text=Slot, font=("Comic Sans", 20),bg="Green", width = '10', height = '1', command=lambda:[btn_pressed(Slot, User), Save_Load.Load(player)])
    Load_buttons[i].place(x=x ,y=y)

def Save_Load_buttons(save, load, User, player): #Saves the current level
    save_btn(save, User, player, "Slot1", 25, 100, 0)
    save_btn(save, User, player, "Slot2", 100, 190, 1)
    save_btn(save, User, player, "Slot3", 225, 100, 2)
    save_btn(save, User, player, "Slot4", 300, 190, 3)

    load_btn(load, User, player, "Slot1", 25, 100, 0)
    load_btn(load, User, player, "Slot2", 100, 190, 1)
    load_btn(load, User, player, "Slot3", 225, 100, 2)
    load_btn(load, User, player, "Slot4", 300, 190, 3)

      
    
    

    
    



  

