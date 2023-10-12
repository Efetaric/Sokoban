from tkinter import *
import Maps 
import Buttons_and_Labels

map_matrix=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] #This contains the map (it turns into a 15x15 matrix)

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

        

def main(matrix, player, map): #The main function

    Maps.Maps_order(matrix, player, map)




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

User = Player(level=1,current_x=1,current_y=2, step_over=0, Button_Pressed='No_Button_Pressed')
Current_Map = Map(Boxes=0, Left_Spots=0, Color_Border="Black", Color_Obstacle="Midnightblue", Color_Space="Grey", Color_Goal="Lime", Color_Player="Yellow", Color_Chest="Magenta", Color_Transform="Purple")

root = Tk()
root.config(background="Silver")
position(root)
root.configure(background="Darkgrey")

canvas = Canvas(root, bg="Black")
Maps.Standard_map(canvas, map_matrix, Current_Map)#Generates the map
inst = Canvas(root, bg="Darkgrey", width=300, height=325, highlightthickness=0) #Generates the instructions
 



Buttons_and_Labels.buttons(root, canvas, inst, map_matrix, User, Current_Map, User, main, map_matrix, Current_Map)





root.mainloop()


