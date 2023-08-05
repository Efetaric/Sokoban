# Sokoban
In this game the user has to push the boxes on their designed spots.
It's pretty intuitive and it also has special features like: teleleportation and experience points.

Controls:
The four purple buttons move the character up, left, down and left;
When the character is over a teleporter and only 2 teleports are on the map, the user can press the middle button to teleport;
If there are more than one teleports, there'll appear 3 buttons: one or teleporting and two for picking which telport is being used.

Attention: The chest can't be moved over the teleport. Be careful to no block your acces to the other side.


Functions implemented and functions that are being worked on at this moment:
When the game is opened two buttons appear: one is for learning how to play the game and one is for starting the game normally;
The user can move the character up, down, left and right;
The character can go only through the empty space, it can't go through the outter borders or the obstacles;
The boxes can be pushed by the user, only if there's no obstacle blocking the box;
Whenever a box is moved over it's designated area the box turns from magenta into purple and the user can see how many more he has to push. If the user tries to push the transformed box back into empty space: it turns again into magenta, the label increases the number of boxes left with 1 and the goal area needs to be filled again. When every box is pushed a button "next map" appears and the user can go to the following map.

Problems:
It has a bit of lag when the map is generated.

Working on: Next button and teleport fuction
