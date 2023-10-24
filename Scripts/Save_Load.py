from tkinter import *
from datetime import*
import Buttons_and_Labels


def Save (player):#Writes the current level into the save file & and creates it when the user saves for the very first time
    try: # File found & read
        f = open("Save.txt", "r")
        d = f.read()
        print(d)
    except: #No file found
        d = str(-1)
        print("No save file found. Generating Save.txt...")
        
    if(d.find("Stop")==-1 or d.find("Slot1")==-1 or d.find("Slot2")==-1 or d.find("Slot3")==-1 or d.find("Slot4")==-1): #Generates the slots if nothing's found and restarts the function
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

#This function is used to disable/enable and update the load buttons with the level, date and time found in the save file
def Great_Load():
    try: # File found & read
        f = open("Save.txt", "r")
        d = f.read()
        print(d)
    except: #No file found
        d = str(-1)
        print("Save.txt is missing")
        for i in range (0,4):
            Buttons_and_Labels.Load_buttons[i].config(state=DISABLED, bg="Grey", text="Empty", font=("Comic Sans", 20), width = '10', height = '1')
    else:
        if (d.find("Stop")==-1 or d.find("Slot1")==-1 or d.find("Slot2")==-1 or d.find("Slot3")==-1 or d.find("Slot4")==-1): #looks up for the slots and stop in save
            for i in range (0,4):
                Buttons_and_Labels.Load_buttons[i].config(state=DISABLED, bg="Grey", text="Empty", font=("Comic Sans", 20), width = '10', height = '1')
            print("Save.txt is corrupted!!!")
        else: #starts if save.txt is found and looks fine
            print("Save.txt initialised...")

            Slot_finder(d, "Slot1", 0)
            Slot_finder(d, "Slot2", 1)
            Slot_finder(d, "Slot3", 2)
            Slot_finder(d, "Slot4", 3)
    


def Slot_finder(d, Slot, i): # This function places 2 lines on the slot label: "Slot level-Y" & "Date-yy/mm/dd TIME-hh:mm:ss"
    Index_S = d.find(Slot) #This is the start index.
    Index_End = d.find("S", Index_S+1) # This is the end index. These 2 combined are used to find the interval for the date and time
    Index_D = d.find("Date", Index_S, Index_End) #The index of Date (between start and end)
    Index_T = d.find("Time", Index_D, Index_End) #The index of Time (between date and end)
    if(Index_D==-1 or Index_T==-1):
        Buttons_and_Labels.Load_buttons[i].config(state=DISABLED, bg="Grey", text="Empty", font=("Comic Sans", 20), width = '10', height = '1')
        print("%s is empty"%Slot)
    else:
        print("%s is ready"%Slot)
        container_Level = d[Index_S+6:Index_D] #Looks better without the slot
        container_Date = d[Index_D+5:Index_T] #I've used 5 in both to skip over "Date-" and "Time-"
        container_Time = d[Index_T+5:Index_End]
        Buttons_and_Labels.Load_buttons[i].config(state=NORMAL, bg="Green", text="\n%s\n%s\n%s"%(container_Level,container_Date, container_Time), font=("Comic Sans", 9), width = '23', height = '3')


def Load (player):#Load the file
     #This try is repeated in case the user deletes the save file while he's browsing the load meanu
    try: # File found & read 
        f = open("Save.txt", "r")
        d = f.read()
        print(d)
    except: #No file found
        d = str(-1)
        print("Save.txt is missing")
        for i in range (0,4):
            Buttons_and_Labels.Load_buttons[i].config(state=DISABLED, bg="Grey", text="Empty", font=("Comic Sans", 20), width = '10', height = '1')
    else:
        if (d.find("Stop")==-1 or d.find("Slot1")==-1 or d.find("Slot2")==-1 or d.find("Slot3")==-1 or d.find("Slot4")==-1): #looks up for the slots and stop in save
            for i in range (0,4):
                Buttons_and_Labels.Load_buttons[i].config(state=DISABLED, bg="Grey", text="Empty", font=("Comic Sans", 20), width = '10', height = '1')
            print("Save.txt is corrupted!!!")
        else: #Loading the Save.file!
            Slot=d.find(player.Button_Pressed)
            Level=d[Slot+12]#the index of the level
            player.level=int(Level)