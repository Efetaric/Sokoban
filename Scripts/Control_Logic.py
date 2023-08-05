#Movement and anti-collision function
def walk(matrix, player, bcolor, ocolor, scolor, pcolor, ccolor, gcolor, tcolor, pressed_btn, stats, hml):
        print(pressed_btn)
#UP
        if(pressed_btn=="Up"):
        #With a box
            if(matrix[player.current_x][player.current_y-1].cget("bg")==ccolor): ## Checks to see if there's any box above
                if (matrix[player.current_x][player.current_y-2].cget("bg")==bcolor or matrix[player.current_x][player.current_y-2].cget("bg")==ocolor ): ##Verifies if there are obstacles above(2 Steps)
                    return
                elif (matrix[player.current_x][player.current_y-2].cget("bg")==gcolor):

                    stats -= 1
                    boxes_left(stats, hml)
                    #Stores and changes the stepped over square
                    Goal_or_Space(matrix, player, scolor, gcolor)
                    step_over(matrix, player, scolor, gcolor, pressed_btn, stats, hml)
                    matrix[player.current_x][player.current_y-2].config(bg=tcolor) ##Moves the box upside
                    player.current_y -= 1
                else:
                    stats -= 1
                    boxes_left(stats, hml)
                    #Stores and changes the stepped over square
                    Goal_or_Space(matrix, player, scolor, gcolor)
                    step_over(matrix, player, scolor, gcolor, pressed_btn, stats, hml)
                    matrix[player.current_x][player.current_y-2].config(bg=ccolor) ##Moves the box upside
                    player.current_y -= 1
                    
        #Without a box 
            elif (matrix[player.current_x][player.current_y-1].cget("bg")==bcolor or matrix[player.current_x][player.current_y-1].cget("bg")==ocolor ): ##Verifies if there are obstacles above(1 Step)
                return
            else:
                #Store and changes the stepped over square 
                Goal_or_Space(matrix, player, scolor, gcolor)
                step_over(matrix, player, scolor, gcolor, pressed_btn, stats, hml)##Turns the old position into free space/goal area
                player.current_y -= 1
        

#Left   
        elif(pressed_btn=="Left"):
        #With a box 
            if (matrix[player.current_x-1][player.current_y].cget("bg")==ccolor):
                if (matrix[player.current_x-2][player.current_y].cget("bg")==bcolor or matrix[player.current_x-2][player.current_y].cget("bg")==ocolor): ##Verifies if there are obstacles to the left side(2 Steps)
                    return
                else:
                    #Store and changes the stepped over square 
                    Goal_or_Space(matrix, player, scolor, gcolor)
                    step_over(matrix, player, scolor, gcolor, pressed_btn, stats, hml)
                    #Counts the boxes placed over the goal area
                    if (matrix[player.current_x-2][player.current_y].cget("bg")==gcolor): 
                        stats -= 1
                        boxes_left(stats, hml)

                    matrix[player.current_x-2][player.current_y].config(bg=ccolor) ##Moves the box to the left
                    player.current_x -= 1
        #Without a box
            elif (matrix[player.current_x-1][player.current_y].cget("bg")==bcolor or matrix[player.current_x-1][player.current_y].cget("bg")==ocolor): ##Verifies if there are obstacles to the left side(1 Step)
                return
            else:
                #Store and changes the stepped over square 
                #Stores and changes the stepped over square
                Goal_or_Space(matrix, player, scolor, gcolor)
                step_over(matrix, player, scolor, gcolor, pressed_btn, stats, hml)
                player.current_x -= 1
        


#Down
        elif(pressed_btn=="Down"):
        #With a box
            if(matrix[player.current_x][player.current_y+1].cget("bg")==ccolor): ## Checks to see if there's any box above
                if (matrix[player.current_x][player.current_y+2].cget("bg")==bcolor or matrix[player.current_x][player.current_y+2].cget("bg")==ocolor ): ##Verifies if there are obstacles bellow(2 Steps)
                    return
                else:
                    #Store and changes the stepped over square 
                    Goal_or_Space(matrix, player, scolor, gcolor)
                    step_over(matrix, player, scolor, gcolor, pressed_btn, stats, hml)
                    #Counts the boxes placed over the goal area
                    if (matrix[player.current_x][player.current_y+2].cget("bg")==gcolor): 
                        stats -= 1
                        boxes_left(stats, hml)

                    matrix[player.current_x][player.current_y+2].config(bg=ccolor) ##Moves the box bellow
                    player.current_y += 1
        #Without a box 
            elif (matrix[player.current_x][player.current_y+1].cget("bg")==bcolor or matrix[player.current_x][player.current_y+1].cget("bg")==ocolor ): ##Verifies if there are obstacles bellow(1 Step)
                return
            else:
                #Store and changes the stepped over square 
                Goal_or_Space(matrix, player, scolor, gcolor)
                step_over(matrix, player, scolor, gcolor, pressed_btn, stats, hml)
                player.current_y += 1
        


#Right   
        elif(pressed_btn=="Right"):
        #With a box 
            if (matrix[player.current_x+1][player.current_y].cget("bg")==ccolor):
                if (matrix[player.current_x+2][player.current_y].cget("bg")==bcolor or matrix[player.current_x+2][player.current_y].cget("bg")==ocolor): ##Verifies if there are obstacles to the right side(2 Steps)
                    return
                else:
                    #Store and changes the stepped over square 
                    Goal_or_Space(matrix, player, scolor, gcolor)
                    step_over(matrix, player, scolor, gcolor, pressed_btn, stats, hml)
                    #Counts the boxes placed over the goal area
                    if (matrix[player.current_x+2][player.current_y].cget("bg")==gcolor): 
                        stats -= 1
                        boxes_left(stats, hml)

                    matrix[player.current_x+2][player.current_y].config(bg=ccolor) ##Moves the box to the right
                    player.current_x += 1
        #Without a box
            elif (matrix[player.current_x+1][player.current_y].cget("bg")==bcolor or matrix[player.current_x+1][player.current_y].cget("bg")==ocolor): ##Verifies if there are obstacles to the right side(1 Step)
                return
            else:
                #Store and changes the stepped over square 
                Goal_or_Space(matrix, player, scolor, gcolor)
                step_over(matrix, player, scolor, gcolor, pressed_btn, stats, hml)
                player.current_x += 1
        
        print(stats)
        matrix[player.current_x][player.current_y].config(bg=pcolor)
        boxes_left(stats, hml)



##Stores the type of area that's under the user (without a box)
def step_over(matrix, player, scolor, gcolor, pressed_btn, stats, hml):

    #Without box
    if (pressed_btn=="Up" and matrix[player.current_x][player.current_y-1].cget("bg")==gcolor):
        player.step_over=1
    elif (pressed_btn=="Up" and matrix[player.current_x][player.current_y-1].cget("bg")!=gcolor):
        player.step_over=0


    elif (pressed_btn=="Left" and matrix[player.current_x-1][player.current_y].cget("bg")==gcolor):
        player.step_over=1
    elif (pressed_btn=="Left" and matrix[player.current_x-1][player.current_y].cget("bg")!=gcolor):
        player.step_over=0

    
    elif (pressed_btn=="Down" and matrix[player.current_x][player.current_y+1].cget("bg")==gcolor):
        player.step_over=1
    elif (pressed_btn=="Down" and matrix[player.current_x][player.current_y+1].cget("bg")!=gcolor):
        player.step_over=0


    elif (pressed_btn=="Right" and matrix[player.current_x+1][player.current_y].cget("bg")==gcolor):
        player.step_over=1
    elif (pressed_btn=="Right" and matrix[player.current_x+1][player.current_y].cget("bg")!=gcolor):
        player.step_over=0
    print("step %d"%player.step_over)

def step_over_with_box(matrix, player, scolor, gcolor, pressed_btn, stats, hml):
        #With a box
   if (pressed_btn=="Up" and matrix[player.current_x][player.current_y-1].cget("bg")==gcolor):
        player.step_over=1

##Stores the type of area that's under the user and the box
def Goal_or_Space(matrix, player, scolor, gcolor):
    if (player.step_over==1):
        matrix[player.current_x][player.current_y].config(bg=gcolor)
    elif (player.step_over==0):
        matrix[player.current_x][player.current_y].config(bg=scolor)



#this function changes the number of boxes left
def boxes_left(stats, hml):
    if (stats > 1):
        hml.config(text="%d boxes left"%stats)
    
    elif (stats == 1):
        hml.config(text="1 box left")

    else:
        hml.config(text="No boxes left")
