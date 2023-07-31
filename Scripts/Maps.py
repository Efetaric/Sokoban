from tkinter import *
#First tutorial map or first start map
def Maps_order(pressed_btn, matrix, ocolor, scolor, gcolor, player):
    if (pressed_btn=="Tutorial"):    
        tutorial_Map1(matrix, ocolor, scolor, gcolor, player)

#Standard map 
def Standard_map(window, matrix, bcolor, scolor):
    columns=[0]*15
    for j in range(0,15):
        for i in range (0,15): 
            matrix[j].append(columns[i])
            matrix[j][i]=Label(window, height=1, width=3, bg=scolor, relief=RAISED, state=NORMAL)
            matrix[j][i].grid(row=i, column=j, sticky = NSEW, padx=1, pady=1)
            ##Makes the outter borders
            if (j==0 or j==14 or i==0 or i==14):
                matrix[j][i].config(bg=bcolor)     
    matrix[7][5].config(bg="Magenta")
#First tutorial map
def tutorial_Map1(matrix, ocolor, scolor, gcolor, player):
    player.current_x=5
    player.current_y=7
    for j in range(1,14):
        for i in range (1,14): 
            if (j==7 and 4<i<10):
                matrix[i][j].config(bg=scolor)
                if (i==9):
                    matrix[i][j].config(bg=gcolor)
            else:
                matrix[i][j].config(bg=ocolor) 
                

        