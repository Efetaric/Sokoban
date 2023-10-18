from tkinter import *

def Save (player):#Writes the current level into the save file & and creates it when the user saves for the very first time
    f = open("Save.txt", "r")
    d = f.read()
    #print(d)


    if(d.find(player.Button_Pressed) == -1 or d.find("Stop")==-1): #Generates the slots if nothing's and restarts the function
        f = open("Save.txt", "w")
        f.write("Slot1_Off\nSlot2_Off\nSlot3_Off\nSlot4_Off\nStop")
        f.close()
        Save(player) 
    else: #Saves the level
        print("fck")
        min = d.find(player.Button_Pressed)
        avg = min + 6 #O from off
        max = d.find("S", min+1) 
        s1 = d[:avg]
        s2 = str(player.level)
        s3 = d[max-1:] #-1 because the notepad looks better with \n between slots
        print(s1+s2+s3)

        f = open("Save.txt", "w")
        f.write(s1+s2+s3)
        f.close()



def Load (player):#Load the file
    f = open("Save.txt", "r")
    d = f.read()
    print(d)


