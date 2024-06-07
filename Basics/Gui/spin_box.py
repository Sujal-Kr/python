#  A spin box is a type of list box that displays one items at a time and scrollbar is present there by default.
# The spin box takes some vaues and works just like the list box ,we have to provide all the values together with the spin value


from tkinter import *
root=Tk()
spin_box=Spinbox(root,from_=0,to=20,values=(101,102,103,104,105,106,107))
spin_box.pack()
root.mainloop()