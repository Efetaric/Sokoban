from tkinter import *
import Maps
import Control_Logic

Button_Pressed="No_Button_Pressed"
map_matrix=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] #This will store the data (it'll become 15x15)
Color_Border="Black" #bcolor
Color_Obstacles="Darkblue"
Color_Space="Dimgrey"
Color_Player="Yellow"
Color_Goal="Lime"
Color_Chest="Magenta"
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

      
#Stores the pressed button id
def btn_pressed(button):
    global Button_Pressed
    Button_Pressed=button

#start button
def begin(matrix, player, bcolor, ocolor, scolor, pcolor, gcolor, ccolor):
    #destroys start and tutorial button
    Start.destroy()        
    Tutorial.destroy()
    #creates the canvas
    canvas = Canvas(bg="Grey")
    Maps.Standard_map(canvas, matrix, bcolor, scolor) ##Generates the Emtpy space and the borders
    Maps.Maps_order(Button_Pressed, matrix, ocolor, scolor, gcolor, player) ##Generates the first map (tutorial or start)
    canvas.pack(side="top")
    
    #creates the buttons
    Up_btn = Button(bg="Purple", width = '5', height = '1', command=lambda: [btn_pressed("Up"), Control_Logic.walk(matrix, player, bcolor, ocolor, scolor, pcolor, ccolor, Button_Pressed)])
    Up_btn.pack(side="top")
    Left_btn = Button(bg="Purple", width = '5', height = '1', command=lambda: [btn_pressed("Left"), Control_Logic.walk(matrix, player, bcolor, ocolor, scolor, pcolor, ccolor, Button_Pressed)])
    Left_btn.place(x=182,y=370)
    Down_btn = Button(bg="Purple", width = '5', height = '1', command=lambda: [btn_pressed("Down"), Control_Logic.walk(matrix, player, bcolor, ocolor, scolor, pcolor, ccolor, Button_Pressed)])
    Down_btn.place(x=227,y=395)    
    Right_btn = Button(bg="Purple", width = '5', height = '1', command=lambda: [btn_pressed("Right"), Control_Logic.walk(matrix, player, bcolor, ocolor, scolor, pcolor, ccolor, Button_Pressed)])
    Right_btn.place(x=270,y=370)
    #Places the player
    matrix[player.current_x][player.current_y].config(bg=pcolor)

    

class Player:
    def __init__(self, level, current_x, current_y):
        self.level = level
        self.current_x = current_x
        self.current_y = current_y

######################################################################
root = Tk()
root.config(background="Silver")
position(root)


User =Player(level=1,current_x=1,current_y=1)
#Game controls
Tutorial = Button(text="Tutorial", font=("Comic Sans", 20),bg="Green", width = '10', height = '1', command=lambda:[btn_pressed("Tutorial"), begin(map_matrix, User, Color_Border, Color_Obstacles, Color_Space, Color_Player, Color_Goal, Color_Chest)])
Tutorial.place(x=165,y=20)
Start = Button(text="Start", font=("Comic Sans", 20),bg="Green", width = '10', height = '1', command=lambda:[btn_pressed("Start"), begin(map_matrix, User, Color_Border, Color_Obstacles, Color_Space, Color_Player, Color_Goal, Color_Chest)])
Start.place(x=165,y=100)

root.mainloop()



