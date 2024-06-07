# varoius type of message box are available as GUI Objejct .Some of them are as as follows 
# Information Box:This message box displays information and usally have only one button (OK) 
# Alone Box:This message box displays any warning message and take the action accordingly.
# Error Box:This message box Occurs whenever ther is an error in the program. basically ot works just like a warning message.But it is having three buttons Yes , No and Cancel.
# Question Box:This message box usally displays any question .
# For example :Delete a File .Save a File etc.
# This Message box usally have three buttons Yes , No and Cancel

from tkinter import *
from tkinter import messagebox
root =Tk()
root.geometry("300x400")
w=Label(root,text="This is a label", font="50")
w.pack()
messagebox.showinfo("University","Tommorow is Holiday")
messagebox.showwarning("Class Teacher","Submit your assignment")
messagebox.showerror("Student","I am not able to solve it")
messagebox.askquestion("parents","Are you Dumb")
messagebox.askokcancel("Friends","Wanna Play?")
messagebox.askyesno("Teacher","Are you taller than 6ft")
messagebox.askretrycancel("System","Can't open a File")

w.mainloop()