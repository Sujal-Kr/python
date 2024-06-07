from tkinter import *
root = Tk()
root.geometry("400x400")

first = Label(root, text="", height=2, width=30, bg="orange")
first.pack()
second = Label(root, text="",height=2,width=30)
second.pack()
third = Label(root, text="",height=2,width=30,bg="green")
third.pack()
root.mainloop()
