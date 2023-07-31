from tkinter import *
import time 

Button_Pressed="No_Button_Pressed"
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

#This function creates the standard map
def map(window,matrix):
    columns=[0]*15
   # columns2=["Blue"]*15
    for j in range(0,15):
        for i in range (0,15): 
            matrix[j].append(columns[i])
            matrix[j][i]=Label(window, height=1, width=3, bg="Red", relief=RAISED, state=NORMAL)
            matrix[j][i].grid(row=i, column=j, sticky = NSEW, padx=1, pady=1)
            ##Makes the outter borders
            if (j==0 or j==14 or i==0 or i==14):
                matrix[j][i].config(bg="Blue")
      


#Checks which button is pressed
def btn_pressed(button):
    global Button_Pressed
    Button_Pressed=button

#start button
def begin(matrix, player):
    Up_btn = Button(bg="Purple", width = '5', height = '1', command=lambda: [btn_pressed("Up"),walk(matrix, player)])
    Up_btn.pack(side="top")
    Left_btn = Button(bg="Purple", width = '5', height = '1', command=lambda: [btn_pressed("Left"),walk(matrix, player)])
    Left_btn.place(x=182,y=370)
    Down_btn = Button(bg="Purple", width = '5', height = '1', command=lambda: [btn_pressed("Down"),walk(matrix, player)])
    Down_btn.pack(side="bottom")    
    Right_btn = Button(bg="Purple", width = '5', height = '1', command=lambda: [btn_pressed("Right"),walk(matrix, player)])
    Right_btn.place(x=270,y=370)
    #Places the player
    matrix[player.current_x][player.current_y].config(bg="Yellow")

#Movement and anti-collision function
def walk(matrix, player):
        print("mama")
        
        if(Button_Pressed=="Up"):
            if (matrix[player.current_x][player.current_y-1].cget("bg")=="Blue"): ##Verifies if there are obstacles above
                return
            else:
                matrix[player.current_x][player.current_y].config(bg="Red") ##Turns the old position into free space
                player.current_y -= 1
        
        elif(Button_Pressed=="Left"):
            if (matrix[player.current_x-1][player.current_y].cget("bg")=="Blue"): ##Verifies if there are obstacles to the left side
                return
            else:
                matrix[player.current_x][player.current_y].config(bg="Red") ##Turns the old position into free space
                player.current_x -= 1
        
        elif(Button_Pressed=="Down"):
            if (matrix[player.current_x][player.current_y+1].cget("bg")=="Blue"): ##Verifies if there are obstacles bellow
                return
            else:
                matrix[player.current_x][player.current_y].config(bg="Red") ##Turns the old position into free space
                player.current_y += 1
        
        elif(Button_Pressed=="Right"):
            if (matrix[player.current_x+1][player.current_y].cget("bg")=="Blue"): ##Verifies if there are obstacles to the right side
                return
            else:
                matrix[player.current_x][player.current_y].config(bg="Red") ##Turns the old position into free space
                player.current_x += 1
        matrix[player.current_x][player.current_y].config(bg="Yellow")
    

class Player:
    def __init__(self, level, current_x, current_y):
        self.level = level
        self.current_x = current_x
        self.current_y = current_y

######################################################################
root = Tk()
position(root)
canvas= Canvas(root, bg="Green")
map_matrix=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
map(canvas,map_matrix)
print(map_matrix[1][2].cget("bg"))
canvas.pack()

Cosmin =Player(level=1,current_x=1,current_y=2)
#Game controls
Start = Button(text="Start", font=("Comic Sans", 20),bg="Green", width = '5', height = '1', command=lambda:[begin(map_matrix, Cosmin), btn_pressed("Start"), Start.destroy()])
Start.pack(side="top")


           
root.mainloop()





