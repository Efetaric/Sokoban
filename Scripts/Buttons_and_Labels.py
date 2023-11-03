from tkinter import *
import Maps
import Control_Logic
import Save_Load
import Classes


CONTROL_buttons=[[],[],[],[]] #Stores the control buttons
Save_buttons=[[],[],[],[]] #Stores the save buttons
Load_buttons=[[],[],[],[]] #Stores the load buttons
Instructions_btns=[]



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


def menu_buttons(root, canvas, menu, inst, save, load, Lower_Courtain, hml, cl, Menu, player, Day_or_Night, Day, Night): #Spawn the menu buttons

    night_mode = Button(text="D/N", image=Day_or_Night.Mode, width = '25', height = '25', command=lambda: [Day_or_Night.Switch(Day,Night),color_shifter(root, menu, inst, save, load, Lower_Courtain, Start, Instructions, Save, Load, Menu, player, Day_or_Night)])
    night_mode.place(x=0, y=0)
    Start = Button(menu, text="Start", font=("Comic Sans", 20),bg=Day_or_Night.btn_Color, fg=Day_or_Night.fg, width = '10', height = '1', command=lambda:[btn_pressed("Start", player), Maps.Maps_order(player, Day_or_Night),
                                                                                    hml_cl(hml,cl,player,Day_or_Night), canvas.pack(), Lower_Courtain.pack(side=BOTTOM), Menu.place(x=360,y=390), menu.forget()])
    Start.place(x=165,y=30)
    Instructions = Button(menu, text="Instructions", font=("Comic Sans", 20),bg=Day_or_Night.btn_Color, fg=Day_or_Night.fg, width = '10', height = '1', command=lambda:[btn_pressed("Instructions", player), inst.pack(), Menu.place(x=360,y=390), menu.forget()])
    Instructions.place(x=165,y=100)
    Save = Button(menu, text="Save", font=("Comic Sans", 20),bg=Day_or_Night.btn_Color, fg=Day_or_Night.fg, width = '10', height = '1', command=lambda:[btn_pressed("Save", player), save.pack(), Menu.place(x=360,y=390), menu.forget()])
    Save.place(x=165,y=170)
    Load = Button(menu, text="Load", font=("Comic Sans", 20),bg=Day_or_Night.btn_Color, fg=Day_or_Night.fg, width = '10', height = '1', command=lambda:[btn_pressed("Load", player), load.pack(), Menu.place(x=360,y=390), menu.forget(), Save_Load.Great_Load()])
    Load.place(x=165,y=240)


def initialize_every_button(root, canvas, player, Day_or_Night, Day, Night): #the main function from this module
    #These contain the buttons and labels


    menu = Canvas(bg=Day_or_Night.bg, width=500, height=325, highlightthickness=0) #Generates the menu canvas
    menu.pack()#Loads the buttons
    inst = Canvas(bg=Day_or_Night.bg, width=300, height=325, highlightthickness=0) #Generates the instructions canvas
    save = Canvas(bg=Day_or_Night.bg, width=500, height=325, highlightthickness=0) #Generates the save canvas
    load = Canvas(bg=Day_or_Night.bg, width=500, height=325, highlightthickness=0) #Generates the load canvas
    Lower_Courtain = Canvas(bg=Day_or_Night.bg, width=500, height=75, highlightthickness=0) #This canvas hides the control buttons, the labels and the next/menu buttons

    #>>>> LOWER SIDE
    cl = Label(Lower_Courtain, font=("MS Sans Serif", "15", "bold"), height=1, width=10, bg=Day_or_Night.menu_Color, fg="Purple", highlightthickness=1, highlightbackground="Purple")
    cl.place(x=5,y=6) #CL/ Current level
    hml = Label(Lower_Courtain, font=("MS Sans Serif", "15", "bold"), height=1, width=10, bg=Day_or_Night.menu_Color, fg="Red", highlightthickness=1, highlightbackground="Purple")
    hml.place(x=5,y=42) #HML/ How many left
    
    Next_btn = Button(Lower_Courtain, bg="Grey", fg=Day_or_Night.fg, text="Next", width = '10', height = '1', state=DISABLED, command=lambda: [Maps.Maps_order(player, Day_or_Night),hml_cl(hml, cl, player, Day_or_Night), Turn_On(Next_btn)])
    Next_btn.place(x=360,y=8)    

    Menu = Button(root, bg=Day_or_Night.btn_Color, fg=Day_or_Night.fg, text="Menu", width = '10', height = '1', command=lambda: [btn_pressed("Menu", player), Turn_On( Next_btn), canvas.forget(),Lower_Courtain.forget(), inst.forget(), save.forget(), load.forget(),
                                                                                    menu.pack(), Menu.place_forget()])
    
    #>>>> Places the control buttons
    control_button(Lower_Courtain, 227, 0, player, Day_or_Night, hml, "Up", Next_btn, 0)
    control_button(Lower_Courtain, 183, 25, player, Day_or_Night, hml, "Left", Next_btn, 1)
    control_button(Lower_Courtain, 227, 50, player, Day_or_Night, hml, "Down", Next_btn, 2)
    control_button(Lower_Courtain, 271, 25, player, Day_or_Night, hml, "Right", Next_btn, 3)
        #Places the control buttons <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    #Lower Side <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    
    instructions(inst, Day_or_Night, Day_or_Night.bg, Day_or_Night.fg)
    Save_Load_buttons(save, load, player, Day_or_Night) #Save canvas pack
    menu_buttons(root, canvas, menu, inst, save, load, Lower_Courtain, hml, cl, Menu, player, Day_or_Night, Day, Night)


def hml_cl(hml,cl,player,map): #This turns "boxes" into "box" if the new map has only one box & changes the current level sign
    cl.config(text="Level: %d"%player.level)
    if(map.Left_Spots==1):
        hml.config(text="1 box left")
    else:
        hml.config(text="%d boxes left"%map.Left_Spots)
    
def color_shifter(root, menu, inst, save, load, Lower_Courtain, Start, Instructions, Save, Load, Menu, player, Day_or_Night):#Changes day/night mode
    #canvases
    root.config(bg=Day_or_Night.bg)
    menu.config(bg=Day_or_Night.bg)
    inst.config(bg=Day_or_Night.bg)
    save.config(bg=Day_or_Night.bg)
    load.config(bg=Day_or_Night.bg)
    Lower_Courtain.config(bg=Day_or_Night.bg)
    #menu buttons
    Start.config(bg=Day_or_Night.btn_Color)
    Instructions.config(bg=Day_or_Night.btn_Color)
    Save.config(bg=Day_or_Night.btn_Color)
    Load.config(bg=Day_or_Night.btn_Color)
    Menu.config(bg=Day_or_Night.menu_Color)

    for i in Instructions_btns:
        i.config(bg=Day_or_Night.bg)
    for i in Save_buttons:
        i.config(bg=Day_or_Night.btn_Color, fg=Day_or_Night.fg)
    for i in Load_buttons:
        i.config(bg=Day_or_Night.btn_Color, fg=Day_or_Night.fg)
    
    Maps.Maps_order(player, Day_or_Night)


#>>>> Instructions
def inst_label(inst, text, size, bold, height, width, bg, fg, x, y): #Dynamic instruction labels - Nightmode changes it
    inst = Label(inst, text=text,font=("MS Sans Serif", size, bold), height=height, width=width, bg=bg, fg=fg)
    inst.place(x=x,y=y)
    Instructions_btns.append(inst)
def static_inst_label(inst, text, size, bold, height, width, bg, fg, x, y): #Static instruction label - Nightmode doesn't change it
    inst = Label(inst, text=text,font=("MS Sans Serif", size, bold), height=height, width=width, bg=bg, fg=fg)
    inst.place(x=x,y=y)


def details(inst, number, color1, color2, color3, bg, fg, y, sign): #this function makes labels witth the colors (instructions)
    inst_label(inst, number, 16, "normal", 1, 2, bg, fg, 0, y)
    static_inst_label(inst, "", 15, "bold", 1, 2, color1, fg, 30, y) #box
    inst_label(inst, "+", 16, "normal", 1, 2, bg, fg, 60, y)
    static_inst_label(inst, "", 15, "bold", 1, 2, color2, fg, 90, y) #box
    inst_label(inst, sign, 16, "normal", 1, 2, bg, fg, 120, y)
    static_inst_label(inst, "", 15, "bold", 1, 2, color3, fg, 150, y) #box

def instructions(inst, map, bg, fg):
    inst_label(inst, "Instructions", 17, "bold", 1, 10, bg, fg, 80, 5) #title
    #>>>> Goal
    inst_label(inst, "Goal", 16, "bold", 1, 4, bg, fg, -4, 55)
    inst_label(inst, "- Turn every  ", 16, "normal", 1, 10, bg, fg, 0, 90)
    static_inst_label(inst, "", 15, "bold", 1, 2, "Purple", fg, 120, 90) #box
    inst_label(inst, "into", 16, "normal", 1, 3, bg, fg, 152, 90)
    static_inst_label(inst, "", 15, "bold", 1, 2, "Magenta", fg, 192, 90) #box
    #Goal <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    #>>>> Details
    inst_label(inst, "Details", 16, "bold", 1, 5, bg, fg, 0, 125)
    details(inst, "1.", "Purple", "Green", "Purple", bg, fg, 160, "=") #Chest + Space
    details(inst, "2.", "Purple", "Yellow", "Magenta", bg, fg, 195, "=") #Chest + Goal
    details(inst, "3.", "Magenta", "Green", "Purple", bg, fg, 230, "=") #Chest out of goal

        #>>>> Forbidden cases
    inst_label(inst, "222", 16, "normal", 4, 40, bg, fg, 0, 265) #constant
    details(inst, "4.", "Purple", "Darkgrey", "Red", bg, fg, 265, "or") #Chest out of goal()
    inst_label(inst, "Not", 16, "normal", 1, 8, bg, fg, 190, 265) #constant
    details(inst, "5.", "Magenta", "Darkgrey", "Red", bg, fg, 300, "or") #Chest out of goal()
    inst_label(inst, "allowed", 16, "normal", 1, 8, bg, fg, 190, 300) #constant
        # Forbidden cases <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    #Details <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#Instructions <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#>>>> Save and Load functions - I couldn't merge load with save for some reason
def save_btn(save, player, Day_or_Night, Slot, x, y, i,):
     Save_buttons[i] = Button(save, text=Slot, font=("Comic Sans", 20),bg=Day_or_Night.btn_Color, fg=Day_or_Night.fg, width = '10', height = '1', command=lambda:[btn_pressed(Slot, player), Save_Load.Save(player)])
     Save_buttons[i].place(x=x ,y=y)

def load_btn(load, player, Day_or_Night, Slot, x, y, i):
    Load_buttons[i] = Button(load, text=Slot, font=("Comic Sans", 20),bg=Day_or_Night.btn_Color, fg=Day_or_Night.fg, width = '10', height = '1', command=lambda:[btn_pressed(Slot, player), Save_Load.Load(player)])
    Load_buttons[i].place(x=x ,y=y)

def Save_Load_buttons(save, load, player, Day_or_Night): #Saves the current level
    save_btn(save, player, Day_or_Night, "Slot1", 25, 100, 0)
    save_btn(save, player, Day_or_Night, "Slot2", 100, 190, 1)
    save_btn(save, player, Day_or_Night, "Slot3", 225, 100, 2)
    save_btn(save, player, Day_or_Night, "Slot4", 300, 190, 3)

    load_btn(load, player, Day_or_Night, "Slot1", 25, 100, 0)
    load_btn(load, player, Day_or_Night, "Slot2", 100, 190, 1)
    load_btn(load, player, Day_or_Night, "Slot3", 225, 100, 2)
    load_btn(load, player, Day_or_Night, "Slot4", 300, 190, 3)

      
    
    

    
    



  

