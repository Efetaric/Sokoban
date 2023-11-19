from tkinter import *
import Maps
import Control_Logic
import Save_Load
import Events

Menu_buttons=[[],[],[],[],[]] #Stores the menu buttons
CONTROL_buttons=[[],[],[],[]] #Stores the control buttons
Save_buttons=[[],[],[],[]] #Stores the save buttons
Load_buttons=[[],[],[],[]] #Stores the load buttons
Instructions_btns=[]



def btn_pressed(button, player): #Stores the pressed button id
    player.Button_Pressed=button

# Control buttons & the state of controls and next
#The control buttons
def control_button(
        root, Lower_Courtain, x, y, player, map, 
        hml, which_button, Next_btn, Reset_btn, i): 
    
    CONTROL_buttons[i] = Button(
        Lower_Courtain, 
        bg="Purple", 
        width=5, 
        height=1, 
        command=lambda: [
            btn_pressed("%s"%which_button, player), 
            Control_Logic.walk(root, player, map, hml), 
            Turn_Off(map.Left_Spots, Next_btn, Reset_btn)])
    CONTROL_buttons[i].place(x=x, y=y)



#Disables the control buttons/ reset & activates next button
def Turn_Off(Left_Spots, Next_btn, Reset_btn): 
    if(Left_Spots==0):
        for i in range (0,4):
            CONTROL_buttons[i].config(state=DISABLED, bg="Grey")
        Reset_btn.config(state=DISABLED, bg="Grey")
        Next_btn.config(state=NORMAL, bg="Yellow")
        
#Activates the control buttons/ reset & disables next button
def Turn_On(Next_btn, Reset_btn): 
    for i in range (0,4):
        CONTROL_buttons[i].config(state=NORMAL, bg="Purple")
    Reset_btn.config(state=NORMAL, bg="Yellow")
    Next_btn.config(state=DISABLED, bg="Grey")

#These 2 are used to block keyboard control when the map is not projected.
def Ready(Day_or_Night):
    Day_or_Night.state="Ready"
def Not_ready(Day_or_Night):
    Day_or_Night.state="Not_Ready"

#Control buttons & the state of controls and next <<<<<<<<<<<<<<<<<<<<<
def always_1(player): #Level resets to 1
    player.level=1

def continue_on_off(player):#turns on/ off the continue button
    if (player.level==1):
        Menu_buttons[0].config(state=DISABLED)
    else:
        Menu_buttons[0].config(state=NORMAL)

#Loads/ Reloads the correct map.
def refresh_or_change(player, Day_or_Night):
    if (Day_or_Night.Left_Spots==0):
        Maps.Maps_order(player, Day_or_Night)
    else:
        Maps.Refresh(Day_or_Night)
    
#Spawn the menu buttons
def menu_buttons(root, canvas, menu, inst, save, load, 
                 Lower_Courtain, hml, cl, Menu, player, 
                 Day_or_Night, Day, Night): 

    night_mode = Button(
        text="D/N", image=Day_or_Night.Mode, 
        width = '25', height = '25', 
        command=lambda: [
            Day_or_Night.Switch(Day, Night),
            Maps.Refresh(Day_or_Night),
            color_shifter(root, menu, inst, 
                          save, load, 
                          Lower_Courtain,
                          player, Day_or_Night)])
    night_mode.place(x=0, y=0)
    
    Menu_buttons[0]=(Button(
        menu, text="Continue", 
        font=("Comic Sans", 20),
        bg=Day_or_Night.btn_Color, 
        fg=Day_or_Night.fg, width = '10',
        height = '1', state=DISABLED, 
        command=lambda:[
            btn_pressed("Continue", player),
            refresh_or_change(player, Day_or_Night),
            hml_cl(hml,cl,player,Day_or_Night), 
            canvas.pack(), menu.forget(),
            Lower_Courtain.place(x=42, y=520), 
            Menu.place(x=402,y=570), 
            Ready(Day_or_Night)]))
    Menu_buttons[0].place(x=165,y=30)

    Menu_buttons[1] = Button(
        menu, text="New game", 
        font=("Comic Sans", 20), 
        bg=Day_or_Night.btn_Color, 
        fg=Day_or_Night.fg, 
        width = '10', height = '1', 
        command=lambda:[
            btn_pressed("New game", player), 
            always_1(player), 
            Maps.Maps_order(player, Day_or_Night), 
            hml_cl(hml,cl,player,Day_or_Night), 
            canvas.pack(), menu.forget(), 
            Lower_Courtain.place(x=42, y=520), 
            Menu.place(x=402,y=570), menu.forget(),
            Ready(Day_or_Night)])
    Menu_buttons[1].place(x=165,y=100)

    Menu_buttons[2] = Button(
        menu, text="Instructions", 
        font=("Comic Sans", 20),
        bg=Day_or_Night.btn_Color, 
        fg=Day_or_Night.fg, width = '10',
        height = '1', command=lambda:[
            btn_pressed("Instructions", player), 
            inst.pack(), Menu.place(x=400,y=570),
            menu.forget()])
    Menu_buttons[2].place(x=165,y=170)

    Menu_buttons[3] = Button(
        menu, text="Save", font=("Comic Sans", 20),
        bg=Day_or_Night.btn_Color, fg=Day_or_Night.fg,
        width = '10', height = '1', command=lambda:[
            btn_pressed("Save", player), save.pack(), 
            Menu.place(x=360,y=570), menu.forget()])
    Menu_buttons[3].place(x=165,y=240)

    Menu_buttons[4] = Button(
        menu, text="Load", font=("Comic Sans", 20),
        bg=Day_or_Night.btn_Color, fg=Day_or_Night.fg, 
        width = '10', height = '1', command=lambda:[
            btn_pressed("Load", player), 
            Save_Load.Great_Load(), 
            Menu.place(x=360,y=570), 
            load.pack(), menu.forget()])
    Menu_buttons[4].place(x=165,y=310)

#the main function from this module
def initialize_every_button(root, canvas, player, 
                            Day_or_Night, Day, Night): 

    #Generates the menu canvas
    menu = Canvas(
        bg=Day_or_Night.bg, 
        width=500, height=425, 
        highlightthickness=0) 
    menu.pack()#Loads the buttons
    #Generates the instructions canvas
    inst = Canvas(
        bg=Day_or_Night.bg,
        width=300, height=325, 
        highlightthickness=0)
    #Generates the save canvas 
    save = Canvas(
        bg=Day_or_Night.bg, 
        width=500, height=470, 
        highlightthickness=0)
    #Generates the load canvas 
    load = Canvas(
        bg=Day_or_Night.bg, 
        width=500, height=470, 
        highlightthickness=0) 
    #Used for the control buttons, the labels and the next/restart buttons
    Lower_Courtain = Canvas(
        bg=Day_or_Night.bg, 
        width=500, height=75,
        highlightthickness=0) 


    cl = Label(
        Lower_Courtain, font=("MS Sans Serif", "15", "bold"), 
        height=1, width=10, bg=Day_or_Night.menu_Color, fg="Purple", 
        highlightthickness=1, highlightbackground="Purple")
    cl.place(x=5,y=6) #CL/ Current level
    hml = Label(
        Lower_Courtain, font=("MS Sans Serif", "15", "bold"), 
        height=1, width=10, bg=Day_or_Night.menu_Color, fg="Red",
        highlightthickness=1, highlightbackground="Purple")
    hml.place(x=5,y=42) #HML/ How many left
    
    Next_btn = Button(
        Lower_Courtain, bg="Grey", fg=Day_or_Night.fg, 
        text="Next", width = '10', height = '1', state=DISABLED, 
        command=lambda:[
            Maps.Maps_order(player, Day_or_Night),
            hml_cl(hml, cl, player, Day_or_Night), 
            Turn_On(Next_btn, Reset_btn), 
            Ready(Day_or_Night)])
    Next_btn.place(x=360,y=0)  

    Reset_btn = Button(
        Lower_Courtain, bg="Yellow", fg=Day_or_Night.fg, 
        text="Reset", width = '10', height = '1', command=lambda:[
            Maps.Maps_order(player, Day_or_Night)])
    Reset_btn.place(x=360,y=26)   

    Menu = Button(
        root, bg=Day_or_Night.btn_Color, fg=Day_or_Night.fg, 
        text="Menu", width = '10', height = '1', command=lambda: [
            btn_pressed("Menu", player), 
            Turn_On(Next_btn, Reset_btn), 
            canvas.forget(), load.forget(), 
            Lower_Courtain.place_forget(), 
            inst.forget(), save.forget(), 
            continue_on_off(player), 
            menu.pack(), Menu.place_forget(),
            Not_ready(Day_or_Night)])
    
    # Places the control buttons
    control_button(
        root, Lower_Courtain, 227, 0, 
        player, Day_or_Night, hml, 
        "Up", Next_btn, Reset_btn, 0)
    control_button(
        root, Lower_Courtain, 183, 25, 
        player, Day_or_Night, hml, 
        "Left", Next_btn, Reset_btn, 1)
    control_button(
        root, Lower_Courtain, 227, 50, 
        player, Day_or_Night, hml, 
        "Down", Next_btn, Reset_btn, 2)
    control_button(
        root, Lower_Courtain, 271, 25, 
        player, Day_or_Night, hml, 
        "Right", Next_btn, Reset_btn, 3)

    
    instructions(
        inst, 
        Day_or_Night.bg, 
        Day_or_Night.fg)

    Save_Load_buttons(
        save, load, player, 
        Day_or_Night) 
    menu_buttons(
        root, canvas, menu, inst, 
        save, load, Lower_Courtain, 
        hml, cl, Menu, player, 
        Day_or_Night, Day, Night)
    
    #Contains every event
    Events.Events(
        root, canvas, Lower_Courtain, 
        player, Day_or_Night, 
        hml, cl, Next_btn, Reset_btn)

#Turns "boxes" into "box" (if map has 1 box) & changes the current level sign
def hml_cl(hml,cl,player,map): 
    cl.config(text="Level: %d"%player.level)
    if(map.Left_Spots==1):
        hml.config(text="1 box left")
    else:
        hml.config(text="%d boxes left"%map.Left_Spots)
    
#Changes day/night mode
def color_shifter(
        root, menu, inst, save, 
        load, Lower_Courtain, 
        player, Day_or_Night):
    #canvases
    root.config(bg=Day_or_Night.bg)
    menu.config(bg=Day_or_Night.bg)
    inst.config(bg=Day_or_Night.bg)
    save.config(bg=Day_or_Night.bg)
    load.config(bg=Day_or_Night.bg)
    Lower_Courtain.config(bg=Day_or_Night.bg)

    for i in Menu_buttons:
        i.config(bg=Day_or_Night.btn_Color)
    for i in Instructions_btns:
        i.config(bg=Day_or_Night.bg)
    for i in Save_buttons:
        i.config(bg=Day_or_Night.btn_Color, fg=Day_or_Night.fg)
    for i in Load_buttons:
        i.config(bg=Day_or_Night.btn_Color, fg=Day_or_Night.fg)
    
    #Maps.Maps_order(player, Day_or_Night)

    


#Instructions
#Dynamic instructions labels - Nightmode changes it
def inst_label(
        inst, text, size, 
        bold, height, width, 
        bg, fg, x, y): 
    inst = Label(
        inst, text=text,font=("MS Sans Serif", size, bold), 
        height=height, width=width, bg=bg, fg=fg)
    inst.place(x=x,y=y)
    Instructions_btns.append(inst)
#Static instructions label - Nightmode doesn't change it
def static_inst_label(
        inst, text, size, 
        bold, height, width, 
        bg, fg, x, y): 
    inst = Label(
        inst, text=text,font=("MS Sans Serif", size, bold), 
        height=height, width=width, bg=bg, fg=fg)
    inst.place(x=x,y=y)

#this function makes labels witth the colors (instructions)
def details(
        inst, number, color1, color2, 
        color3, bg, fg, y, sign): 
    inst_label(
        inst, number, 16, "normal", 
        1, 2, bg, fg, 0, y)
    static_inst_label(
        inst, "", 15, "bold", 1, 2, 
        color1, fg, 30, y) #box
    inst_label(
        inst, "+", 16, "normal", 1, 2, 
        bg, fg, 60, y)
    static_inst_label(
        inst, "", 15, "bold", 1, 2, 
        color2, fg, 90, y) #box
    inst_label(
        inst, sign, 16, "normal", 1, 2, 
        bg, fg, 120, y)
    static_inst_label(
        inst, "", 15, "bold", 1, 2, 
        color3, fg, 150, y) #box

def instructions(inst, bg, fg):
    inst_label(
        inst, "Instructions", 17, "bold", 
        1, 10, bg, fg, 80, 5) #title
    
    # Goal
    inst_label(
        inst, "Goal", 16, "bold", 
        1, 4, bg, fg, -4, 55)
    inst_label(
        inst, "- Turn every  ", 16, 
        "normal", 1, 10, bg, fg, 0, 90)
    static_inst_label(
        inst, "", 15, "bold", 1, 2, 
        "Purple", fg, 120, 90) #box
    inst_label(inst, "into", 16, "normal", 
               1, 3, bg, fg, 152, 90)
    static_inst_label(
        inst, "", 15, "bold", 1, 2, 
        "Magenta", fg, 192, 90) #box


    # Details
    inst_label(
        inst, "Details", 16, "bold", 
        1, 5, bg, fg, 0, 125)
    details(
        inst, "1.", "Purple", "Green", 
        "Purple", bg, fg, 160, "=") #Chest + Space
    details(
        inst, "2.", "Purple", "Yellow", 
        "Magenta", bg, fg, 195, "=") #Chest + Goal
    details(
        inst, "3.", "Magenta", "Green", 
        "Purple", bg, fg, 230, "=") #Chest out of goal

        # Forbidden cases
    inst_label(
        inst, "222", 16, "normal", 
        4, 40, bg, fg, 0, 265) #constant
    details(
        inst, "4.", "Purple", "Darkgrey", 
        "Red", bg, fg, 265, "or") #Chest out of goal()
    inst_label(
        inst, "Not", 16, "normal", 
        1, 8, bg, fg, 190, 265) #constant
    details(
        inst, "5.", "Magenta", "Darkgrey", 
        "Red", bg, fg, 300, "or") #Chest out of goal()
    inst_label(
        inst, "allowed", 16, "normal", 1, 8, 
        bg, fg, 190, 300) #constant


# Save and Load functions - I couldn't merge load with save for some reason
def save_btn(
        save, load, player, 
        Day_or_Night, Slot, 
        x, y, i):
     Save_buttons[i] = Button(
         save, text=Slot, font=("Comic Sans", 33), 
         bg=Day_or_Night.btn_Color, fg=Day_or_Night.fg, 
         width = '8', height = '1', command=lambda:[
             btn_pressed(Slot, player), 
             Save_Load.Save(player)])
     Save_buttons[i].place(x=x ,y=y)

     Load_buttons[i] = Button(
         load, text=Slot, font=("Comic Sans", 33), 
         bg=Day_or_Night.btn_Color, fg=Day_or_Night.fg, 
         width = '8', height = '1', command=lambda:[
             btn_pressed(Slot, player), 
             Save_Load.Load(player)])
     Load_buttons[i].place(x=x ,y=y)


#Saves the current level
def Save_Load_buttons(
        save, load, player, 
        Day_or_Night): 
    save_btn(
        save, load, player, 
        Day_or_Night, "Slot1", 
        135, 10, 0)
    save_btn(
        save, load, player, 
        Day_or_Night, "Slot2", 
        135, 130, 1)
    save_btn(
        save, load, player, 
        Day_or_Night, "Slot3", 
        135, 250, 2)
    save_btn(
        save, load, player, 
        Day_or_Night, "Slot4", 
        135, 370, 3)

      
    
    

    
    



  

