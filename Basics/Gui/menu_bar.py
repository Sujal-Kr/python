# that can be added to the fucntion 
# To repersent a sperate on the menu bar 
# To make a sub menu for a single menu option the command is add_cascade.
# We can arrange the menu bar on the window with the command config
from tkinter import *
top=Tk()
# Create a top leve menu
menubar=Menu(top)
menubar.add_command(label="Breakfast")
menubar.add_command(label="Lunch")
menubar.add_command(label="Dinner")


# display the menu
top.config(menu=menubar)
top.mainloop()