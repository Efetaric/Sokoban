#Used to identify the map labels
Border = 0   #Border from above
Border1 = 1  #Border wall
Torch = 2    #Border torch
Obstacle = 3 #Obstacle
Space = 4    #Space
Goal = 5     #Goal
CoS = 6      #Chest over Space
CoG = 7      #Chest over Goal
Player = 8   #Player

#Uused in order to reduce the lenght of the if(s)
Collision=(Border, Border1, Torch, Obstacle)
Non_collision=(Space, Goal)
Space_T=(Space, CoS)
Goal_T=(Goal, CoG)
Chests=(CoS, CoG)
