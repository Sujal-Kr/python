# Program that shows list of courses completed by mca  having  horziontal and vertical scroll bar .
# on click of the list display the respective teacher name in textbox


import tkinter as tk

# Sample data
courses = {
    "Data Structures": "Prof. John Smith",
    "Algorithms": "Dr. Emily Brown",
    "Database Management": "Prof. Alan Turing",
    "Computer Networks": "Dr. Grace Hopper",
    "Operating Systems": "Prof. Donald Knuth",
    "Software Engineering": "Prof. Barbara Liskov",
    "Artificial Intelligence": "Dr. Andrew Ng",
    "Machine Learning": "Prof. Geoffrey Hinton",
    "Big Data Analytics": "Dr. Daphne Koller",
    "Cloud Computing": "Prof. Tim Berners-Lee"
}

def on_course_select(event):
    selected_course = course_listbox.get(course_listbox.curselection())
    teacher_name = courses[selected_course]
    teacher_textbox.delete(0, tk.END)
    teacher_textbox.insert(0, teacher_name)

# Create the main window
root = tk.Tk()
root.title("Course and Faculty Information")

# Create a listbox
course_listbox = tk.Listbox(root, height=10)
course_listbox.pack(padx=10, pady=10)

# Populate the listbox with courses
for course in courses:
    course_listbox.insert(tk.END, course)

# Bind the select event to the listbox
course_listbox.bind('<<ListboxSelect>>', on_course_select)

# Create a label and textbox for displaying the teacher's name
teacher_label = tk.Label(root, text="Faculty Name:")
teacher_label.pack(padx=10, pady=5)

teacher_textbox = tk.Entry(root, width=50)
teacher_textbox.pack(padx=10, pady=5)

# Run the application
root.mainloop()
