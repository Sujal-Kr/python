# Table is considered as hierarchical
# To create a table the function treeview is required .
# The treeview function takes minimum two arguments that is row and column.These row and column 
# must display on some canvas and that canvas is very first aargument
# Once the table is created we can metion .The column id and the column tittle with 
# To Provide the title of the column ,the function name is adding
# once the table structure is created with 
# Tree view 
# Column Id 
# Cloumn Title then we can insert the title in the title table

from tkinter import *
from tkinter import ttk
root =Tk()
tab=ttk.Treeview(root,column=("0","1","2","3"))
# creating column heading 
tab.column("#0")
tab.heading("#0",text="SI.No")
tab.column("#1")
tab.heading("#1",text="Reg No.")
tab.column("#2")
tab.heading("#2",text="Student Name")
tab.column("#3")
tab.heading("#3",text="Result")
# inserting column values
tab.insert(parent='',index='end',iid=1,text='',values=('101','Sujal','Pass'))
tab.insert(parent='',index='end',iid=2,text='',values=('102','Suman','Pass'))
tab.pack()
root.mainloop()