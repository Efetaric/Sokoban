import Maps
import Buttons_and_Labels

def Events(
        root, canvas, Lower_Courtain, 
        player, Day_or_Night, hml, cl, 
        Next_btn, Reset_btn):
    #Escape
    Exit(root)
    #r
    Restart(
        root, player, Day_or_Night, 
        hml, cl, Next_btn, Reset_btn)
    #w
    Control(
        root, player, Day_or_Night, hml, 
        "Up", Next_btn, Reset_btn, 0, "w")
    #w
    Control(
        root, player, Day_or_Night, hml, 
        "Left", Next_btn, Reset_btn, 0, "a")
    #w
    Control(
        root, player, Day_or_Night, hml, 
        "Down", Next_btn, Reset_btn, 0, "s")
    #w
    Control(
        root, player, Day_or_Night, hml, 
        "Right", Next_btn, Reset_btn, 0, "d")

def Exit(root):
    root.bind("<Escape>", lambda event: Exit(root))
    root.quit()
    print("Exit")

#Restart/ Next
def Restart(root, player, Day_or_Night, 
        hml, cl, Next_btn, Reset_btn):
    root.bind("<r>", lambda event: [
        Maps.Maps_order(player, Day_or_Night), 
        Buttons_and_Labels.hml_cl(hml,cl,player,Day_or_Night), 
        Buttons_and_Labels.Turn_On(Next_btn, Reset_btn),
        Buttons_and_Labels.Ready(Day_or_Night), print("Restart")])

last_key=""
def Control(
        root, player, map, hml, which_button, 
        Next_btn, Reset_btn, i, key):

    root.bind("<KeyPress-%s>"%key, lambda event:[
            Buttons_and_Labels.btn_pressed("%s"%which_button, player), 
            Buttons_and_Labels.Control_Logic.walk(root, player, map, hml), 
            Buttons_and_Labels.Turn_Off(map.Left_Spots, Next_btn, Reset_btn)])
    root.bind("<KeyPress-%s>"%key)

