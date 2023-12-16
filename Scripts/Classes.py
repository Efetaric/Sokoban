from tkinter import *

#########################################################
class Player:
    def __init__(
            self, level, X, Y, step_over, 
            Button_Pressed):
        self.level = level
        self.X = X
        self.Y = Y
        self.step_over = step_over
        self.Button_Pressed = Button_Pressed


class Aspect: #This is for day and night mode
    def __init__(
            self, bg, fg, btn_Color, menu_Color, Mode,  
            Border_image, Border_image1, Torch_image,
            Obstacle_image, Space_image, Goal_image, 
            Player_image, Chest_space_image, 
            Chest_goal_image):
        #buttons/ canvas
        self.bg=bg #canvas background
        self.fg=fg #font
        self.btn_Color=btn_Color #button background
        self.menu_Color=menu_Color #menu color
        self.Mode=PhotoImage(file=Mode)

            #map
        self.Border_image = PhotoImage(file=Border_image)
        self.Border_image1 = PhotoImage(file=Border_image1)
        self.Torch_image = PhotoImage(file=Torch_image)
        self.Obstacle_image = PhotoImage(file=Obstacle_image)
        self.Space_image = PhotoImage(file=Space_image)
        self.Goal_image = PhotoImage(file=Goal_image)
        self.Player_image = PhotoImage(file=Player_image)
        self.Chest_space_image = PhotoImage(file=Chest_space_image)
        self.Chest_goal_image = PhotoImage(file=Chest_goal_image)



class Day_Night:
    def __init__(self, Boxes, Left_Spots, Day):
        #Day initialization
        #Buttons
        self.state="Not_Ready"#Keeps under control the control keys
        self.mode=1 #day=1, default is day
        self.Boxes = Boxes #Initializes the left spots
        self.Left_Spots = Left_Spots
        self.bg=Day.bg #canvas background
        self.fg=Day.fg #font
        self.btn_Color=Day.btn_Color #button background
        self.menu_Color=Day.menu_Color #menu color
        self.Mode=Day.Mode

        #map
        self.Border_image = Day.Border_image
        self.Border_image1 = Day.Border_image1
        self.Torch_image = Day.Torch_image
        self.Obstacle_image = Day.Obstacle_image
        self.Space_image = Day.Space_image
        self.Goal_image = Day.Goal_image
        self.Player_image = Day.Player_image
        self.Chest_space_image = Day.Chest_space_image
        self.Chest_goal_image = Day.Chest_goal_image

    
    def Switch(self, Day, Night):
        print(self.mode)
        print(self.Border_image)
        print(self.Border_image1)
        #day mode
        if (self.mode<1):
            self.mode=1
            print("Day mode")
            self.bg=Day.bg #canvas background
            self.fg=Day.fg #font
            self.btn_Color=Day.btn_Color #button background
            self.menu_Color=Day.menu_Color #menu color
            self.Mode=Day.Mode

            #map
            self.Border_image = Day.Border_image
            self.Border_image1 = Day.Border_image1
            self.Torch_image = Day.Torch_image
            self.Obstacle_image = Day.Obstacle_image
            self.Space_image = Day.Space_image
            self.Goal_image = Day.Goal_image
            self.Player_image = Day.Player_image
            self.Chest_space_image = Day.Chest_space_image
            self.Chest_goal_image = Day.Chest_goal_image
            return self.mode
        
        #night mode
        else:             
            self.mode=0
            print("Night mode")
            self.bg=Night.bg #canvas background
            self.fg=Night.fg #font
            self.btn_Color=Night.btn_Color #button background
            self.menu_Color=Night.menu_Color #menu color
            self.Mode=Night.Mode

            #map
            self.Border_image = Night.Border_image
            self.Border_image1 = Night.Border_image1
            self.Torch_image = Night.Torch_image
            self.Obstacle_image = Night.Obstacle_image
            self.Space_image = Night.Space_image
            self.Goal_image = Night.Goal_image
            self.Player_image = Night.Player_image
            self.Chest_space_image = Night.Chest_space_image
            self.Chest_goal_image = Night.Chest_goal_image
            return self.mode

            
        

#######################################################################
        