from tkinter import *
import Maps 
import Control_Logic

Button_Pressed="No_Button_Pressed"
map_matrix=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] #This contains the map (it turns into a 15x15 matrix)
Color_Border="Black"    #bcolor
Color_Obstacle="Midnightblue"   #ocolor 
Color_Space="Grey"      #scolor
Color_Goal="Lime"       #gcolor
Color_Player="Yellow"   #pcolor
Color_Chest="Magenta"   #ccolor
MapOrder=0

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
def btn_pressed(button):
    global Button_Pressed
    Button_Pressed=button

#start button
def begin(matrix, player, pcolor):
    #Destroys the current buttons
    Start.destroy()
    Tutorial.destroy()
    #Places the Arena
    canvas= Canvas(root, bg="Black")
    Maps.Standard_map(canvas, map_matrix, Color_Border, Color_Space) #Make the outter border
    Maps.Maps_order(Button_Pressed, map_matrix, Color_Obstacle, Color_Space, Color_Goal, player)#Generates the first map (tutorial or not)  
    canvas.pack()
    #Places the buttons
    Up_btn = Button(bg="Purple", width = '5', height = '1', command=lambda: [btn_pressed("Up"), Control_Logic.walk(matrix, player, Color_Border, Color_Obstacle, Color_Space, Color_Player, Color_Chest, Button_Pressed)])
    Up_btn.pack(side="top")
    Left_btn = Button(bg="Purple", width = '5', height = '1', command=lambda: [btn_pressed("Left"), Control_Logic.walk(matrix, player, Color_Border, Color_Obstacle, Color_Space, Color_Player, Color_Chest, Button_Pressed)])
    Left_btn.place(x=182,y=370)
    Down_btn = Button(bg="Purple", width = '5', height = '1', command=lambda: [btn_pressed("Down"), Control_Logic.walk(matrix, player, Color_Border, Color_Obstacle, Color_Space, Color_Player, Color_Chest, Button_Pressed)])
    Down_btn.pack(side="bottom")    
    Right_btn = Button(bg="Purple", width = '5', height = '1', command=lambda: [btn_pressed("Right"), Control_Logic.walk(matrix, player, Color_Border, Color_Obstacle, Color_Space, Color_Player, Color_Chest, Button_Pressed)])
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
position(root)
root.configure(background="Darkgrey")


#m1= Maps.tutorial_Map1(map_matrix, Color_Obstacle, Color_Space, Color_Goal)
#Game controls
User = Player(level=1,current_x=1,current_y=2)
Tutorial = Button(text="Tutorial", font=("Comic Sans", 20),bg="Green", width = '10', height = '1', command=lambda:[btn_pressed("Tutorial"), begin(map_matrix, User, Color_Player)])
Tutorial.place(x=165,y=20)
Start = Button(text="Start", font=("Comic Sans", 20),bg="Green", width = '10', height = '1', command=lambda:[btn_pressed("Start"), begin(map_matrix, User, Color_Player)])
Start.place(x=165,y=100)




root.mainloop()





