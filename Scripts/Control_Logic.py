#Movement and anti-collision function (it encapsulates everything from this module)
def walk(matrix, player, bcolor, ocolor, scolor, pcolor, ccolor, gcolor, tcolor, pressed_btn, map, hml):
        print(pressed_btn)
        match pressed_btn:
            case "Up":
                direction(matrix, player, 0, -1, 0, -1, bcolor, ocolor, scolor, ccolor, gcolor, tcolor, map, hml)
            case "Left":
                direction(matrix, player, -1, 0, -1, 0, bcolor, ocolor, scolor, ccolor, gcolor, tcolor, map, hml)
            case "Down":
                direction(matrix, player, 0, 1, 0, 1, bcolor, ocolor, scolor, ccolor, gcolor, tcolor, map, hml)
            case "Right":
                direction(matrix, player, 1, 0, 1, 0, bcolor, ocolor, scolor, ccolor, gcolor, tcolor, map, hml)

        print(map.Left_Spots)
        matrix[player.current_x][player.current_y].config(bg=pcolor)
        boxes_left(map, hml)


def direction(matrix, player, X_coordonate, Y_coordonate, X_box, Y_box, bcolor, ocolor, scolor, ccolor, gcolor, tcolor, map, hml):
    #with a box
    if(matrix[player.current_x+(X_coordonate) ][player.current_y+(Y_coordonate)].cget("bg")==ccolor 
        or matrix[player.current_x+(X_coordonate) ][player.current_y+(Y_coordonate)].cget("bg")==tcolor): ## Checks to see if there's any box ahead
        step_over_with_box(matrix, player, X_coordonate, Y_coordonate, X_box, Y_box,  bcolor, ocolor, scolor, ccolor, gcolor, tcolor, map, hml)

    #Without a box 
    elif (matrix[player.current_x+(X_coordonate)][player.current_y+(Y_coordonate)].cget("bg")==bcolor or matrix[player.current_x+(X_coordonate)][player.current_y+(Y_coordonate)].cget("bg")==ocolor ): ##Verifies if there are obstacles (1 Step)
            return
    else:
        Goal_or_Space(matrix, player, scolor, gcolor)
        step_over(matrix, player, X_coordonate, Y_coordonate, gcolor, tcolor)
        player_position(player, X_coordonate, Y_coordonate)


#The new position of the player
def player_position(player, X_coordonate, Y_coordonate): 
    player.current_x = player.current_x + (X_coordonate)
    player.current_y = player.current_y + (Y_coordonate)


##Stores the type of area that's under the user (without a box)
def step_over(matrix, player, X_coordonate, Y_coordonate, gcolor, tcolor):
    if (matrix[player.current_x+(X_coordonate)][player.current_y+(Y_coordonate)].cget("bg")==gcolor 
        or matrix[player.current_x+(X_coordonate)][player.current_y+(Y_coordonate)].cget("bg")==tcolor):#
        player.step_over=1
    elif (matrix[player.current_x+(X_coordonate)][player.current_y+(Y_coordonate)].cget("bg")!=gcolor):
        player.step_over=0
    print("step %d"%player.step_over)
    

def step_over_with_box(matrix, player, X_coordonate, Y_coordonate, X_box, Y_box,  bcolor, ocolor, scolor, ccolor, gcolor, tcolor, map, hml):
    #With a box
    if (matrix[player.current_x+(X_coordonate+X_box)][player.current_y+(Y_coordonate+Y_box)].cget("bg")==bcolor 
        or matrix[player.current_x+(X_coordonate+X_box)][player.current_y+(Y_coordonate+Y_box)].cget("bg")==ocolor): ##Verifies if there are obstacles ahead(2 Steps)
        return
    else:
        boxes_left(map, hml)
        Goal_or_Space(matrix, player, scolor, gcolor)
        step_over(matrix, player, X_coordonate, Y_coordonate, gcolor, tcolor)
        if (matrix[player.current_x+(X_coordonate+X_box)][player.current_y+(Y_coordonate+Y_box)].cget("bg")==gcolor):
            matrix[player.current_x+(X_coordonate+X_box)][player.current_y+(Y_coordonate+Y_box)].config(bg=tcolor) ##Moves the box inside goal area and transforms it
            map.Left_Spots -= 1 #Decreases the goal slots area when a box is over it
        else:
            if (matrix[player.current_x+(X_box)][player.current_y+(Y_box)].cget("bg")==tcolor):
                map.Left_Spots += 1 #Increase the goal area if the player pushes a box out of it
            matrix[player.current_x+(X_coordonate+X_box)][player.current_y+(Y_coordonate+Y_box)].config(bg=ccolor) ##Moves the box on empty space
        player_position(player, X_coordonate, Y_coordonate)

##Stores the type of area that's under the user and the box
def Goal_or_Space(matrix, player, scolor, gcolor):
    if (player.step_over==1):
        matrix[player.current_x][player.current_y].config(bg=gcolor)
    elif (player.step_over==0):
        matrix[player.current_x][player.current_y].config(bg=scolor)



#this function changes the number of boxes left
def boxes_left(map, hml):
    if (map.Left_Spots > 1):
        hml.config(text="%d boxes left"%map.Left_Spots)
    
    elif (map.Left_Spots == 1):
        hml.config(text="1 box left")

    else:
        hml.config(text="No boxes left")
