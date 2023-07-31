#Movement and anti-collision function
def walk(matrix, player, bcolor, ocolor, scolor, pcolor, ccolor, pressed_btn):
        print("mama")

        #UP
        if(pressed_btn=="Up"):
        #With a box
            if(matrix[player.current_x][player.current_y-1].cget("bg")==ccolor): ## Checks to see if there's any box above
                if (matrix[player.current_x][player.current_y-2].cget("bg")==bcolor or matrix[player.current_x][player.current_y-2].cget("bg")==ocolor ): ##Verifies if there are obstacles above(2 Steps)
                    return
                else:
                    matrix[player.current_x][player.current_y].config(bg=scolor) ##Turns the old position into free space
                    matrix[player.current_x][player.current_y-2].config(bg=ccolor) ##Moves the box upside
                    player.current_y -= 1
                    
        #Without a box 
            elif (matrix[player.current_x][player.current_y-1].cget("bg")==bcolor or matrix[player.current_x][player.current_y-1].cget("bg")==ocolor ): ##Verifies if there are obstacles above(1 Step)
                return
            else:
                matrix[player.current_x][player.current_y].config(bg=scolor) ##Turns the old position into free space
                player.current_y -= 1
        

        #Left   
        elif(pressed_btn=="Left"):
        #With a box 
            if (matrix[player.current_x-1][player.current_y].cget("bg")==ccolor):
                if (matrix[player.current_x-2][player.current_y].cget("bg")==bcolor or matrix[player.current_x-2][player.current_y].cget("bg")==ocolor): ##Verifies if there are obstacles to the left side(2 Steps)
                    return
                else:
                    matrix[player.current_x][player.current_y].config(bg=scolor) ##Turns the old position into free space
                    matrix[player.current_x-2][player.current_y].config(bg=ccolor) ##Moves the box to the left
                    player.current_x -= 1
        #Without a box
            elif (matrix[player.current_x-1][player.current_y].cget("bg")==bcolor or matrix[player.current_x-1][player.current_y].cget("bg")==ocolor): ##Verifies if there are obstacles to the left side(1 Step)
                return
            else:
                matrix[player.current_x][player.current_y].config(bg=scolor) ##Turns the old position into free space
                player.current_x -= 1
        

        #Down
        if(pressed_btn=="Down"):
        #With a box
            if(matrix[player.current_x][player.current_y+1].cget("bg")==ccolor): ## Checks to see if there's any box above
                if (matrix[player.current_x][player.current_y+2].cget("bg")==bcolor or matrix[player.current_x][player.current_y-2].cget("bg")==ocolor ): ##Verifies if there are obstacles bellow(2 Steps)
                    return
                else:
                    matrix[player.current_x][player.current_y].config(bg=scolor) ##Turns the old position into free space
                    matrix[player.current_x][player.current_y+2].config(bg=ccolor) ##Moves the box bellow
                    player.current_y += 1
                    
        #Without a box 
            elif (matrix[player.current_x][player.current_y+1].cget("bg")==bcolor or matrix[player.current_x][player.current_y-1].cget("bg")==ocolor ): ##Verifies if there are obstacles bellow(1 Step)
                return
            else:
                matrix[player.current_x][player.current_y].config(bg=scolor) ##Turns the old position into free space
                player.current_y += 1
        

        #Right   
        elif(pressed_btn=="Right"):
        #With a box 
            if (matrix[player.current_x+1][player.current_y].cget("bg")==ccolor):
                if (matrix[player.current_x+2][player.current_y].cget("bg")==bcolor or matrix[player.current_x-2][player.current_y].cget("bg")==ocolor): ##Verifies if there are obstacles to the right side(2 Steps)
                    return
                else:
                    matrix[player.current_x][player.current_y].config(bg=scolor) ##Turns the old position into free space
                    matrix[player.current_x+2][player.current_y].config(bg=ccolor) ##Moves the box to the right
                    player.current_x += 1
        #Without a box
            elif (matrix[player.current_x+1][player.current_y].cget("bg")==bcolor or matrix[player.current_x-1][player.current_y].cget("bg")==ocolor): ##Verifies if there are obstacles to the right side(1 Step)
                return
            else:
                matrix[player.current_x][player.current_y].config(bg=scolor) ##Turns the old position into free space
                player.current_x += 1
        
        
        matrix[player.current_x][player.current_y].config(bg=pcolor)
        
        