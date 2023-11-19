from tkinter import *
from datetime import*
import Buttons_and_Labels

#Writes the current level into the save file
#& creates it when the user saves for the very first time
def Save (player):
    try: # File found & read
        f = open("Save.txt", "r")
        d = f.read()
        print(d)
    except: #No file found
        d = str(-1)
        print("No save file found. Generating Save.txt...")
        
    #Generates the slots if nothing's found and restarts the function
    if(d.find("Stop")==-1
            or d.find("Slot1")==-1 
            or d.find("Slot2")==-1 
            or d.find("Slot3")==-1 
            or d.find("Slot4")==-1): 
        f = open("Save.txt", "w")
        f.write("Slot1 Empty\nSlot2 Empty\nSlot3 Empty\nSlot4 Empty\nStop")
        f.close()
        Save(player)   
    else: #Saves the level
        print("Save")
        min = d.find(player.Button_Pressed)
        avg = min + 6 #E from empty
        max = d.find("S", min+1) 
        s1 = d[:avg]
        s2 = "Level-"+str(player.level)
        s3 = d[max-1:] #-1 because the notepad looks better with \n between slots
        dt = datetime.today().strftime(" Date-%Y/%m/%d Time-%H:%M:%S")
        fullstring=s1+s2+dt+s3
        f = open("Save.txt", "w")
        f.write(fullstring)
        f.close()

#Used to disable/enable and update the load buttons with the data
#For the Load button from the Menu canvas
def Great_Load(): 
    try: # File found & read
        f = open("Save.txt", "r")
        d = f.read()
        #print(d)
    except: #No file found
        d = str(-1)
        print("Save.txt is missing")
        for i in range (0,4):
            Buttons_and_Labels.Load_buttons[i].config(
                state=DISABLED, bg="Grey", text="Empty", 
                font=("Comic Sans", 33), width = '8', height = '1')
    #looks up for the slots and stop in save
    else:
        if (d.find("Stop")==-1 
                or d.find("Slot1")==-1 
                or d.find("Slot2")==-1 
                or d.find("Slot3")==-1 
                or d.find("Slot4")==-1): 
            for i in range (0,4):
                Buttons_and_Labels.Load_buttons[i].config(
                    state=DISABLED, bg="Grey", text="Empty", 
                    font=("Comic Sans", 33), width = '8', height = '1')
            print("Save.txt is corrupted!!!")
        #starts if save.txt is found and looks fine
        else: 
            print("Save.txt initialised...")

            Slot_finder(d, "Slot1", 0)
            Slot_finder(d, "Slot2", 1)
            Slot_finder(d, "Slot3", 2)
            Slot_finder(d, "Slot4", 3)
    

#Places 2 lines on the slot label: "Slot level-Y" & "Date-yy/mm/dd TIME-hh:mm:ss"
def Slot_finder(d, Slot, i): 
    Index_S = d.find(Slot) #Start index.
    Index_End = d.find("S", Index_S+1) #End index. 
    #These 2 combined are used to find the interval for the date and time
    Index_D = d.find("Date", Index_S, Index_End) #Date index
    Index_T = d.find("Time", Index_D, Index_End) #Time index 
    if(Index_D==-1 or Index_T==-1):
        Buttons_and_Labels.Load_buttons[i].config(
            state=DISABLED, bg="Grey", text="Empty", 
            font=("Comic Sans", 33), width = '8', height = '1')
        #print("%s is empty"%Slot)
    else:
        #print("%s is ready"%Slot)
        #Looks better without the slot
        container_Level = d[Index_S+6:Index_D] 
        #Used 5 in both in order to skip over "Date-" and "Time-"
        container_Date = d[Index_D+5:Index_T] 
        container_Time = d[Index_T+5:Index_End]
        Buttons_and_Labels.Load_buttons[i].config(
            state=NORMAL, bg="Green", 
            text="\n%s\n%s\n%s"%(
                container_Level, 
                container_Date, 
                container_Time), 
            font=("Comic Sans", 15), width = '19', height = '3')


def Load (player):#Load the file
    #In case the user deletes the save file while he's in load menu
    try: # File found & read 
        f = open("Save.txt", "r")
        d = f.read()
        #print(d)
    except: #No file found
        d = str(-1)
        print("Save.txt is missing")
        for i in range (0,4):
            Buttons_and_Labels.Load_buttons[i].config(
                state=DISABLED, bg="Grey", text="Empty", 
                font=("Comic Sans", 33), width = '8', height = '1')
    else:
        #looks up for the slots and stop in save
        if (d.find("Stop")==-1 
                or d.find("Slot1")==-1 
                or d.find("Slot2")==-1 
                or d.find("Slot3")==-1 
                or d.find("Slot4")==-1):
            for i in range (0,4):
                Buttons_and_Labels.Load_buttons[i].config(
                    state=DISABLED, bg="Grey", text="Empty", 
                    font=("Comic Sans", 33), width = '8', height = '1')
            print("Save.txt is corrupted!!!")
        else: #Loading the Save.file!
            Slot=d.find(player.Button_Pressed)
            Level=d[Slot+12]#the index of the level
            player.level=int(Level)
            print("%s selected!\nCurrent level:%s"%(
                player.Button_Pressed,
                Level))