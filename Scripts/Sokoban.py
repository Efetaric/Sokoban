from tkinter import *
import Classes
import Maps 
import Buttons_and_Labels
import Animation



def position(root): #Sets the main window

    width = 600
    height = 700

    # screen width and height
    screen_width = root.winfo_screenwidth() # width of the screen
    screen_height = root.winfo_screenheight() # height of the screen

    # screen coordonates for root
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    root.geometry('%dx%d+%d+%d' % (width, height, x, y))


root = Tk()
root.config()
position(root)


######################################################################

User = Classes.Player(
    level=1,
    X=1,
    Y=2, 
    step_over=0, 
    Button_Pressed='No_Button_Pressed',
    inbetween=0)


Day = Classes.Aspect(
    #Buttons
    bg="Darkgrey", 
    fg="Black",
    btn_Color="Deep sky blue",
    menu_Color="Green",
    Mode='Sprites/Day_Mode.png',
    #Map
    Border_image="Sprites/Wall_dTop.png",
    Border_image1="Sprites/Wall_dBottom.png",
    Torch_image = "Sprites/Wall_dTorch.png",
    Obstacle_image="Sprites/Obstacle_dBush1.png", 
    Space_image="Sprites/Space_day.png", 
    Goal_image="Sprites/Goal_day.png", 
    Player_image="Sprites/Player_dRSpace0.png", 
    Chest_space_image="Sprites/Chest_dSpace.png", 
    Chest_goal_image="Sprites/Chest_dGoal.png")


Night = Classes.Aspect(
    bg="Black", 
    fg="Darkgrey",
    btn_Color="Yellow",
    menu_Color="Yellow",
    Mode="Sprites/Night_Mode.png",
    
    #Map
    Border_image="Sprites/Wall_nTop.png",
    Border_image1="Sprites/Wall_nBottom.png",
    Torch_image = "Sprites/Wall_nTorch0.png", 
    Obstacle_image="Sprites/Obstacle_dBush1.png", 
    Space_image="Sprites/Space_Night.png", 
    Goal_image="Sprites/Goal_Night.png", 
    Player_image="Sprites/Player_dRSpace0.png", 
    Chest_space_image="Sprites/Wall_dTop.png", 
    Chest_goal_image="Sprites/Chest_dGoal.png")

Day_or_Night = Classes.Day_Night(
    Boxes=1,
    Left_Spots=1,
    Day=Day
)

root.configure(background=Day_or_Night.bg)
canvas = Canvas(bg="Black", highlightthickness=0)
Maps.Standard_map(canvas)#Generates the map
Buttons_and_Labels.initialize_every_button(
    root, canvas, User, 
    Day_or_Night, Day, Night)


########################################################################
Animation.Initialise_images()
Animation.Animation_Map(root, Day_or_Night, 0)
Animation.Animation_Player(root, Day_or_Night, User, 0)

root.mainloop()


