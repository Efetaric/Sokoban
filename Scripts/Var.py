#Used to identify the map labels
Border = 0   #Border from above
Border1 = 1  #Border wall
Obstacle = 2 #Obstacle
Space = 3    #Space
Goal = 4     #Goal
CoS = 5      #Chest over Space
CoG = 6      #Chest over Goal
Player = 7   #Player

#Uused in order to reduce the lenght of the if(s)
Collision=(Border, Border1, Obstacle)
Non_collision=(Space, Goal)
Space_T=(Space, CoS)
Goal_T=(Goal, CoG)
Chests=(CoS, CoG)
