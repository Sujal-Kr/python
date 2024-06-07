# A Button perform event handling
# A Button works with left and right click seperatly.
# After the event execution the process that takes place is know as Action.


from tkinter import *
win=Tk()
win.title("Python app")
label=Label(win,text="Button click")
label.pack()
def click():action.configure(text="Clicked" ,foreground="white", background="black")
label.configure(foreground="red")
label.configure(text="Button clicked")
action=Button(win,text="Click me",command=click)
action.pack()

win.mainloop()