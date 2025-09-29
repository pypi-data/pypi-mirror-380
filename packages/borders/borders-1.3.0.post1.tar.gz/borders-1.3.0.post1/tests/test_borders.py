from borders import frame
import os

menu_list = [
    ("Task Overview","white","red"),
    "1234567890123456789012345678901234567890",
    "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    "AAA"]
    

#print("\033[40m black")
#frame(menu_list, colour=95, spacing=1, max_width=70)
#frame(menu_list, colour=34, text_background=40, frame_colour=33, frame_background=41, spacing=2, max_width=70)
#frame(menu_list)
#print(frame.__doc__)

#print("\033[42;95m colour")

fore_colours = [30,31,32,33,34,35,36,37,90,91,92,93,94,95,96,97]
back_colours = [40,41,42,43,44,45,46,47,100,101,102,103,104,105,106,107]

frame(menu_list, colour="bright cyan", frame_colour="bright cyan", spacing=1)
