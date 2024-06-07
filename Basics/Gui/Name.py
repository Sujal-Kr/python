import tkinter as tk
m=tk.Tk()
label = tk.Label(m, text="What is your name?", height=2, width=30)
text = tk.Text(m, height=2, width=30)
label.pack()
text.pack()

m.mainloop()
