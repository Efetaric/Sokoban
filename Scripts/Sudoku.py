from tkinter import *
import Maps 
import Control_Logic


map_matrix=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] #This contains the map (it turns into a 15x15 matrix)
buttons=[[],[],[],[]] #Stores the control buttons

def position(root): #Sets the main window

    width = 500
    height = 420

    # screen width and height
    screen_width = root.winfo_screenwidth() # width of the screen
    screen_height = root.winfo_screenheight() # height of the screen

    # screen coordonates for root
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    root.geometry('%dx%d+%d+%d' % (width, height, x, y))



def btn_pressed(button, player): #Stores the pressed button id
    player.Button_Pressed=button

def main_button(color, width, height, x, y, which_btn, player, matrix, map, hml, button, Next_btn, i): #The control buttons
     button[i] = Button(bg=color, width = width, height = height, command=lambda: [btn_pressed(which_btn, player), Control_Logic.walk(matrix, player, map, hml), Turn_Off(buttons, map.Left_Spots, Next_btn)])
     button[i].place(x=x, y=y)
     print(button[i])

def Turn_Off(buttons, Left_Spots, Next_btn): #Disables the control buttons & activates next button
    if(Left_Spots==0):
        for i in range (0,4):
            buttons[i].config(state=DISABLED, bg="Grey")
        Next_btn.config(state=NORMAL, bg="Yellow")

def Turn_On(buttons, Next_btn): #Activates the control buttons & disables next button
    for i in range (0,4):
        buttons[i].config(state=NORMAL, bg="Purple")
    Next_btn.config(state=DISABLED, bg="Grey")

        
def hml_cl(hml,cl,player,map): #This turns "boxes" into "box" if the new map has only one box & changes the changes the current level sign
    cl.config(text="Level: %d"%player.level)
    if(map.Left_Spots==1):
        hml.config(text="1 box left")
    else:
        hml.config(text="%d boxes left"%map.Left_Spots)



def main(window, matrix, player, map): #The main function
    #Places the Arena
    canvas= Canvas(root, bg="Black")
    Maps.Standard_map(canvas, matrix, player, map)#Generates the map
    canvas.pack()

    if (User.Button_Pressed=="Start"): #When the player plays start this if turns the "%s boxes left" into "1 box left" & shows displays the current level
        current_level=Label(window, text="Level 1", font=("MS Sans Serif", "15", "bold"), height=1, width=10, bg="Black", fg="Yellow")
        current_level.place(x=40,y=385)
        how_many_left=Label(window, text="1 box left", font=("MS Sans Serif", "15", "bold"), height=1, width=10, bg="Black", fg="Red")
        how_many_left.place(x=40,y=345)
    
    #This function goes to the next map and destroys the button
    Next_btn = Button(bg="Yellow", width = '10', height = '1', command=lambda: [Maps.Maps_order(matrix, player, map),hml_cl(how_many_left, current_level, player, map),
                                                                                Turn_On(buttons, Next_btn)])
    Next_btn.place(x=360,y=355)
    #Places the buttons
    main_button("Purple", "5", "1", 226.3, 345, "Up", player, matrix, map, how_many_left, buttons, Next_btn, 0)
    main_button("Purple", "5", "1", 182, 370, "Left", player, matrix, map, how_many_left, buttons, Next_btn, 1)
    main_button("Purple", "5", "1", 226.3, 395, "Down", player, matrix, map, how_many_left, buttons, Next_btn, 2)
    main_button("Purple", "5", "1", 270, 370, "Right", player, matrix, map, how_many_left, buttons, Next_btn, 3) 


class Player:
    def __init__(self, level, current_x, current_y, step_over, Button_Pressed):
        self.level = level
        self.current_x = current_x
        self.current_y = current_y
        self.step_over = step_over
        self.Button_Pressed = Button_Pressed

class Map:
    def __init__(self, Boxes, Left_Spots, Color_Border, Color_Obstacle, Color_Space, Color_Goal, Color_Player, Color_Chest, Color_Transform):
        self.Boxes = Boxes #this is used only to initialize the left spots, but it can be used to print "x boxes out of y boxes"
        self.Left_Spots = Left_Spots
        self.Color_Border = Color_Border
        self.Color_Obstacle = Color_Obstacle
        self.Color_Space = Color_Space
        self.Color_Goal = Color_Goal
        self.Color_Player = Color_Player
        self.Color_Chest = Color_Chest
        self.Color_Transform = Color_Transform

######################################################################

root = Tk()
root.config(background="Silver")
position(root)
root.configure(background="Darkgrey")


User = Player(level=1,current_x=1,current_y=2, step_over=0, Button_Pressed='No_Button_Pressed')
Current_Map = Map(Boxes=0, Left_Spots=0, Color_Border="Black", Color_Obstacle="Midnightblue", Color_Space="Grey", Color_Goal="Lime", Color_Player="Yellow", Color_Chest="Magenta", Color_Transform="Purple")
#Start button
Start = Button(text="Start", font=("Comic Sans", 20),bg="Green", width = '10', height = '1', command=lambda:[btn_pressed("Start", User), Start.destroy(), main(root, map_matrix, User, Current_Map)])
Start.place(x=165,y=30)
Instructions = Button(text="Instructions", font=("Comic Sans", 20),bg="Green", width = '10', height = '1', command=lambda:[btn_pressed("Instructions", User), Start.destroy(), main(root, map_matrix, User, Current_Map)])
Instructions.place(x=165,y=100)



root.mainloop()



