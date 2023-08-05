#Movement and anti-collision function (it encapsulates everything from this module)
def walk(matrix, player, map, hml):
        print(player.Button_Pressed)
        match player.Button_Pressed:
            case "Up":
                direction(matrix, player, 0, -1, map, hml)
            case "Left":
                direction(matrix, player, -1, 0, map, hml)
            case "Down":
                direction(matrix, player, 0, 1, map, hml)
            case "Right":
                direction(matrix, player, 1, 0, map, hml)

        print(map.Left_Spots)
        matrix[player.current_x][player.current_y].config(bg=map.Color_Player)
        boxes_left(map, hml)




def direction(matrix, player, X_coordonate, Y_coordonate, map, hml):
    #with a box
    if(matrix[player.current_x+(X_coordonate) ][player.current_y+(Y_coordonate)].cget("bg")==map.Color_Chest 
        or matrix[player.current_x+(X_coordonate) ][player.current_y+(Y_coordonate)].cget("bg")==map.Color_Transform): ## Checks to see if there's any box ahead
        step_over_with_box(matrix, player, X_coordonate, Y_coordonate, map, hml)

    #Without a box 
    elif (matrix[player.current_x+(X_coordonate)][player.current_y+(Y_coordonate)].cget("bg")==map.Color_Border 
        or matrix[player.current_x+(X_coordonate)][player.current_y+(Y_coordonate)].cget("bg")==map.Color_Obstacle ): ##Verifies if there are obstacles (1 Step)
        return
    else:
        Goal_or_Space(matrix, player, map)
        step_over(matrix, player, X_coordonate, Y_coordonate, map)
        player_position(player, X_coordonate, Y_coordonate)



#The new position of the player
def player_position(player, X_coordonate, Y_coordonate): 
    player.current_x = player.current_x + (X_coordonate)
    player.current_y = player.current_y + (Y_coordonate)



##Stores the type of area that's under the user (without a box)
def step_over(matrix, player, X_coordonate, Y_coordonate, map):
    if (matrix[player.current_x+(X_coordonate)][player.current_y+(Y_coordonate)].cget("bg")==map.Color_Goal 
        or matrix[player.current_x+(X_coordonate)][player.current_y+(Y_coordonate)].cget("bg")==map.Color_Transform):#
        player.step_over=1
    elif (matrix[player.current_x+(X_coordonate)][player.current_y+(Y_coordonate)].cget("bg")!=map.Color_Goal):
        player.step_over=0
    print("step %d"%player.step_over)
    


def step_over_with_box(matrix, player, X_coordonate, Y_coordonate, map, hml):
    #With a box
    if (matrix[player.current_x+(X_coordonate+X_coordonate)][player.current_y+(Y_coordonate+Y_coordonate)].cget("bg")==map.Color_Border 
        or matrix[player.current_x+(X_coordonate+X_coordonate)][player.current_y+(Y_coordonate+Y_coordonate)].cget("bg")==map.Color_Obstacle): ##Verifies if there are obstacles ahead(2 Steps)
        return
    else:
        boxes_left(map, hml)
        Goal_or_Space(matrix, player, map)
        step_over(matrix, player, X_coordonate, Y_coordonate, map)
        if (matrix[player.current_x+(X_coordonate+X_coordonate)][player.current_y+(Y_coordonate+Y_coordonate)].cget("bg")==map.Color_Goal):
            matrix[player.current_x+(X_coordonate+X_coordonate)][player.current_y+(Y_coordonate+Y_coordonate)].config(bg=map.Color_Transform) ##Moves the box inside goal area and transforms it
            map.Left_Spots -= 1 #Decreases the goal slots area when a box is over it
        else:
            if (matrix[player.current_x+(X_coordonate)][player.current_y+(Y_coordonate)].cget("bg")==map.Color_Transform):
                map.Left_Spots += 1 #Increase the goal area if the player pushes a box out of it
            matrix[player.current_x+(X_coordonate+X_coordonate)][player.current_y+(Y_coordonate+Y_coordonate)].config(bg=map.Color_Chest) ##Moves the box on empty space
        player_position(player, X_coordonate, Y_coordonate)



##Stores the type of area that's under the user and the box
def Goal_or_Space(matrix, player, map):
    if (player.step_over==1):
        matrix[player.current_x][player.current_y].config(bg=map.Color_Goal)
    elif (player.step_over==0):
        matrix[player.current_x][player.current_y].config(bg=map.Color_Space)



#this function changes the number of boxes left
def boxes_left(map, hml):
    if (map.Left_Spots > 1):
        hml.config(text="%d boxes left"%map.Left_Spots)
    
    elif (map.Left_Spots == 1):
        hml.config(text="1 box left")

    else:
        hml.config(text="No boxes left")
