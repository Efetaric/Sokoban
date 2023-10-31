from tkinter import *
import Maps 
import Buttons_and_Labels


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

class Appearance: #This is for day and night mode
    def __init__(self, day_bg, night_bg, font_dColor, font_nColor, btn_dColor, btn_nColor, mode):
        self.day_bg=day_bg #day mode background
        self.night_bg=night_bg #night mode background
        self.font_dColor=font_dColor #day mode font
        self.font_nColor=font_nColor #night mode font
        self.btn_dColor=btn_dColor #button bg day mode
        self.btn_nColor=btn_nColor #button bg night mode
        self.menu_dColor=btn_nColor #menu day mode (in reverse with the menu buttons)
        self.menu_nColor=btn_dColor #menu night mode


        self.mode=mode
        self.background=day_bg
        self.font_color=font_dColor
        self.btn_color=btn_dColor
        self.menu_color=btn_dColor
        



    def night_or_day(self): #Changes everything
        if (self.mode<1):#day mode
            self.mode=1
            print("Day mode")
            self.background=self.day_bg
            self.font_color=self.font_dColor
            self.btn_color=self.btn_dColor
            self.menu_color=self.menu_dColor
            return self.background, self.font_color, self.btn_color, self.menu_color
        else:             #night mode
            self.mode=0
            print("Night mode")
            self.background=self.night_bg
            self.font_color=self.font_nColor
            self.btn_color=self.btn_nColor
            self.menu_color=self.menu_nColor
            return self.background, self.font_color, self.btn_color, self.menu_color

        
      


    
            

######################################################################

User = Player(level=1,current_x=1,current_y=2, step_over=0, Button_Pressed='No_Button_Pressed')
Current_Map = Map(Boxes=0, Left_Spots=0, Color_Border="Grey", Color_Obstacle="Navy", Color_Space="Steelblue", Color_Goal="Aquamarine", Color_Player="Yellow", Color_Chest="Violetred", Color_Transform="Purple")
Mode = Appearance(day_bg ="Darkgrey", night_bg="Black", font_dColor="Black", font_nColor="Darkgrey", btn_dColor="deep sky blue", btn_nColor="Yellow", mode=1) 

root = Tk()
root.config()
position(root)
root.configure(background=Mode.background)

canvas = Canvas(bg="Black", highlightthickness=0)
Maps.Standard_map(canvas, Current_Map)#Generates the map





Buttons_and_Labels.initialize_every_button(root, canvas, User, Current_Map, User, Mode)

#button bg  si shifter



root.mainloop()


