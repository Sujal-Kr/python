# that can be added to the fucntion 
# To repersent a sperate on the menu bar 
# To make a sub menu for a single menu option the command is add_cascade.
# We can arrange the menu bar on the window with the command config
from tkinter import *
top=Tk()
# Create a top leve menu
menubar=Menu(top)


break_meuu=Menu(menubar)
break_meuu.add_command(label="Poha")
break_meuu.add_command(label="Sandwich")
menubar.add_cascade(label="Breakfast",menu=break_meuu)

lunch_menu=Menu(menubar)
lunch_menu.add_command(label="Thali")
lunch_menu.add_command(label="Special Thali")
menubar.add_cascade(label="Luch",menu=lunch_menu)


dinner_menu=Menu(menubar)
dinner_menu.add_command(label="Palak Panner")
dinner_menu.add_command(label="Gobi manchurian")
menubar.add_cascade(label="Dinner",menu=dinner_menu)
# display the menu
top.config(menu=menubar)
top.mainloop()