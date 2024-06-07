import tkinter as tk
m=tk.Tk()
label = tk.Label(m, text="What is your name?", height=2, width=30)

# Create a Text widget with the parent window
text = tk.Text(m, height=2, width=30)

# Pack the widgets
label.pack()
text.pack()

# Run the application
m.mainloop()

