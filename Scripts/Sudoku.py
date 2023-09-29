from tkinter import *
import Maps 
import Control_Logic


map_matrix=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] #This contains the map (it turns into a 15x15 matrix)

#Sets the main window
def position(root):

    width = 500
    height = 420

    # screen width and height
    screen_width = root.winfo_screenwidth() # width of the screen
    screen_height = root.winfo_screenheight() # height of the screen

    # screen coordonates for root
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    root.geometry('%dx%d+%d+%d' % (width, height, x, y))


#Stores the Button id
def btn_pressed(button, player):
    player.Button_Pressed=button

#Main function
def main(window, matrix, player, map):
    #Places the Arena
    canvas= Canvas(root, bg="Black")
    Maps.Maps_order(canvas, matrix, player, map)#Generates the map
    canvas.pack()
    #Shows on a label how many boxes are left
    if (User.Button_Pressed=="Start"): #starts the game
        current_level=Label(window, text="Level 1", font=("MS Sans Serif", "15", "bold"), height=1, width=10, bg="Black", fg="Yellow")
        current_level.place(x=40,y=385)
        how_many_left=Label(window, text="1 box left", font=("MS Sans Serif", "15", "bold"), height=1, width=10, bg="Black", fg="Red")
        how_many_left.place(x=40,y=345)
    #Places the buttons
    Up_btn = Button(bg="Purple", width = '5', height = '1', command=lambda: [btn_pressed("Up", player), Control_Logic.walk(matrix, player, map, how_many_left)
                                                                                ,ON_OFF(map, Up_btn, Left_btn, Down_btn, Right_btn, Next_btn)])
    Up_btn.pack(side="top")
    Left_btn = Button(bg="Purple", width = '5', height = '1', command=lambda: [btn_pressed("Left", player), Control_Logic.walk(matrix, player, map, how_many_left)
                                                                                ,ON_OFF(map, Up_btn, Left_btn, Down_btn, Right_btn, Next_btn)])
    Left_btn.place(x=182,y=370)
    Down_btn = Button(bg="Purple", width = '5', height = '1', command=lambda: [btn_pressed("Down", player), Control_Logic.walk(matrix, player, map, how_many_left)
                                                                                ,ON_OFF(map, Up_btn, Left_btn, Down_btn, Right_btn, Next_btn)])
    Down_btn.pack(side="bottom")    
    Right_btn = Button(bg="Purple", width = '5', height = '1', command=lambda: [btn_pressed("Right", player), Control_Logic.walk(matrix, player, map, how_many_left)
                                                                                ,ON_OFF(map, Up_btn, Left_btn, Down_btn, Right_btn, Next_btn)])
    Right_btn.place(x=270,y=370)
    #This function goes to the next map and destroys the button
    Next_btn = Button(bg="Yellow", width = '10', height = '1', command=lambda: [Maps.Maps_order(canvas, matrix, player, map), ON_OFF(map, Up_btn, Left_btn, Down_btn, Right_btn, Next_btn)
                                                                                ,hml_cl(how_many_left,current_level,player, map)])
    Next_btn.place(x=360,y=355)

def ON_OFF(map,UP,LEFT,DOWN,RIGHT,NEXT):
    if(map.Left_Spots==0):
        UP.config(state=DISABLED, bg="Grey")
        LEFT.config(state=DISABLED, bg="Grey")
        DOWN.config(state=DISABLED, bg="Grey")
        RIGHT.config(state=DISABLED, bg="Grey")
        NEXT.config(state=NORMAL, bg="Yellow")
    else:
        UP.config(state=NORMAL, bg="Purple")
        LEFT.config(state=NORMAL, bg="Purple")
        DOWN.config(state=NORMAL, bg="Purple")
        RIGHT.config(state=NORMAL, bg="Purple")
        NEXT.config(state=NORMAL, bg="Grey")
        
def hml_cl(hml,cl,player,map):
    cl.config(text="Level: %d"%player.level)
    if(map.Left_Spots==1):
        hml.config(text="1 box left")
    else:
        hml.config(text="%d boxes left"%map.Left_Spots)


    

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
Start.place(x=165,y=100)


root.mainloop()



