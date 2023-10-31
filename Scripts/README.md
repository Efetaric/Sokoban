# Sokoban
<pre>

Objective
Move the boxes over their designated spots.

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Functions implemented and functions that are being worked on at this moment:
#The user can move the character up, down, left and right;
#The character can go only through the empty space, it can't go through the outter borders or the obstacles;
#The boxes can be pushed by the user, only if there's no obstacle blocking the box;
#Whenever a box is moved over it's designated area, the box turns from magenta into purple and the user can see how many more he has to push. If
the user tries to push the transformed box back into empty space: it turns again into magenta, the label increases the number of boxes left with
1 and the goal area needs to be filled again. When every box is pushed a button "next" appears and the user can go to the following map.
#It's possible to return to the menu anytime.
#Instructions window is ready
#Save/Load is ready. There are designed many safety nets in case the User loses/erases the save file. As long as there's not added "D" and "T" or random slots I don't think there can be any problems.

Problems:
It has a bit of lag when the map is generated.

Working on:
-Night/Day mode
-Delete load files function, even if it isn't necesary since the save buttons rewrite the save file each time.
-Create a "New game" button that activates after the users passes level 1. 
-Maps are still lacking. I'll focus on them after I finish the above functions.
</pre>