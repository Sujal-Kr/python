# A text box is diffrent form text area as it usally contains the text in a single statement.
# import tkinter as tk
from tkinter import *
m=Tk()
m.geometry=("400*250")
text_box=Text(m,height=14,width=40,wrap="word",font=('Arial',16,'bold'),foreground="red",background="yellow")
text_box.insert('end',"This is a message")
text_box.config(state=DISABLED)
text_box.pack(expand=True)
m.mainloop()
