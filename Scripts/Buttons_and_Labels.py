from tkinter import *
import Maps
import Control_Logic
import Save_Load


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


def menu_buttons(root, canvas, menu, inst, save, load, Lower_Courtain, User, Current_Map, hml, cl, Menu, player, map, Mode): #Spawn the menu buttons
    night_mode = Button(bg="Grey", fg=Mode.font_color, text="Next", width = '10', height = '1', command=lambda: [Mode.night_or_day(), color_shifter(root, menu, inst, save, load, Lower_Courtain, Start, Instructions, Save, Load, Menu, Mode)])
    night_mode.pack(side=TOP)
    Start = Button(menu, text="Start", font=("Comic Sans", 20),bg=Mode.btn_color, fg=Mode.font_color, width = '10', height = '1', command=lambda:[btn_pressed("Start", User), Maps.Maps_order(User, Current_Map),
                                                                                    hml_cl(hml,cl,player,map), canvas.pack(), Lower_Courtain.pack(side=BOTTOM), Menu.place(x=360,y=390), menu.forget()])
    Start.place(x=165,y=30)
    Instructions = Button(menu, text="Instructions", font=("Comic Sans", 20),bg=Mode.btn_color, fg=Mode.font_color, width = '10', height = '1', command=lambda:[btn_pressed("Instructions", User), inst.pack(), Menu.place(x=360,y=390), menu.forget()])
    Instructions.place(x=165,y=100)
    Save = Button(menu, text="Save", font=("Comic Sans", 20),bg=Mode.btn_color, fg=Mode.font_color, width = '10', height = '1', command=lambda:[btn_pressed("Save", User), save.pack(), Menu.place(x=360,y=390), menu.forget()])
    Save.place(x=165,y=170)
    Load = Button(menu, text="Load", font=("Comic Sans", 20),bg=Mode.btn_color, fg=Mode.font_color, width = '10', height = '1', command=lambda:[btn_pressed("Load", User), load.pack(), Menu.place(x=360,y=390), menu.forget(), Save_Load.Great_Load()])
    Load.place(x=165,y=240)


def initialize_every_button(root, canvas, player, Current_Map, User, Mode): #the main function from this module
    #These contain the buttons and labels
    menu = Canvas(bg=Mode.background, width=500, height=325, highlightthickness=0) #Generates the menu canvas
    menu.pack()#Loads the buttons
    inst = Canvas(bg=Mode.background, width=300, height=325, highlightthickness=0) #Generates the instructions canvas
    save = Canvas(bg=Mode.background, width=500, height=325, highlightthickness=0) #Generates the save canvas
    load = Canvas(bg=Mode.background, width=500, height=325, highlightthickness=0) #Generates the load canvas
    Lower_Courtain = Canvas(bg=Mode.background, width=500, height=75, highlightthickness=0) #This canvas hides the control buttons, the labels and the next/menu buttons

    #>>>> LOWER SIDE
    cl = Label(Lower_Courtain, font=("MS Sans Serif", "15", "bold"), height=1, width=10, bg=Mode.menu_color, fg="Purple", highlightthickness=1, highlightbackground="Purple")
    cl.place(x=5,y=6) #CL/ Current level
    hml = Label(Lower_Courtain, font=("MS Sans Serif", "15", "bold"), height=1, width=10, bg=Mode.menu_color, fg="Red", highlightthickness=1, highlightbackground="Purple")
    hml.place(x=5,y=42) #HML/ How many left
    
    Next_btn = Button(Lower_Courtain, bg="Grey", fg=Mode.font_color, text="Next", width = '10', height = '1', state=DISABLED, command=lambda: [Maps.Maps_order(player, Current_Map),hml_cl(hml, cl, player, Current_Map), Turn_On(Next_btn)])
    Next_btn.place(x=360,y=8)    

    Menu = Button(root, bg=Mode.btn_color, fg=Mode.font_color, text="Menu", width = '10', height = '1', command=lambda: [btn_pressed("Menu", player), Turn_On( Next_btn), canvas.forget(),Lower_Courtain.forget(), inst.forget(), save.forget(), load.forget(),
                                                                                    menu.pack(), Menu.place_forget()])
    
    #>>>> Places the control buttons
    control_button(Lower_Courtain, 227, 0, player, Current_Map, hml, "Up", Next_btn, 0)
    control_button(Lower_Courtain, 183, 25, player, Current_Map, hml, "Left", Next_btn, 1)
    control_button(Lower_Courtain, 227, 50, player, Current_Map, hml, "Down", Next_btn, 2)
    control_button(Lower_Courtain, 271, 25, player, Current_Map, hml, "Right", Next_btn, 3)
        #Places the control buttons <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    #Lower Side <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    
    instructions(inst, Current_Map, Mode.background, Mode.font_color)
    Save_Load_buttons(save, load, User, player, Mode) #Save canvas pack
    menu_buttons(root, canvas, menu, inst, save, load, Lower_Courtain, User, Current_Map, hml, cl, Menu, player, Current_Map, Mode)


def hml_cl(hml,cl,player,map): #This turns "boxes" into "box" if the new map has only one box & changes the current level sign
    cl.config(text="Level: %d"%player.level)
    if(map.Left_Spots==1):
        hml.config(text="1 box left")
    else:
        hml.config(text="%d boxes left"%map.Left_Spots)
    
def color_shifter(root, menu, inst, save, load, Lower_Courtain, Start, Instructions, Save, Load, Menu, Mode):#Changes day/night mode
    #canvases
    root.config(bg=Mode.background)
    menu.config(bg=Mode.background)
    inst.config(bg=Mode.background)
    save.config(bg=Mode.background)
    load.config(bg=Mode.background)
    Lower_Courtain.config(bg=Mode.background)
    #menu buttons
    Start.config(bg=Mode.btn_color)
    Instructions.config(bg=Mode.btn_color)
    Save.config(bg=Mode.btn_color)
    Load.config(bg=Mode.btn_color)
    Menu.config(bg=Mode.menu_color)

    for i in Instructions_btns:
        i.config(bg=Mode.background)
    for i in Save_buttons:
        i.config(bg=Mode.btn_color, fg=Mode.font_color)
    for i in Load_buttons:
        i.config(bg=Mode.btn_color, fg=Mode.font_color)


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
    static_inst_label(inst, "", 15, "bold", 1, 2, map.Color_Chest, fg, 120, 90) #box
    inst_label(inst, "into", 16, "normal", 1, 3, bg, fg, 152, 90)
    static_inst_label(inst, "", 15, "bold", 1, 2, map.Color_Transform, fg, 192, 90) #box
    #Goal <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    #>>>> Details
    inst_label(inst, "Details", 16, "bold", 1, 5, bg, fg, 0, 125)
    details(inst, "1.", map.Color_Chest, map.Color_Space, map.Color_Chest, bg, fg, 160, "=") #Chest + Space
    details(inst, "2.", map.Color_Chest, map.Color_Goal, map.Color_Transform, bg, fg, 195, "=") #Chest + Goal
    details(inst, "3.", map.Color_Transform, map.Color_Space, map.Color_Chest, bg, fg, 230, "=") #Chest out of goal

        #>>>> Forbidden cases
    inst_label(inst, "222", 16, "normal", 4, 40, bg, fg, 0, 265) #constant
    details(inst, "4.", map.Color_Chest, map.Color_Obstacle, map.Color_Border, bg, fg, 265, "or") #Chest out of goal()
    inst_label(inst, "Not", 16, "normal", 1, 8, bg, fg, 190, 265) #constant
    details(inst, "5.", map.Color_Transform, map.Color_Obstacle, map.Color_Border, bg, fg, 300, "or") #Chest out of goal()
    inst_label(inst, "allowed", 16, "normal", 1, 8, bg, fg, 190, 300) #constant
        # Forbidden cases <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    #Details <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#Instructions <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#>>>> Save and Load functions - I couldn't merge load with save for some reason
def save_btn(save, User, player, Mode, Slot, x, y, i,):
     Save_buttons[i] = Button(save, text=Slot, font=("Comic Sans", 20),bg=Mode.btn_color, fg=Mode.font_color, width = '10', height = '1', command=lambda:[btn_pressed(Slot, User), Save_Load.Save(player)])
     Save_buttons[i].place(x=x ,y=y)

def load_btn(load, User, player, Mode, Slot, x, y, i):
    Load_buttons[i] = Button(load, text=Slot, font=("Comic Sans", 20),bg=Mode.btn_color, fg=Mode.font_color, width = '10', height = '1', command=lambda:[btn_pressed(Slot, User), Save_Load.Load(player)])
    Load_buttons[i].place(x=x ,y=y)

def Save_Load_buttons(save, load, User, player, Mode): #Saves the current level
    save_btn(save, User, player, Mode, "Slot1", 25, 100, 0)
    save_btn(save, User, player, Mode, "Slot2", 100, 190, 1)
    save_btn(save, User, player, Mode, "Slot3", 225, 100, 2)
    save_btn(save, User, player, Mode, "Slot4", 300, 190, 3)

    load_btn(load, User, player, Mode, "Slot1", 25, 100, 0)
    load_btn(load, User, player, Mode, "Slot2", 100, 190, 1)
    load_btn(load, User, player, Mode, "Slot3", 225, 100, 2)
    load_btn(load, User, player, Mode, "Slot4", 300, 190, 3)

      
    
    

    
    



  

