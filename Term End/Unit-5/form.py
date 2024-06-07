from tkinter import *
def display():
    str=name_area.get("1.0",END)
    info.config(text=str)
root=Tk()
root.geometry("400x400")
name=Label(root,text="What is the name of the")
name_area=Text(root,height=1,width=30)
btn=Button(root,text="clik",command=display)
info=Label(root,text="")


name.pack()
name_area.pack()
btn.pack()
info.pack()
mainloop()